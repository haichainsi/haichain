# -*- coding: utf-8 -*-
import os, sys

files = ['_worker.js', 'app/_worker.js', 'functions/api/mcp.js', 'functions/api/mcp/[[path]].js']
target = "pathname === '/'"
for path in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for i, l in enumerate(f):
                if target in l:
                    print(f'{path}:{i+1}: {l.strip()}')
