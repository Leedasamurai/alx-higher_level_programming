#!/usr/bin/node

'use strict';

const myObject = {
  type: 'object',
  value: 12,
  incr: function() {
    this.value++;
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

