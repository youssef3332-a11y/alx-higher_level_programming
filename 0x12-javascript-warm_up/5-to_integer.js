#!/usr/bin/node
const args = process.argv.slice(2);
const a = parseInt(args[0]);
let result = 'Not number';
if (!isNaN(a)) {
  result = a;
}
console.log(`My number: ${result}`);
