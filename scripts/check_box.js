const fs = require('fs');
const zlib = require('zlib');

function analyzeFile(filepath) {
  const buf = fs.readFileSync(filepath);
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
  const bpp = 4;
  const stride = width * bpp;
  const uncompressed = Buffer.alloc(width * height * bpp);
  
  let srcPos = 0;
  for (let y = 0; y < height; y++) {
    const filter = raw[srcPos++];
    const rowStart = y * stride;
    const prevRowStart = (y - 1) * stride;
    for (let x = 0; x < stride; x++) {
      const rawByte = raw[srcPos++];
      const left = x >= bpp ? uncompressed[rowStart + x - bpp] : 0;
      const up = y > 0 ? uncompressed[prevRowStart + x] : 0;
      const upLeft = (y > 0 && x >= bpp) ? uncompressed[prevRowStart + x - bpp] : 0;
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

  // Check corners
  console.log('Top Left [0,0]:', [uncompressed[0], uncompressed[1], uncompressed[2], uncompressed[3]]);
  console.log('Center [1000,1000]:', [
    uncompressed[(1000 * 2000 + 1000) * 4],
    uncompressed[(1000 * 2000 + 1000) * 4 + 1],
    uncompressed[(1000 * 2000 + 1000) * 4 + 2],
    uncompressed[(1000 * 2000 + 1000) * 4 + 3]
  ]);

  // Let's find rows with significant opacity
  for (let threshold of [50, 150, 200]) {
    let minX = width, maxX = 0, minY = height, maxY = 0, count = 0;
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        const idx = (y * width + x) * 4;
        const a = uncompressed[idx + 3];
        if (a > threshold) {
          count++;
          if (x < minX) minX = x;
          if (x > maxX) maxX = x;
          if (y < minY) minY = y;
          if (y > maxY) maxY = y;
        }
      }
    }
    console.log(`Threshold ${threshold}: count=${count}, bounds=[x: ${minX}..${maxX}, y: ${minY}..${maxY}], size: ${maxX - minX}x${maxY - minY}`);
  }
}

analyzeFile('assets/haisi-icon.png');
