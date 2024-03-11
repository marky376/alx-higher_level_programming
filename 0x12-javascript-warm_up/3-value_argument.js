#!/usr/bin/node

const argCount = process.argv[2];

if (!argCount)
{
	console.log('No arguments');
}
else
{
	console.log(argCount);
}
