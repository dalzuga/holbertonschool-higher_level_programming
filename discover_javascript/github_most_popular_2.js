var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 6e73c90fdfe07bca58b4c3e20eaa15e367169857'
    }
};

var f = function(jsonString) {
    console.log(typeof jsonString);
    console.log(jsonString)};

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}

var req = https.request(options, function(res)
			{
			    streamToString(res, f); 
			}
		       );
req.end();
