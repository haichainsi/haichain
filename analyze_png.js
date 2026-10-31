const fs = require('fs');
const zlib = require('zlib');

function analyzePng(filePath) {
  const data = fs.readFileSync(filePath);
  // Scan for IHDR
  const width = data.readUInt32BE(16);
  const height = data.readUInt32BE(20);
  const colorType = data[25]; // 6 = RGBA, 2 = RGB, 0 = Grayscale
  
  // Find IDAT chunks
  let pos = 8;
  const idats = [];
  while (pos < data.length) {
    const len = data.readUInt32BE(pos);
    const type = data.toString('ascii', pos + 4, pos + 8);
    if (type === 'IDAT') {
      idats.push(data.slice(pos + 8, pos + 8 + len));
    }
    pos += 12 + len;
  }
  const decompressed = zlib.inflateSync(Buffer.concat(idats));
  
  // Scan first few rows to check if text is white (255) or black (0)
  let whiteCount = 0;
  let blackCount = 0;
  let transparentCount = 0;
  
  // Assuming RGBA (4 bytes per pixel + 1 filter byte per scanline)
  const bytesPerPixel = colorType === 6 ? 4 : (colorType === 2 ? 3 : 1);
  const stride = width * bytesPerPixel + 1;
  
  for (let y = 0; y < height; y++) {
    const rowOffset = y * stride + 1;
    for (let x = 0; x < width; x++) {
      const p = rowOffset + x * bytesPerPixel;
      if (colorType === 6) {
        const r = decompressed[p];
        const g = decompressed[p+1];
        const b = decompressed[p+2];
        const a = decompressed[p+3];
        if (a < 50) {
          transparentCount++;
        } else if (r > 200 && g > 200 && b > 200) {
          whiteCount++;
        } else if (r < 50 && g < 50 && b < 50) {
          blackCount++;
        }
      }
    }
  }
  console.log(`${filePath} (${width}x${height}): transparent=${transparentCount}, white=${whiteCount}, black=${blackCount}`);
}

analyzePng('assets/logo-text-1.png');
analyzePng('assets/logo-text-2.png');
analyzePng('assets/logo-haichain-si.png');
