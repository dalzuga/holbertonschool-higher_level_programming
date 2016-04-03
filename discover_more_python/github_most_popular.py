import requests

request_headers = {'User-Agent': 'Holberton_School', 'Authorization': 'token 95fd848656afb3a7d20af06365375c2a6f0b2fa8'}

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
response = requests.get(url)

print response
