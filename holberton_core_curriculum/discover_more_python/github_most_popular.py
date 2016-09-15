import urllib2

request_headers = {'User-Agent': 'Holberton_School', 'Authorization': 'token 95fd848656afb3a7d20af06365375c2a6f0b2fa8'}

githuburl = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
req = urllib2.Request(githuburl, headers=request_headers)
response = urllib2.urlopen(req)

print response.read()
