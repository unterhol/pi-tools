var http = require('http');
var express = require('express');

var app = express();

app.use(express['static'](__dirname));

// Express route
app.get('inputs/:id', function(req, res) {
    res.status(200).send("hello")
});

// Express route unknown handler
app.get('*', function(req, res) {
    res.status(404).send("Oops, route not found")
});

app.use(function(err, req, res, next){
    if (req.xhr) {
        res.status(500).send('Oops, 500 error)');
    }
    else {
        next(err);
    }
});