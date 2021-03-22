#!/usr/bin/node
/*
script that prints a square
*/
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let n = 0; n < x; n++) {
    console.log('x'.repeat(x));
  }
}
