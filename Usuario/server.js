const http = require('http');
const port = process.env.PORT || 5173;
const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    return res.end('ok');
  }
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Usuario running');
});
server.listen(port, () => console.log(`Usuario listening on ${port}`));
