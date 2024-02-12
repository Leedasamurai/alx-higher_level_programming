#!/usr/bin/node

'use strict';

const size = process.argv[2];

if (!isNaN(size) && size !== undefined && parseInt(size) > 0) {
    for (let i = 0; i < parseInt(size); i++) {
        console.log('X'.repeat(parseInt(size)));
    }
} else {
    console.log("Missing size");
}
