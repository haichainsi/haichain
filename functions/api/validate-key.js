/**
 * Cloudflare Pages Function: POST /api/validate-key
 * Validates Bring-Your-Own-Key (BYOK) for AI Providers
 */
export async function onRequestPost({ request }) {
  try {
    const { provider, apiKey } = await request.json();

    if (!apiKey || typeof apiKey !== 'string' || apiKey.trim().length < 8) {
      return new Response(JSON.stringify({ valid: false, error: "API Key must be at least 8 characters long." }), {
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    const trimmed = apiKey.trim();
    let valid = false;
    let error = null;

    if (provider === 'OpenAI') {
      valid = trimmed.startsWith('sk-');
      if (!valid) error = "OpenAI key must start with 'sk-'.";
    } else if (provider === 'Anthropic Claude') {
      valid = trimmed.startsWith('sk-ant-');
      if (!valid) error = "Anthropic key must start with 'sk-ant-'.";
    } else if (provider === 'DeepSeek') {
      valid = trimmed.startsWith('sk-');
      if (!valid) error = "DeepSeek key must start with 'sk-'.";
    } else {
      valid = true;
    }

    if (!valid) {
      return new Response(JSON.stringify({ valid: false, error }), {
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    const maskedKey = trimmed.length > 8 ? `${trimmed.slice(0, 4)}...${trimmed.slice(-4)}` : '****';

    return new Response(JSON.stringify({
      valid: true,
      provider,
      maskedKey
    }), {
      status: 200,
      headers: { "Content-Type": "application/json" }
    });
  } catch (err) {
    return new Response(JSON.stringify({ valid: false, error: err.message }), {
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
}
