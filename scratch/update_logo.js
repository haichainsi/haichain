const fs = require('fs');

function updateLogoInFiles() {
  const brandAnchorTarget = `      <!-- Brand Logo: Pure Official Logo (Harmonious Mobile & Desktop) -->\n      <a href=\"/\" class=\"flex items-center group py-1\">\n        <img src=\"/assets/haichain-official-logo.png?v=geom2026_v4\" alt=\"HAICHAIN\" class=\"h-7 sm:h-8 md:h-8.5 w-auto object-contain filter invert-0 dark:invert transition-transform duration-200 group-hover:scale-[1.02]\" style=\"max-height: 32px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo.png?v=geom2026_v4';}\">\n      </a>`;

  const brandAnchorReplacement = `      <!-- Brand Logo: Emblem + Official Wordmark (100% Visible in Both Light & Dark Modes) -->\n      <a href=\"/\" class=\"flex items-center space-x-2.5 sm:space-x-3 group py-1\">\n        <img src=\"/assets/haisi-icon.png\" alt=\"HAICHAIN Emblem\" class=\"w-7 h-7 sm:w-8 sm:h-8 rounded-lg object-contain shrink-0 shadow-sm transition-transform duration-200 group-hover:scale-105\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}\">\n        <!-- Light Mode: Dark Logo -->\n        <img src=\"/assets/haichain-official-logo.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"dark:hidden h-6 sm:h-7 md:h-7.5 w-auto object-contain transition-transform duration-200 group-hover:scale-[1.01]\" style=\"max-height: 30px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo.png?v=geom2026_v5';}\">\n        <!-- Dark Mode: Pure White Logo -->\n        <img src=\"/assets/haichain-official-logo-white.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"hidden dark:block h-6 sm:h-7 md:h-7.5 w-auto object-contain transition-transform duration-200 group-hover:scale-[1.01]\" style=\"max-height: 30px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo-white.png?v=geom2026_v5';}\">\n      </a>`;

  ['app/index.html', 'index.html'].forEach(p => {
    let html = fs.readFileSync(p, 'utf8');
    // Replace header logo
    if (html.includes(brandAnchorTarget)) {
      html = html.replace(brandAnchorTarget, brandAnchorReplacement);
    } else {
      // Regex replace if whitespace differed
      html = html.replace(
        /<a href=\"\/\" class=\"flex items-center group py-1\">[\s\S]*?<\/a>/,
        brandAnchorReplacement.trim()
      );
    }
    
    // Replace footer logo
    html = html.replace(
      /<img src=\"\/assets\/haichain-official-logo\.png\?v=geom2026_v4\" alt=\"HAICHAIN\" class=\"h-5 sm:h-\[22px\][^>]*>/,
      `<img src=\"/assets/haisi-icon.png\" alt=\"HAICHAIN Emblem\" class=\"w-5 h-5 rounded object-contain shrink-0\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}\">\n        <img src=\"/assets/haichain-official-logo.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"dark:hidden h-4 sm:h-[18px] w-auto object-contain opacity-95\" style=\"max-height: 18px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo.png?v=geom2026_v5';}\">\n        <img src=\"/assets/haichain-official-logo-white.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"hidden dark:block h-4 sm:h-[18px] w-auto object-contain opacity-95\" style=\"max-height: 18px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo-white.png?v=geom2026_v5';}\">`
    );

    fs.writeFileSync(p, html, 'utf8');
    console.log('Updated logo in:', p);
  });

  // Update dashboard.html
  ['app/dashboard.html', 'dashboard.html'].forEach(p => {
    let html = fs.readFileSync(p, 'utf8');
    
    // Sidebar logo in dashboard
    html = html.replace(
      /<a href=\"\/\" class=\"flex items-center space-x-2 pb-6 border-b border-brand-lightBorder dark:border-brand-border group\">[\s\S]*?<\/a>/,
      `<a href=\"/\" class=\"flex items-center space-x-2.5 pb-6 border-b border-brand-lightBorder dark:border-brand-border group\">\n        <img src=\"/assets/haisi-icon.png\" alt=\"HAICHAIN Emblem\" class=\"w-7 h-7 rounded-lg object-contain shrink-0 shadow-sm transition-transform group-hover:scale-105\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}\">\n        <img src=\"/assets/haichain-official-logo.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"dark:hidden w-auto object-contain transition-transform group-hover:scale-[1.02]\" style=\"height: 22px; width: auto; max-height: 24px; max-width: 150px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo.png?v=geom2026_v5';}\">\n        <img src=\"/assets/haichain-official-logo-white.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"hidden dark:block w-auto object-contain transition-transform group-hover:scale-[1.02]\" style=\"height: 22px; width: auto; max-height: 24px; max-width: 150px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo-white.png?v=geom2026_v5';}\">\n      </a>`
    );

    // Mobile header logo in dashboard
    html = html.replace(
      /<a href=\"\/\" class=\"flex items-center space-x-2 group shrink-0\">[\s\S]*?<\/a>/,
      `<a href=\"/\" class=\"flex items-center space-x-2 group shrink-0\">\n          <img src=\"/assets/haisi-icon.png\" alt=\"HAICHAIN Emblem\" class=\"w-6 h-6 rounded-md object-contain shrink-0 shadow-sm\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}\">\n          <img src=\"/assets/haichain-official-logo.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"dark:hidden object-contain transition-transform group-hover:scale-[1.02] shrink-0\" style=\"height: 22px; width: auto; max-height: 24px; max-width: 140px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo.png?v=geom2026_v5';}\">\n          <img src=\"/assets/haichain-official-logo-white.png?v=geom2026_v5\" alt=\"HAICHAIN\" class=\"hidden dark:block object-contain transition-transform group-hover:scale-[1.02] shrink-0\" style=\"height: 22px; width: auto; max-height: 24px; max-width: 140px; display: block;\" onerror=\"if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haichain-official-logo-white.png?v=geom2026_v5';}\">\n        </a>`
    );

    fs.writeFileSync(p, html, 'utf8');
    console.log('Updated logo in:', p);
  });
}

updateLogoInFiles();
