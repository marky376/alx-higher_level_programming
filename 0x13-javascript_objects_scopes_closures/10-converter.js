#!/usr/bin/node
// 10-converter.js
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
