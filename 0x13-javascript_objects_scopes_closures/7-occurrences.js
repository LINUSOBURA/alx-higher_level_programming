#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (element in list) {
    if (list[element] == searchElement) {
      count += 1;
    }
  }

  return count;
};
