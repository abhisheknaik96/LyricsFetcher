
import urllib, urllib2, requests, re
from subprocess import CalledProcessError, check_output
from bs4 import BeautifulSoup
import json as m_json

PATH = "/home/abhisheknaik96/Music/Lyrics/"

def getURL(query):

	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json = m_json.loads ( response )
	results = json [ 'responseData' ] [ 'results' ]
	url=""

	for result in results:
	    if result['url'].find('azlyrics')>0 :
	    	url = result['url']   # was URL in the original and that threw a name error exception
	    	break;
	if url!="":
		print url
		return url
	else:
		print "URL from azlyrics.com not found."

def parse(url):

	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	text = soup.get_text()

	result = re.findall(r'Print[\n]+(.*) Submit', text, re.DOTALL|re.IGNORECASE)

	if len(result)>0 :
		lyrics = result[0]
		lyrics = lyrics.encode('ascii', 'ignore').decode('ascii')

		return lyrics
	else:
		return -1

def download(songName):

	# query = raw_input ( 'Query: ' )
	# query = "my songs know what you did in the dark lyrics"
	url = getURL(songName + ' lyrics')
	result = parse(url)

	if result==-1:
		return -1
	else:
		return result

def display(fileName):

	try:
	    output = check_output(["ls", PATH])
	    start = output.find(fileName)
	    end = output.find('.txt', start) + 4
	    # print output[start:end] + "<"
	    output = check_output(["sublime", PATH+output[start:end]])
	    returncode = 0
	except CalledProcessError as e:
	    output = e.output
	    returncode = e.returncode
	    print "Downloaded Lyrics not found..."
	else:
		print "Done"

	# print(returncode)

def save(songName, lyrics):

	fp = open(PATH + songName + '.txt', 'w')
	fp.write(lyrics)
	fp.close()

def downloadAndDisplay(songName):

	print "\nDownloading lyrics for " + songName + "\n"
	result = download(songName)
	
	if result==-1:
		print "\nLyrics not found...\n"	
	else:
		save(songName, result)
		print "\nDownloaded and saved.\n\nDisplaying...\n"
		display(songName)

def downloaded(songName):

	output = check_output(["ls", PATH])
	start = output.find(songName)
	if start<0:
		return False
	else:
		return True


output = check_output('lsof -F n -c rhythmbox | grep Music | cut -c 29-', shell=True)
print output 

fileName = re.findall(r'.*.mp3', output)
if fileName==-1:
	print "No song playing currently."
	quit()

songName = fileName[0][:-4] 			# Assuming 1st one is the current song.
print songName

if downloaded(songName)==True :
	print "Lyrics already present.\nOpening...\n\n"
	display(songName)
else :
	downloadAndDisplay(songName)


######################################################################
#	0. Find out current song using bash.
#	1. Check if song present or not, using bash.
#	2. If not, download and save.
#	3. Open in sublime.
######################################################################



