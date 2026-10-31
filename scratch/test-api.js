const http = require('http');

function post(url, data) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify(data);
    const u = new URL(url);
    const req = http.request({
      hostname: u.hostname,
      port: u.port,
      path: u.pathname,
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(postData)
      }
    }, res => {
      let d = "";
      res.on("data", c => d += c);
      res.on("end", () => {
        try { resolve({ status: res.statusCode, body: JSON.parse(d) }); }
        catch (e) { resolve({ status: res.statusCode, raw: d }); }
      });
    });
    req.on("error", reject);
    req.write(postData);
    req.end();
  });
}

function get(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => {
      let d = "";
      res.on("data", c => d += c);
      res.on("end", () => {
        try { resolve({ status: res.statusCode, body: JSON.parse(d) }); }
        catch (e) { resolve({ status: res.statusCode, raw: d }); }
      });
    }).on("error", reject);
  });
}

async function test() {
  console.log("=== 1. Testing GET /api/slot ===");
  const slot = await get("http://localhost:3000/api/slot");
  console.log("Slot Result:", JSON.stringify(slot, null, 2));

  console.log("\n=== 2. Testing POST /api/validate-key for Claude ===");
  const keyTest = await post("http://localhost:3000/api/validate-key", {
    provider: "Anthropic Claude",
    apiKey: "sk-ant-api03-testMockSecretKey1234567890abcdef"
  });
  console.log("Key Validation:", JSON.stringify(keyTest, null, 2));

  console.log("\n=== 3. Testing POST /api/infer (Gateway Inference) ===");
  const inferTest = await post("http://localhost:3000/api/infer", {
    provider: "Anthropic Claude",
    model: "Claude 3.5 Sonnet",
    prompt: "How does HAICHAIN protect Claude agents from prompt injection wallet drain?",
    walletAddress: "DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk"
  });
  console.log("Inference Result:", JSON.stringify(inferTest, null, 2));
}

test().catch(console.error);
