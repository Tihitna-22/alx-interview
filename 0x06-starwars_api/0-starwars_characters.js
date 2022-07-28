#!/usr/bin/node

const request = require('request');

const id = process.argv[2] + '/';
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + id, async function (err, res, body) {
    if (err) return console.error(err);

    const list_url = JSON.parse(body).characters;


    for (const li of list_url) {
        await new Promise(function (resolve, reject) {
            request(li, function (err, res, body) {
                if (err) return console.error(err);

              ]
                console.log(JSON.parse(body).name);
                resolve();
            });
        });
    }
});
