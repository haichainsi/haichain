// functions/api/validate-key.js
// Cloudflare Pages Function: API Key Syntax Validator for BYOK Connectors

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization",
    },
  });
}

export async function onRequestPost({ request }) {
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  try {
    const body = await request.json().catch(() => ({}));
    const { provider, apiKey } = body;

    if (!apiKey || typeof apiKey !== "string") {
      return new Response(
        JSON.stringify({ valid: false, error: "API Key cannot be empty." }),
        { status: 400, headers: corsHeaders }
      );
    }

    const trimmed = apiKey.trim();

    // Basic format validation
    if (provider === "openai" && !trimmed.startsWith("sk-")) {
      return new Response(
        JSON.stringify({ valid: false, error: "OpenAI API keys typically begin with 'sk-'." }),
        { status: 400, headers: corsHeaders }
      );
    }

    if (provider === "anthropic" && !trimmed.startsWith("sk-ant-")) {
      return new Response(
        JSON.stringify({ valid: false, error: "Anthropic API keys typically begin with 'sk-ant-'." }),
        { status: 400, headers: corsHeaders }
      );
    }

    if (provider === "perplexity" && !trimmed.startsWith("pplx-")) {
      return new Response(
        JSON.stringify({ valid: false, error: "Perplexity API keys typically begin with 'pplx-'." }),
        { status: 400, headers: corsHeaders }
      );
    }

    return new Response(
      JSON.stringify({
        valid: true,
        provider: provider,
        message: "API Key format verified successfully.",
      }),
      { status: 200, headers: corsHeaders }
    );
  } catch (err) {
    return new Response(
      JSON.stringify({ valid: false, error: err.message }),
      { status: 500, headers: corsHeaders }
    );
  }
}
