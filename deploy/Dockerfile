# ==============================================================================
# HAIChain Production Dockerfile (Node.js 20 LTS Alpine)
# ==============================================================================
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependency manifests
COPY package*.json ./
COPY packages/agent-pay/package*.json ./packages/agent-pay/
COPY mcp-server/package*.json ./mcp-server/

# Install dependencies and build TypeScript packages
RUN npm ci --workspace=packages/agent-pay --workspace=mcp-server
COPY . .
RUN npm run build --prefix packages/agent-pay
RUN npm run build --prefix mcp-server

# Production Runner Stage
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV PORT=8080
ENV SOLANA_CLUSTER=devnet

COPY --from=builder /app ./

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://127.0.0.1:8080/status || exit 1

CMD ["node", "server/production-agent-relayer.js"]
