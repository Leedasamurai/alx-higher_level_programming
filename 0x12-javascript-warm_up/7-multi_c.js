#!/usr/bin/node

'use strict';

const arg = process.argv[2];

if (!isNaN(arg) && arg !== undefined && parseInt(arg) > 0) {
    for (let i = 0; i < parseInt(arg); i++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}
