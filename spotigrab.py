#!/usr/bin/python
import dbus
import os
import time
import sys
import subprocess
import glob

def numberdestroyer(string):
	string = string.translate(None,"1234567890")
	return string

def customformat(nonformattedfile):
	nonformattedfile = nonformattedfile.replace(" ", "_")
	nonformattedfile = nonformattedfile.replace("/", "1")
	nonformattedfile = nonformattedfile + ".mp3"
	formatedfile = nonformattedfile
	return formatedfile
#grabs the artist and title of the current spotify song your listening
def spotifyinfograbber():
	session_bus = dbus.SessionBus()
	spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
	spotify_properties = dbus.Interface(spotify_bus,"org.freedesktop.DBus.Properties")
	metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
	artist = metadata['xesam:artist']
	for info in artist:
		artist = info
	title = metadata['xesam:title']
	info = ("%s, %s"%(title,artist))
	return info
#similar to the "touch" bash command
def touch(name):
    with open(path, 'a'):
        os.utime(path, None)

#Looks for an mp3files directory if not found it makes on,it also checks for songs so you dont record the same song over and over again.
def filechecker():
	try:
		os.listdir("mp3files")
	except OSError:
		os.makedirs("mp3files")
	print(":)")
	directory = os.listdir("mp3files")
	if len(directory) == 0:
		with open(os.path.join("mp3files", "starterfile"),"wb") as starterfile:
			pass
	elif len(directory) >= 2:
		try:
			os.remove("/home/eric/Desktop/spotigrab/mp3files/starterfile")
		except OSError:
			pass
	info = spotifyinfograbber()
	outformat = info.replace(" ", "_")
	outformat = outformat.replace("/", "1")
	outformat = outformat.replace("'",",")
	outformat = outformat.replace('"',',')
	outformat = outformat + ".mp3"
	num1 = 0
	scanlimit = len(directory)
	scanlimit = int(scanlimit) 
	for song in directory:
		if song == outformat:
			record = False
			break
		else:
			record = True
	if record == True:
		return "RECORD"
	else:
		return "RECORDFALSE"
		
#starts ffmpeg
def record(songinfo):
	songinfo = songinfo.replace(" ", "_")
	songinfo = songinfo.replace("/","1")
	songinfo = songinfo.replace("'",",")
	songinfo = songinfo.replace('"',',')
	print songinfo
	songinfo = songinfo + ".mp3"
	rec = subprocess.Popen(["ffmpeg", "-f", "pulse", "-i", "default", songinfo])
	return rec

#puts everything together and restarts the program when finished :)
def main():
	while True:
		info = spotifyinfograbber()
		checkfiles = filechecker()
		if checkfiles == "RECORD":
			while True:
				if info == spotifyinfograbber():
					try:
						if rec:
							pass
					except NameError:
						rec = record(info)
				else:
					rec.kill()
					mp3files = glob.glob("*mp3")
					for mp3file in mp3files:
						os.system("mv %s mp3files/" %mp3file)
						try:
							os.remove(mp3file)
						except OSError:
							pass
						
						
					
					os.system("./spotigrab.py")
		else:
			print "Song already exists in mp3files directory please listen to it or skip"
			while True:
				if info == spotifyinfograbber():
					pass
				else:
					os.system("./spotigrab.py")

main()
