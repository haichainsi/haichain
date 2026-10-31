const http = require('http');

function testStreamingOpenAI() {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      model: 'gpt-4o',
      stream: true,
      messages: [{ role: 'user', content: 'Say hello in 3 words' }]
    });

    const req = http.request({
      hostname: 'localhost',
      port: 3000,
      path: '/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer agent_cursor_ide_02',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, (res) => {
      let chunksCount = 0;
      let fullContent = '';
      res.on('data', chunk => {
        chunksCount++;
        const str = chunk.toString();
        const lines = str.split('\n');
        for (const line of lines) {
          if (line.startsWith('data: ') && line !== 'data: [DONE]') {
            try {
              const parsed = JSON.parse(line.slice(6));
              fullContent += (parsed.choices[0]?.delta?.content || '');
            } catch(e) {}
          }
        }
      });
      res.on('end', () => {
        resolve({
          status: res.statusCode,
          chunksCount,
          fullContent: fullContent.trim(),
          txSig: res.headers['x-haichain-tx-sig'],
          margin: res.headers['x-haichain-treasury-margin-usdt']
        });
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function testStreamingAnthropic() {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      model: 'claude-3-5-sonnet-20241022',
      stream: true,
      messages: [{ role: 'user', content: 'Say hi to HAICHAIN' }]
    });

    const req = http.request({
      hostname: 'localhost',
      port: 3000,
      path: '/v1/messages',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': 'agent_claude_desktop_01',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, (res) => {
      let chunksCount = 0;
      let fullContent = '';
      res.on('data', chunk => {
        chunksCount++;
        const str = chunk.toString();
        const lines = str.split('\n');
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const parsed = JSON.parse(line.slice(6));
              if (parsed.type === 'content_block_delta') {
                fullContent += (parsed.delta?.text || '');
              }
            } catch(e) {}
          }
        }
      });
      res.on('end', () => {
        resolve({
          status: res.statusCode,
          chunksCount,
          fullContent: fullContent.trim(),
          txSig: res.headers['x-haichain-tx-sig'],
          margin: res.headers['x-haichain-treasury-margin-usdt']
        });
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function main() {
  console.log('Testing OpenAI Streaming...');
  const oaiStream = await testStreamingOpenAI();
  console.log('OpenAI Stream Status:', oaiStream.status, 'Chunks:', oaiStream.chunksCount, 'TxSig:', oaiStream.txSig);

  console.log('\nTesting Anthropic Streaming...');
  const antStream = await testStreamingAnthropic();
  console.log('Anthropic Stream Status:', antStream.status, 'Chunks:', antStream.chunksCount, 'TxSig:', antStream.txSig);
}

main().catch(console.error);
