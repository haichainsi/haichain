import http from 'http';
import { handleMcpRequest } from './cloud-mcp-functions/_mcp_handler.js';

const PORT = 3600;

process.on('uncaughtException', (err) => {
  console.error('[Daemon] Uncaught Exception:', err);
});

process.on('unhandledRejection', (reason) => {
  console.error('[Daemon] Unhandled Rejection:', reason);
});

const server = http.createServer(async (req, res) => {
  try {
    const url = 'http://' + (req.headers.host || '127.0.0.1:3600') + req.url;

    // Collect request body for POST
    let body = [];
    for await (const chunk of req) {
      body.push(chunk);
    }
    const bodyBuffer = Buffer.concat(body);

    const headers = new Headers();
    for (const [key, value] of Object.entries(req.headers)) {
      if (value) {
        if (Array.isArray(value)) {
          value.forEach(v => headers.append(key, v));
        } else {
          headers.set(key, value);
        }
      }
    }

    const init = {
      method: req.method,
      headers: headers
    };
    if (req.method !== 'GET' && req.method !== 'HEAD' && bodyBuffer.length > 0) {
      init.body = bodyBuffer;
    }

    const standardReq = new Request(url, init);
    const standardRes = await handleMcpRequest(standardReq);

    // Send status
    res.statusCode = standardRes.status;

    // Send headers
    standardRes.headers.forEach((val, key) => {
      res.setHeader(key, val);
    });

    // Send body
    const arrayBuffer = await standardRes.arrayBuffer();
    res.end(Buffer.from(arrayBuffer));
  } catch (err) {
    console.error('Server error:', err);
    res.statusCode = 500;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ error: err.message }));
  }
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.warn(`[Daemon] Port ${PORT} already in use, skipping local bind.`);
  } else {
    console.error('[Daemon] Server error:', err);
  }
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`HAICHAIN Cloud MCP Gateway listening on http://127.0.0.1:${PORT}`);
});
