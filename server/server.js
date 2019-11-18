const http = require('http');
const callSendAPI = require('./messenger_api');

const server = http.createServer((req, res) => {
    res.end('This is my server response!');
});
console.log("labite on port ",process.env.PORT)
callSendAPI('1907097259403451', 'la bite');
server.listen(process.env.PORT || 3000);


