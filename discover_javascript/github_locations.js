var https = require('https');
var l=0;
var finalJson= [];
var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 6e73c90fdfe07bca58b4c3e20eaa15e367169857'
    }
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

function writeit(){
   
    var fs = require('fs');
    fs.writeFile("/tmp/49", JSON.stringify(finalJson), function(err) {
	    if(err) {
		return console.log(err);
	    }
	    console.log("The file was saved!");
	});
}

function log(callback){
    if (l==30){
	callback();
    }
}

function repeat(){
    for(k=0;k<30;k++){
	daniel();
    }
}

function daniel(){
    var urlto=jsonParse.items[k].owner.url.toString().replace("https://api.github.com", "");
    var fname=jsonParse.items[k].full_name;
    
    var urloptions = {
	hostname: 'api.github.com',
	path: urlto,
	headers: {
	    'User-Agent': 'Holberton_School',
	    'Authorization': 'token 6e73c90fdfe07bca58b4c3e20eaa15e367169857'
	}
    
    }

    var req2 = https.request(urloptions, function(res) {
	    streamToString(res, function(jsonString){
		jsonParse2=JSON.parse(jsonString);

		finalJson[l]={
		    full_name: fname,
		    location: jsonParse2.location
		};
		    l++;
		    log(writeit);
	    });
	});
    req2.end();
}


var req = https.request(options, function(res) {
	streamToString(res, function(jsonString){
		jsonParse=JSON.parse(jsonString);
		jsonParse.items.map(function(o, i){
			url=[jsonParse.items[i].url].join();
			fullname=[jsonParse.items[i].full_name].join();
		    },repeat());
	    });
    });

req.end()
