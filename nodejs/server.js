const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    uptime=os.uptime();
    utmin=uptime/60;
    uthour=utmin/60;
    utday=uthour/24;
    uptime = Math.floor(uptime);
    utmin = Math.floor(utmin);
    uthour = Math.floor(uthour)
    utday = Math.floor(utday)
    utday = utday%24
    uthour = uthour%60
    utmin = utmin%60
    uptime = uptime%60
    tmemory=os.totalmem();
    tmemmb=tmemory/2048
    cpu=os.cpus().length;
    fmemory=os.freemem();
    fmemmb=fmemory/2048
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${utday} Days ${uthour} Hours ${utmin} Minutes ${uptime} Seconds</p>
        <p>Total Memory: ${tmemmb} MB</p>
        <p>Free Memory: ${fmemmb} MB</p>
        <p>Number of CPUs: ${cpu}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");