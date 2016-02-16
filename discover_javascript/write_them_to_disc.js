var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 6e73c90fdfe07bca58b4c3e20eaa15e367169857'
    }
};

var fs = require('fs');

function writeToFile(s)
{
    fs.writeFile("/tmp/49", s, function(err) {
	if(err) {
	    return console.log(err);
	}

	console.log("The file was saved!");
    });
}

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
			    streamToString(res, function(jsonString)
					   {
					       console.log(typeof jsonString);
					       console.log(jsonString);
					       writeToFile(jsonString);
					   }
					  );
			}

		       ); 
req.end();
