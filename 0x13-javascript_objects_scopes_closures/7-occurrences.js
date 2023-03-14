#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(member => {
    if (member === searchElement) {
      count++;
    }
  });
  return count;
};
