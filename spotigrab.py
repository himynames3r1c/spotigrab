#!/usr/bin/python
import dbus
import os
import time
import sys
import subprocess

def numberdestroyer(string):
	string = string.translate(None,"1234567890")
	return string

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

def touch(name):
    with open(path, 'a'):
        os.utime(path, None)

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
	for song in directory:
		if info == song:
			return ("RECORDFALSE")
		else:
			return ("RECORD")

def record(songinfo):
	songinfo = songinfo.replace(" ", "_")
	songinfo = songinfo.replace("/","1") #AC/DC SHOWED ME THIS
	songinfo = songinfo + ".mp3"
	rec = subprocess.Popen(["ffmpeg", "-f", "pulse", "-i", "default", songinfo])
	return rec

#Ask if spotfiy is running
def main():
	while True:
		choice = "y"
		choice = choice.upper()
		if choice == "Y":
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
						#Move files to mp3files folder and remove _ in spaces and 1 is slashes
						os.system("./spotigrab.py")
			else:
				sys.exit()
			

main()
#maybe implement method to see if spotify is running
#perhaps make an api with web api
