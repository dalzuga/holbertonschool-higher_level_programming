var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 6e73c90fdfe07bca58b4c3e20eaa15e367169857'
    }
};

var cb = function(s) {
    console.log(s);
}

var req = https.request(options, function(stream) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
});
req.end();
