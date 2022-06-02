from urllib.request import urlopen
import json
json_url = urlopen("https://usbiomag.com/wp-json/wp/v2/posts/293")

data = json.loads(json_url.read())

print (data)