import { handleMcpRequest } from '../_mcp_handler.js';

export async function onRequest(context) {
  return await handleMcpRequest(context.request);
}
