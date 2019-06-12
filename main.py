import mutagen
import requests
import pprint
import os
import api_keys as ak
import json
data = mutagen.File('song.flac')
data['title'] = 'New Title'
data.save()

# Get Album name and stuff

artist = input('Enter artist: ') or 'Radiohead'
album = input('Enter Album: ') or 'Amnesiac'
pp = pprint.PrettyPrinter(4)

API_key = ak.API_key

url = " http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=" + API_key + "&artist="+artist+"&album=" + album + "&format=json"

r = requests.get(url)
r = json.loads(r.text)

for i in r['album']['tracks']['track']:
	data = mutagen.File('./Song/' + os.listdir('./Songs/')[int(i['@attr']['rank'])- 1] )
	# os.rename(''./2001 - Amnesiac/' + os.listdir('./2001 - Amnesiac')[int(i['@attr']['rank'])- 1]', i['name'])
	data['title'] = i['name']
	data['album'] = r['album']['name']
	data['tracknumber'] = i['@attr']['rank']
	data['album artist'] = r['album']['artist']
	data['artist'] = r['album']['artist']
	data.save()




