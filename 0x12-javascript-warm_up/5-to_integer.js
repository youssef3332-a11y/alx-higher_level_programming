#!/usr/bin/node
const args = process.argv.slice(2);
const a = parseInt(args[0]) || 'Not a number';
console.log(`My number: ${a}`);
