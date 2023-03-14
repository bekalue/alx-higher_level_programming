#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
