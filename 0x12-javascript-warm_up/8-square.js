#!/usr/bin/node
/*
script that prints a square
*/
'use strict';
let x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
