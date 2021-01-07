var http = require('http');
var express = require('express');
var wpi = require('pi-gpio');

var app = express();

var inputs = [{ pin: '16', gpio: '23', value: null }, { pin: '22', gpio: '25', value: null }];

var i;
for (i in inputs) {
    console.log('opening GPIO port ' + inputs[i].gpio + ' on pin ' + inputs[i].pin + ' as input');
    gpio.open(inputs[i].pin, "input", function (err) {
        if (err) {
            throw err;
        }
    });
}

// setInterval( function () {
//     // read GPIO input port
//     gpio.read(inputs[0].pin, function (err, value) {
//     if (err) {
//     throw err;
//     }
//     console.log('read pin ' + inputs[0].pin + ' value = ' + value);
//     // update the inputs object
//     inputs[0].value = value.toString(); // store value as a string
//     });
// }

app.use(express['static'](__dirname));

// Express route for incoming requests for a customer name
app.get('/inputs/:id', function(req, res) {
    res.status(200).send(inputs[req.params.id]);
});
    
// Express route for any other unrecognised incoming requests
app.get('*', function(req, res) {
    res.status(404).send('Unrecognised API call');
});
    
// Express route to handle errors
app.use(function(err, req, res, next) {
    if (req.xhr) {
    res.status(500).send('Oops, Something went wrong!');
    } else {
    next(err);
    }
});

app.listen(3000);
console.log('App Server running at port 3000');

