#!/usr/bin/node
const numofArg = process.argv.length - 2;
if (numofArg === 0) {
  console.log('No argument');
} else if (numofArg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
