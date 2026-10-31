const http = require('http');

function testOversizedPayload() {
  return new Promise((resolve) => {
    // Generate 6MB payload (exceeds 5MB limit)
    const largeStr = 'x'.repeat(6 * 1024 * 1024);
    const postData = JSON.stringify({ prompt: largeStr });

    const req = http.request({
      hostname: 'localhost',
      port: 3000,
      path: '/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      },
      timeout: 5000
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        resolve({ status: res.statusCode, body: data });
      });
    });

    req.on('error', (err) => {
      resolve({ status: 'aborted/error', error: err.message });
    });

    req.write(postData);
    req.end();
  });
}

testOversizedPayload().then(res => {
  console.log('Oversized Payload Response Status (Expected 413):', res.status);
  console.log('Response Body:', res.body || res.error);
});
