const http = require('http');
const express = require('express');
const routes = require('./routes').router;

var app = express();

app.use(routes);

var server = http.Server(app);
server.listen(process.env.PORT || 3000);