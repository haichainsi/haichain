const fs = require('fs');

function inspect() {
  const html = fs.readFileSync('dashboard.html', 'utf8');
  const mcpIdx = html.indexOf('id="tab-mcp"');
  const docsIdx = html.indexOf('id="tab-docs"');
  console.log('mcpIdx:', mcpIdx, 'docsIdx:', docsIdx);

  // find end of section tab-mcp
  const mcpEnd = html.indexOf('</section>', mcpIdx);
  const mcpSection = html.slice(mcpIdx - 20, mcpEnd + 10);
  console.log('MCP Section length:', mcpSection.length);

  const docsEnd = html.indexOf('</section>', docsIdx);
  const docsSection = html.slice(docsIdx - 20, docsEnd + 10);
  console.log('Docs Section length:', docsSection.length);

  fs.writeFileSync('scripts/mcp_section_dump.html', mcpSection);
  fs.writeFileSync('scripts/docs_section_dump.html', docsSection);
}

inspect();
