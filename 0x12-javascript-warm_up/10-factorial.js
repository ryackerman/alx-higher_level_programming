#!/usr/bin/node
function factorial(f) {
	if (f < 0) {
		return (-1);
	}
	if (f === 0 || isNaN(f)) {
		return (1);
	}
	return (f * factorial(f - 1));
}

console.log(factorial(Number(process.argv[2])));
