import urllib
mp3file = urllib.urlopen("http://www.subflow.net/Radio/ambient/001-01-Blame_it_on_the_Rain.mp3")
output = open('test.mp3','wb')
output.write(mp3file.read())
output.close()