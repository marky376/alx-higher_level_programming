#!/usr/bin/node
const { dict } = require('./101-data');

const userDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!userDict[occurrences]) {
    userDict[occurrences] = [];
  }
  userDict[occurrences].push(userId);
}

console.log(userDict);

