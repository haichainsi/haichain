// Test script to execute renderTerminalContent in Node.js
import fs from 'fs';

// Mock browser environment
const localStorageData = {
  'haichain-connected-wallet': JSON.stringify({ address: 'CsFDqYvXWhaichainTestRefWallet123456789' }),
  'haichain-lang': 'vi',
  'haichain_referral_clicks': JSON.stringify([
    {
      ref: 'CsFDqYvXWhaichainTestRefWallet123456789',
      source: 'X (Twitter)',
      device: 'Mobile',
      isUnique: true,
      timestamp: Date.now() - 3600000
    },
    {
      ref: 'CsFDqYvXWhaichainTestRefWallet123456789',
      source: 'Telegram',
      device: 'Desktop',
      isUnique: true,
      timestamp: Date.now() - 1800000
    },
    {
      ref: 'CsFDqYvXWhaichainTestRefWallet123456789',
      source: 'X (Twitter)',
      device: 'Mobile',
      isUnique: false,
      timestamp: Date.now() - 600000
    }
  ]),
  'haichain_referral_ledger': JSON.stringify([
    {
      referrer: 'CsFDqYvXWhaichainTestRefWallet123456789',
      buyer: 'Buyer1111111111111111111111111111111111111',
      amountUsdt: 1000,
      commissionHai: 8571,
      timestamp: Date.now() - 86400000
    }
  ])
};

global.window = {
  location: { origin: 'https://haichain.si', pathname: '/', search: '' },
  localStorage: {
    getItem: (k) => localStorageData[k] || null,
    setItem: (k, v) => { localStorageData[k] = v; },
    removeItem: (k) => { delete localStorageData[k]; }
  },
  sessionStorage: {
    getItem: () => null,
    setItem: () => {}
  },
  addEventListener: () => {},
  dispatchEvent: () => {}
};
global.localStorage = global.window.localStorage;
global.sessionStorage = global.window.sessionStorage;
global.document = {
  getElementById: () => null,
  querySelector: () => null,
  querySelectorAll: () => [],
  addEventListener: () => {}
};
// navigator is read-only in Node 22

console.log('Testing sale-controller logic imports...');
const code = fs.readFileSync('sale-controller.js', 'utf-8');

// Run within safe scope
try {
  eval(code);
  console.log('sale-controller.js evaluated successfully without any runtime error!');
} catch (e) {
  console.error('Evaluation error:', e);
}
