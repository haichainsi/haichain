const fs = require('fs');
const zlib = require('zlib');

// CRC32 table
const crcTable = [];
for (let n = 0; n < 256; n++) {
  let c = n;
  for (let k = 0; k < 8; k++) {
    c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
  }
  crcTable[n] = c;
}

function crc32(buf) {
  let crc = 0xffffffff;
  for (let i = 0; i < buf.length; i++) {
    crc = crcTable[(crc ^ buf[i]) & 0xff] ^ (crc >>> 8);
  }
  return (crc ^ 0xffffffff) >>> 0;
}

function makeChunk(type, data) {
  const len = data.length;
  const chunk = Buffer.alloc(12 + len);
  chunk.writeUInt32BE(len, 0);
  chunk.write(type, 4, 4, 'ascii');
  data.copy(chunk, 8);
  const typeAndData = chunk.slice(4, 8 + len);
  const crc = crc32(typeAndData);
  chunk.writeUInt32BE(crc, 8 + len);
  return chunk;
}

function cropAndSave(inputFile, outputFile) {
  const buf = fs.readFileSync(inputFile);
  const width = buf.readUInt32BE(16);
  const height = buf.readUInt32BE(20);
  
  let pos = 8;
  const idats = [];
  while (pos < buf.length) {
    const len = buf.readUInt32BE(pos);
    const type = buf.toString('ascii', pos + 4, pos + 8);
    if (type === 'IDAT') idats.push(buf.slice(pos + 8, pos + 8 + len));
    pos += 12 + len;
  }
  
  const raw = zlib.inflateSync(Buffer.concat(idats));
  const stride = width * 4;
  const uncompressed = Buffer.alloc(width * height * 4);
  let srcPos = 0;
  for (let y = 0; y < height; y++) {
    const filter = raw[srcPos++];
    const rowStart = y * stride;
    const prevRowStart = (y - 1) * stride;
    for (let x = 0; x < stride; x++) {
      const rawByte = raw[srcPos++];
      const left = x >= 4 ? uncompressed[rowStart + x - 4] : 0;
      const up = y > 0 ? uncompressed[prevRowStart + x] : 0;
      const upLeft = (y > 0 && x >= 4) ? uncompressed[prevRowStart + x - 4] : 0;
      let val = 0;
      if (filter === 0) val = rawByte;
      else if (filter === 1) val = (rawByte + left) & 0xff;
      else if (filter === 2) val = (rawByte + up) & 0xff;
      else if (filter === 3) val = (rawByte + Math.floor((left + up) / 2)) & 0xff;
      else if (filter === 4) {
        const p = left + up - upLeft;
        const pa = Math.abs(p - left);
        const pb = Math.abs(p - up);
        const pc = Math.abs(p - upLeft);
        let pr = left;
        if (pb < pa && pb < pc) pr = up;
        else if (pc < pa && pc < pb) pr = upLeft;
        val = (rawByte + pr) & 0xff;
      }
      uncompressed[rowStart + x] = val;
    }
  }

  // Find emblem bounds (non-black pixels)
  let minX = width, maxX = 0, minY = height, maxY = 0;
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = (y * width + x) * 4;
      const r = uncompressed[idx];
      const g = uncompressed[idx+1];
      const b = uncompressed[idx+2];
      if (r > 30 || g > 30 || b > 30) {
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;
        if (y < minY) minY = y;
        if (y > maxY) maxY = y;
      }
    }
  }

  console.log('Original Emblem Bounds:', { minX, maxX, minY, maxY, w: maxX - minX, h: maxY - minY });

  const emblemW = maxX - minX;
  const emblemH = maxY - minY;
  const cx = Math.round((minX + maxX) / 2);
  const cy = Math.round((minY + maxY) / 2);
  
  // Create a 1:1 square crop with 6% padding around the maximum dimension
  const maxDim = Math.max(emblemW, emblemH);
  const targetHalf = Math.round((maxDim * 1.08) / 2);
  
  const cropX0 = cx - targetHalf;
  const cropX1 = cx + targetHalf;
  const cropY0 = cy - targetHalf;
  const cropY1 = cy + targetHalf;
  const cropSize = cropX1 - cropX0;

  console.log(`Cropping square: ${cropSize}x${cropSize} around (${cx}, ${cy})`);

  // Target cropped buffer (filter byte + row bytes)
  const targetStride = cropSize * 4 + 1;
  const targetRaw = Buffer.alloc(cropSize * targetStride);
  
  let dstPos = 0;
  for (let y = cropY0; y < cropY1; y++) {
    targetRaw[dstPos++] = 0; // Filter 0 (None)
    for (let x = cropX0; x < cropX1; x++) {
      if (x < 0 || x >= width || y < 0 || y >= height) {
        // Out of bounds -> solid black
        targetRaw[dstPos++] = 0;
        targetRaw[dstPos++] = 0;
        targetRaw[dstPos++] = 0;
        targetRaw[dstPos++] = 255;
      } else {
        const srcIdx = (y * width + x) * 4;
        targetRaw[dstPos++] = uncompressed[srcIdx];
        targetRaw[dstPos++] = uncompressed[srcIdx + 1];
        targetRaw[dstPos++] = uncompressed[srcIdx + 2];
        targetRaw[dstPos++] = uncompressed[srcIdx + 3];
      }
    }
  }

  const deflated = zlib.deflateSync(targetRaw, { level: 9 });

  // PNG Header
  const signature = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

  // IHDR
  const ihdrData = Buffer.alloc(13);
  ihdrData.writeUInt32BE(cropSize, 0);
  ihdrData.writeUInt32BE(cropSize, 4);
  ihdrData[8] = 8; // Bit depth 8
  ihdrData[9] = 6; // RGBA
  ihdrData[10] = 0; // Deflate
  ihdrData[11] = 0; // Filter standard
  ihdrData[12] = 0; // Non-interlaced
  const ihdrChunk = makeChunk('IHDR', ihdrData);

  // IDAT
  const idatChunk = makeChunk('IDAT', deflated);

  // IEND
  const iendChunk = makeChunk('IEND', Buffer.alloc(0));

  const finalPng = Buffer.concat([signature, ihdrChunk, idatChunk, iendChunk]);
  fs.writeFileSync(outputFile, finalPng);
  console.log(`Saved cropped icon to ${outputFile} (${finalPng.length} bytes, ${cropSize}x${cropSize})`);
}

cropAndSave('assets/branding/haichain icon (2).png', 'assets/haisi-icon.png');
