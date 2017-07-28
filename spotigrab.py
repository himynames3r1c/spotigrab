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
	outformat = info.replace(" ", "_")
	outformat = outformat.replace("/", "1")
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
		

def record(songinfo):
	songinfo = songinfo.replace(" ", "_")
	songinfo = songinfo.replace("/","1") #AC/DC SHOWED ME THIS
	songinfo = songinfo + ".mp3"
	rec = subprocess.Popen(["ffmpeg", "-f", "pulse", "-i", "default", songinfo])
	return rec

#Ask if spotfiy is running
def main():
	while True:
		choice = raw_input("Is spotify running (Y/N) :")
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
