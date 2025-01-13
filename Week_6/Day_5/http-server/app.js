const http = require('http');
const port = 5001

const server = http.createServer((request, response) => {
    // console.log(request)
    console.log(request.url)
    console.log(request.method)
    console.log(request.header)
    response.end('Hello from my server')
});

server.listen(port, () => {
    console.log(`Run on port ${port}`)
});