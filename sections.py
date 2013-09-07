#!/usr/bin/python
from pyechonest import config
config.ECHO_NEST_API_KEY="IDN0GVG31XJR8WLCM"
from pyechonest import artist
from pyechonest import track
import json
import urllib2
import pygame





def getSimilarArtists(artistString):
    similar_artist_list=[]
    try:
        artistObject= artist.Artist(urllib.unquote(artistString).decode('utf8'))
        for similar_artist in artistObject.similar: 
            similar_artist_list.append(similar_artist.name)
        jsonOutput=json.dumps(similar_artist_list)
        return jsonOutput
    except:
        similar_artist_list.append('No Similar Artists Found')
        jsonOutput=json.dumps(similar_artist_list)
        return jsonOutput

def getArtistImage(artistString):
    try:
        artistObject= artist.Artist(urllib.unquote(artistString).decode('utf8'))
        images=artistObject.get_images()
        l=len(images)
        k=random.randint(0,l-1)
        return images[k]['url']
    except:
       return 'http://images.wikia.com/theslenderman/images/c/ce/Question-mark-face.jpg'


def getArtistBio(artistString):
    artistObject= artist.Artist(urllib.unquote(artistString).decode('utf8'))
    bios=artistObject.get_biographies()
    return bios[0]['text'].encode('ascii','ignore')

#print getSimilarArtists('skrillex')
mp3='Bassnectar.mp3'
pytrack = track.track_from_filename(mp3)
response=urllib2.urlopen(pytrack.analysis_url)
jsonOutput=json.loads(response.read())
for i in range(len(jsonOutput['sections'])):
    print jsonOutput['sections'][i]
    print ""
#print urllib2.get_data()
#print jsonOutput
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.load(mp3)
pygame.mixer.music.play()

