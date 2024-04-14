#!/usr/bin/node
const args = require('process').argv;

let max;

if (args.length > 3) {
  let tmp;
  max = 2;
  for (let i = 3; i < args.length; i++) {
    tmp = i;
    if (parseInt(args[max]) < parseInt(args[tmp])) {
      max = tmp;
    }
  }

  args.splice(max, 1);

  max = parseInt(args[2]);
  for (let i = 3; i < args.length; i++) {
    tmp = parseInt(args[i]);
    if (max < tmp) {
      max = tmp;
    }
  }
} else {
  max = 0;
}

console.log(max);
