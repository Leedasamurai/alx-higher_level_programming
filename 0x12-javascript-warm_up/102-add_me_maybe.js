#!/usr/bin/node

'use strict';

function addMeMaybe(number, theFunction) {
  theFunction(number + 1);
}

module.exports = { addMeMaybe };

