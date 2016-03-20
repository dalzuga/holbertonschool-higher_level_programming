#!/usr/bin/ruby

require "net/http"
require "uri"

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 6e73c90fdfe07bca58b4c3e20eaa15e367169857'
}

uri = URI.parse("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc")

response = Net::HTTP.get(uri)

puts response

f = File.new("/tmp/49", "w+")
f.write(response)
