#!/usr/bin/node

function secondBiggest (args) {
  const nums = args.map(Number).sort((a, b) => b - a);
  return nums[1] || 0;
}

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  console.log(secondBiggest(args));
}
