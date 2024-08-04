#!/usr/bin/node
const times = process.argv.slice(2);
const num = parseInt(times[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
