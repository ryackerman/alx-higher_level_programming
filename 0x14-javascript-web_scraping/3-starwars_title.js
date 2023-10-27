#!/usr/bin/node
const request = require('request');
const movie = 'https://swapi-api.alx-tools.com/api/films/';

request(movie + process.argv[2], function (error, response, body) {
	if (error)
	{
		console.error(error);
	}
	else
	{
		const movieDt = JSON.parse(body);
		console.log(movieDt.title);
	}
});
