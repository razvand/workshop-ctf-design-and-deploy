const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
    const queryObject = url.parse(req.url, true).query;

    res.writeHead(200, {'Content-Type': 'text/html'});
    
    res.write('<h1>Calculator Service</h1>');
    res.write('<p>Enter a calculation:</p>');
    res.write('<form method="GET">');
    res.write('Calculation: <input type="text" name="calc" placeholder="1+1">');
    res.write('<input type="submit" value="Calculate">');
    res.write('</form>');

    if (queryObject.calc) {
        try {
            // VULNERABILITY: Using eval() on user input
            const result = eval(queryObject.calc);
            res.write('<h2>Result: ' + result + '</h2>');
        } catch (e) {
            res.write('<h2>Error: ' + e.message + '</h2>');
        }
    }

    res.end();
});

server.listen(3000, () => {
    console.log('Server running on port 3000');
});
