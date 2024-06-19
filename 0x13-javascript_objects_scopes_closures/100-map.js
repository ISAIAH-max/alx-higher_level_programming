#!/usr/bin/node

// Import the list from the file
const { list } = require('./100-data');

// Print the original list
console.log(list);

// Create a new list with each value multiplied by its index
const newList = list.map((value, index) => value * index);

//Print the new list
console.log(newList);
