#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  const incremented = number + 1;
  theFunction(incremented);
}

module.exports = { addMeMaybe };
