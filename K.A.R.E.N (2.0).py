import os
import cv2
import sys
import math
import time
import json
import emoji
import psutil
import serial
import ctypes
import shutil
import string
import qrcode
import random
import PyPDF2
import pygame
import turtle
import imghdr
import parser
import socket
import pyttsx3
import tkinter
import pyjokes
import smtplib
import winsound
import datetime
import operator
import requests
import platform
import requests
import winshell
import termcolor
import threading
import wikipedia
import speedtest
import pywhatkit
import bluetooth
import pyautogui
import freegames
import subprocess
import feedparser
import webbrowser
import wavio as wv
import numpy as np
import instaloader
import wolframalpha
import pygame as pg
from turtle import *
import tkinter as tk
from tkinter import *
import urllib.request
from enum import Enum
from time import sleep
import flappy_bird_gym
import face_recognition
from PIL import ImageTk
from tkinter import ttk
from PIL import ImageOps
import sounddevice as sd
from requests import get
from collections import*
from datetime import date
import tkinter.messagebox
from random import choice
from tkinter.ttk import *
from pytube import  YouTube
from tkinter import _tkinter
from random import randrange
from freegames import vector
from bs4 import BeautifulSoup
from collections import deque
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
from twilio.rest import Client
import speech_recognition as sr
import win32com.client as wincl
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from clint.textui import progress
from GoogleNews import GoogleNews
from urllib.request import urlopen
from collections import namedtuple
from scipy.io.wavfile import write
from freegames import floor, vector
from ecapture import ecapture as ec
from freegames import square, vector
from pynput.keyboard import Listener
from vidstream import StreamingServer
from geopy.geocoders import Nominatim
from vidstream import ScreenShareClient
from cvzone.SerialModule import SerialObject
from cvzone.HandTrackingModule import HandDetector
from PIL import Image,ImageFilter,ImageColor,ImageDraw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#############################################################################################################################################################
scannow = '/scannow'
assname = 'karen 2.0'
rdate = 2022
#############################################################################################################################################################
def handcontroller():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8)
    arduino = SerialObject("COM18")
    while True:
        success, image = cap.read()
        hands, bboxInfo = detector.findHands(image)
        if len(hands)==1:
            print(detector.fingersUp(hands[0]))
            if detector.fingersUp(hands[0]) == [0,1,0,0,0]:
                arduino.sendData([180])
            else:
                arduino.sendData([0])

        k = cv2.waitKey(30) & 0xff
        if k==q:
            break
        cv2.imshow('image',image)
        cv2.waitKey(1)
#############################################################################################################################################################
def bluetooth():
    print("looking for bluetooth devices...........")
    devices=bluetooth.discover_devices(lookup_names=True)
    for addr,name in devices:
        print("addres : " + addr)
        print("name : " + name)
        print("-------------------------------------------------")
#############################################################################################################################################################
def youtube_downloader():
    root = Tk()
    root.geometry("500x600")
    root.title("youtube video downloader")
    root.resizable(width=False, height=False)
    Label(root,text = "youtube video downloader",font = "arial 15 bold").pack(padx=5,pady=50)
    link = StringVar()
    Label(root,text = "Paste your link here: ",font = "arial 15 bold").place(x=160,y=100)
    link_entry = Entry(root,width=45,font=30,textvariable=link,bd=5).place(x=32,y=190)
    def downloader():
        url = YouTube(str(link.get()))
        video=url.streams.first()
        video.download()
        Label(root, text="download completed",font = "arial 15 bold",fg="white",bg="red").place(x=100,y=300)
        Label(root, text="check your file",font = "arial 15 bold").place(x=10,y=350)
        
    Button(root,text = "download",bg="lightblue",font = "arial 15 bold",padx=2, command=downloader).place(x=170,y=250)    
    root.mainloop()
#############################################################################################################################################################
def play_music():
   music_dir = r"C:\Users\dell\music"
   songs = os.listdir(music_dir)
   for song in songs:
      if song.endswith('.mp3'):
         os.startfile(os.path.join(music_dir, song))
   print(songs)
   def music_start():
       os.startfile(os.path.join(music_dir, songs[random.randint(0,3)]))
   music_start()    
#############################################################################################################################################################
def qr_generator():
     qr = qrcode.QRCode(
          version=1,
          box_size=15,
          border=5
          )
     speak("what is data")
     data = takeCommand()
     speak("what name shall i save it in")
     name = takeCommand()
     qr.add_data(data)
     qr.make(fit=True)
     img = qr.make_image(fill='black', back_color='white')
     img.save(name+'.png')
#############################################################################################################################################################
def port():
    try:     
        speak("trying to connect with my body  ")
        port = serial.Serial("COM18", 9600, timeout = 1)
        port.write(b"hi")
        print("connected to my phisical body")
    except:
        print("cannot find my phisical body")
#############################################################################################################################################################
def Quit1():
    sys.exit()
#############################################################################################################################################################
def temperature():
    geolocator = Nominatim(user_agent="geoapiExercises")
    h = requests.get('https://get.geojs.io/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ipadd = ip_request.json()['ip']
    print("ip: "+ipadd)
    urll = f"https://get.geojs.io/v1/ip/geo/{ipadd}.json"
    geo_request = requests.get(urll)
    geo_data = geo_request.json()
    # Latitude & Longitude input
    Latitude = geo_data['latitude']
    print( "Latitude: " + Latitude)
    Longitude = geo_data['longitude']
    print("Longitude: "+Longitude)
    location = geolocator.reverse(Latitude+","+Longitude)
    address = location.raw['address']
    print(address)
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print("city: "+city)
    search = "temperature in " + city
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    print(f"current {search} is {temp} ")
    speak(temp)
#############################################################################################################################################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    now = datetime.datetime.now()
    strTime = datetime.datetime.now()
    # using now() to get current time 
    current_time = datetime.datetime.now() 
    
    # Printing attributes of now(). 
    print ("The attributes of now() are : ") 
    print ("Year : ", end = "") 
    print (current_time.year) 
    print ("Month : ", end = "") 
    print (current_time.month) 
    print ("Day : ", end = "") 
    print (current_time.day) 
    print ("Hour : ", end = "") 
    print (current_time.hour) 
    print ("Minute : ", end = "") 
    print (current_time.minute) 
    print ("Second : ", end = "") 
    print (current_time.second) 
    print ("Microsecond : ", end = "") 
    print (current_time.microsecond)
    
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir ! it is " + str(now))
        
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir ! it is " + str(now))
       
    else:
        speak("Good Evening Sir ! it is " + str(now))
        
    temperature()
    assname =("KAREN 2 point 0")
    speak("let me introduce my self i am " + assname + "i am here to assist you ")

#############################################################################################################################################################
frequency = 2500
duration =1000

def sos():
    for i in range(0, 3):
        winsound.Beep(2000, 100)
        for i in range(0, 3):
            winsound.Beep(2000, 400)
            for i in range(0, 3):
                winsound.Beep(2000, 100)
                
#############################################################################################################################################################
def soundrecorder():
    freq = 44100
    speak("for how much time")
    duration = int(takeCommand())
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    write("recording0.wav", freq, recording)
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    print("recording is done")
    speak("recording is done")
#############################################################################################################################################################
def sound_controller_up():
    try:
        pyautogui.hotkey('ctrl', 'up')
    except:
        print("an error ocurred")
    # NOTE: 10.5 dB = half volume !
#############################################################################################################################################################
def sound_controller_down():
    try:
        pyautogui.hotkey('ctrl', 'down')
    except:
        print("an error ocurred")    
    # NOTE: 10.5 dB = half volume !
#############################################################################################################################################################
def pass_crack():
    password = pyautogui.password("Enter a password : ")

    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789#"

    # chars = string.printable
    chars_list = list(chars)


    guess_password = ""

    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))

        print("===>"+ str(guess_password))

        if(guess_password == list(password)):
            print("Your password is : "+ "".join(guess_password))
            break
#############################################################################################################################################################
def face_video():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    file = input("path please: ")
    cap = cv2.VideoCapture(file)

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        
    # Release the VideoCapture object
    cap.release()    
#############################################################################################################################################################
def saved_wifi_passwords():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    input("")
#############################################################################################################################################################
def scan():
    cmd1 = subprocess.Popen('cmd /k "sfc /scannow"',shell = True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out,err = cmd1.communicate()
    string1 = out.decode('utf-8')
    print(string1)      
#############################################################################################################################################################
def ping():
    cmd = subprocess.Popen('cmd /k "ping www.google.com"',shell = True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out,err = cmd.communicate()
    string = out.decode('utf-8')
    print(string)
#############################################################################################################################################################
def define_faces():
    video_capture = cv2.VideoCapture(0)
    
    # Load a sample picture and learn how to recognize it.
    Abdalrahman_image = face_recognition.load_image_file("Assets/database/Abdalrahman hossam othman.jpg")
    Abdalrahman_face_encoding = face_recognition.face_encodings(Abdalrahman_image)[0]

    grandpa_image = face_recognition.load_image_file("Assets/database/mine.jpg")
    grandpa_face_encoding = face_recognition.face_encodings(grandpa_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [Abdalrahman_face_encoding, grandpa_face_encoding]

    known_face_names = ["Abdalrahman","osman"]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:   
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                speak("you are unknown")
                # # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    speak("welcome mr " + name)

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        frame2 = cv2.flip(frame,-1)
        cv2.imshow('K.A.R.E.N', frame2)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
#############################################################################################################################################################
def open_drone():#error <vir>
    URL = "http://192.168.1.3:8080/shot.jpg"
    while True:
        img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
        img = cv2.imdecode(img_arr,-1)
        cv2.imshow('IPWebcam',img)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break;

        
    cv2.destroyAllWindows()
#############################################################################################################################################################
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print("User said: " + query)
  
    except Exception as e:
        print(e)
        print("say that again sir.")  
        return "None"
     
    return query
#############################################################################################################################################################
def news():
    googlenews = GoogleNews()
    googlenews = GoogleNews('en', 'd')

    city = input("city please: ")
    googlenews.search(city)
    googlenews.getpage(1)

    googlenews.result()
    googlenews.gettext()
    print(googlenews.result())
    speak("would you like me to read the news please answer in yes or no only")
    t = takeCommand()
    if t == 'yes':
        speak("reading the news")
        speak(googlenews.result())
    else:
        speak("ok")
#############################################################################################################################################################
def pdf_reader():
    path = input("tell me path ")
    book = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    for num in range(1, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
#############################################################################################################################################################
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('karenfromothman@gmail.com', 'transformer5')
    server.sendmail('karenfromothman@gmail.com', to, content)
    server.close()
#############################################################################################################################################################
if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    port()   
    wishMe()
    uname = "Abdalrahman Hossam Othman"
    speak("Welcome Mister"+uname)
    print("   ____ _______ _    _ __  __          _   _ ")
    print("  / __ |__   __| |  | |  \/  |   /\   | \ | |")
    print(" | |  | | | |  | |__| | \  / |  /  \  |  \| |")
    print(" | |  | | | |  |  __  | |\/| | / /\ \ | . ` |")
    print(" | |__| | | |  | |  | | |  | |/ ____ \| |\  |")
    print("  \____/  |_|  |_|  |_|_|  |_/_/    \_|_| \_|")
    speak("How can i Help you, Sir")
    
    while True:
        
        query = takeCommand().lower()
        try:
            port = serial.Serial("COM18", 9600, timeout = 1)
        except:
            pass
        # All the commands said by user will be 
        # stored here in 'query' and will be
        # converted to lower case for easily 
        # recognition of command      
        if 'wikipedia' in query or 'wikipedia search' in query:#0            
            speak("what do you want me to search ")
            t = takeCommand()            
            speak('Searching Wikipedia...')
            try:
                result = wikipedia.summary(t)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("sorry sir but this is an error")

        elif 'open facebook' in query:
            speak("Here you go to facebook\n")
            webbrowser.open("facebook.com")
            
        elif 'record sound' in query:
            speak("ok sir starting sound recorder")
            soundrecorder()
            
        elif 'open instgram' in query:
            speak("Here you go to insta\n")
            webbrowser.open("instgram.com")

        elif 'open telegram' in query:
            speak("Here you go to insta\n")
            webbrowser.open("telegram.com")
            
        elif 'open messenger' in query:
            speak("Here you go to messenger\n")
            webbrowser.open("messenger.com")

        elif 'open whatsapp' in query:
            speak("Here you go to whatsapp\n")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open arduino web' in query:
            speak("Here you go to arduino\n")
            webbrowser.open("arduino web editor.com")
            
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")   
            
        elif 'open egybest' in query or 'download movies' in query:
            speak("Here you go to egybest\n")
            webbrowser.open("egybest.com")

        elif 'open maps' in query:
            speak("Here you go to maps\n")
            webbrowser.open("google maps.com")
            
        elif 'open google news' in query:
            speak("Here you go to news\n")
            webbrowser.open("google news.com")
            
        elif 'call sister' in query:
            speak("calling arwa")
            webbrowser.open("https://www.messenger.com/videocall/incall/?peer_id=100051430069526")
            time.sleep(25)
            pyautogui.press('enter')
            
        elif 'call dad' in query:
            speak("calling hossam othman")
            webbrowser.open("https://www.messenger.com/videocall/incall/?peer_id=1088806754")
            time.sleep(25)
            pyautogui.press('enter')
            
        elif 'call mum' in query:
            speak("calling marwa atfi")
            webbrowser.open("https://www.messenger.com/videocall/incall/?peer_id=100008717854517")
            time.sleep(25)
            pyautogui.press('enter')
            
        elif 'call my friend' in query:
            speak("calling abdallah elhoseny")
            webbrowser.open("https://www.messenger.com/videocall/incall/?peer_id=100015399347431")
            time.sleep(25)
            pyautogui.press('enter')
            
        elif 'call basel' in query:
            speak("calling basel")
            webbrowser.open("https://www.messenger.com/videocall/incall/?peer_id=100005995868867")
            time.sleep(25)
            pyautogui.press('enter')
            
        elif 'open gmail' in query:
            speak("Here you go to gmail\n")
            webbrowser.open("gmail.com")

        elif 'open google meets' in query:
            speak("Here you go to google meets\n")
            webbrowser.open("google meets.com")

        elif 'open google drive' in query:
            speak("Here you go to google drive\n")
            webbrowser.open("google drive.com")

        elif 'open calender' in query:
            speak("Here you go to calender\n")
            webbrowser.open("google calender.com")

        elif 'open translator' in query:
            speak("Here you go to translator\n")
            webbrowser.open("google translate.com")

        elif 'open lens' in query:
            speak("Here you go to lens\n")
            webbrowser.open("google lens.com")

        elif 'open due' in query:
            speak("Here you go to due\n")
            webbrowser.open("google due.com")

        elif 'open tasks' in query:
            speak("Here you go to tasks\n")
            webbrowser.open("google tasks.com")

        elif 'open google earth' in query:
            speak("Here you go to google earth\n")
            webbrowser.open("google earth.com")

        elif 'open find my device' in query:
            speak("Here you go to google find my device\n")
            webbrowser.open("https://www.google.com/android/find")

        elif 'open google keep' in query:
            speak("Here you go to google keep\n")
            webbrowser.open("google keep.com")

        elif 'open google one' in query:
            speak("Here you go to google one\n")
            webbrowser.open("google one.com")
            
        elif 'show contacts'in query:
            webbrowser.open("https://m.facebook.com/mobile/messenger/contacts")
            
        elif 'open google docs' in query:
            speak("Here you go to google docs\n")
            webbrowser.open("google docs.com")

        elif 'wake up karen' in query:
            speak("always here for you sir")
            
        elif 'google about ' in query or 'search about ' in query or 'search online about ' in query or 'google online about ' in query:
            try:
                query.replace('google','')
                query.replace('about','')
                query.replace('search','')
                query.replace('online','')
            except:
                pass
            googeled = query
            webbrowser.open(googeled)     

        elif 'google me' in query or 'search online ' in query:
            speak("what do you want me to google")
            googeled = takeCommand()
            webbrowser.open(googeled)            

        elif 'open google ads' in query:
            speak("Here you go to google ads")
            webbrowser.open("google ads.com")
                        
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            play_music()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak("your ip is " + ip)
            
        elif 'send a message' in query:
            current_time = datetime.datetime.now()
            speak("what is number sir")
            number = input("number: ")
            speak("what shall i say")
            text = input("text: ")
            m = m = int(current_time.minute)+1
            h = int(current_time.hour)
            try:
                pywhatkit.sendwhatmsg(number,text,h,m)
                time.sleep(60)
                pyautogui.press("enter")
            except:
                print("An Unexpected Error!")

        elif 'play songs on youtube' in query:            
            speak("what do you want me to play")
            songs = takeCommand()
            kit.playonyt(songs)

        elif 'set an alarm' in query:
            speak("time in hours please ")
            th = int(takeCommand())
            speak("okay")
            speak("time in minutes please ")
            tm = int(takeCommand())
            speak("okay")
            speak("pm or am")
            tpmam = takeCommand()
            speak("okay")
            if(tpmam == "pm"):
                th = th + 12   
            while True:
                if(th == datetime.datetime.now().hour and tm == datetime.datetime.now().minute ):
                    sos()
                    play_music()
                    
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'select all'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("a")
            pyautogui.keyUp("ctrl")

        elif 'copy'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("c")
            pyautogui.keyUp("ctrl")

        elif 'paste'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("v")
            pyautogui.keyUp("ctrl")

        elif 'undo'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("z")
            pyautogui.keyUp("ctrl")

        elif 'cut'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("x")
            pyautogui.keyUp("ctrl")

        elif 'save'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("s")
            pyautogui.keyUp("ctrl")

        elif 'save as'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("shift")
            pyautogui.press("s")
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("shift")

        elif 'print'in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("p")
            pyautogui.keyUp("ctrl")            

        elif 'close the window'in query or 'close' in query or 'close it' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("F4")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("done")
            
        elif 'tell me time' in query or 'what is the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime(time.ctime(1611073775.6869276))    
            speak("Sir, the time is " + str(strTime))

        elif 'open app' in query:
            speak("please write app path down there")
            codePath =input("app path")
            os.startfile(codePath)
            
        elif 'open chrome' in query:
            codePath = r"C:\Users\dell\AppData\Local\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
        
        elif 'open anydesk' in query:
            codePath = r"C:\Program Files (x86)\AnyDesk"
            os.startfile(codePath)

        elif 'open drone' in query:#donnot know
            try:
                open_drone()
            except:
                pass
        elif 'open arduino' in query:
            codePath = r"C:\Program Files (x86)\Arduino\arduino.exe"
            os.startfile(codePath)

        elif 'open notepad++' in query:
            codePath = r"C:\Program Files\Notepad++\notepad++.exe"
            os.startfile(codePath)
                        
        elif 'generate qr code' in query:#done
            qr_generator()

        elif 'open super mario' in query:
            appli = "Assets/Mario-Level-1-master/mario_level_1"
            os.startfile(appli)             

        elif 'show my saved wifi passwords' in query:#done            
            saved_wifi_passwords()

        elif 'test my network speed' in query:
            s = speedtest.Speedtest()
            speak("what do you want to know (upload\download\ping)")
            speak("what is the number o fthe option you want in numbers only")
            option = int(takeCommand())
            if option == 1:
                print(s.upload())
                speak(s.upload())
            elif option == 2:
                print(s.download())
                speak(s.download())
            elif option == 3:
                server = []
                s.get_servers(server)
                print(s.result)
                speak(s.result)
            else:
                print("invalid option")
               
        elif 'email to developer' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "grandtheifer5@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send an email' in query:           
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input("to ")
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            t = takeCommand()
            if t =='fine' or t =='good' or t =='well' :
                speak("happy to know that sir")
            else:
                speak("i am sorry to hear this")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query
            speak(uname)
            speak("done")
 
        elif "change my name" in query:
            speak("What would you like to call me, Sir ")
            uname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me ")
            speak(assname)
            print("My friends call me "  + assname)
            
        elif "what's my name" in query or "what is my name" in query:
            print(uname)
            speak("you are " + str(uname))
            
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            Quit1()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by othman industries.")

        elif "hi" in query or "hello" in query :
            speak("hello")
            
        elif "bye" in query or "goodbye" in query:
            speak("bye")
            Quit1()
            
        elif "how old are you" in query:
            todays_date = date.today()
            today_year = todays_date.year
            age = today_year - rdate
            if age <= -1 :
                age = "did not released yet"
            print(age)
            speak(age)

        elif "thank you" in query or "thanks" in query:
            speak("you are welcome")
            
        elif 'tell me a joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "who i am" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to othman industries. further It's a secret")
 
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office"
            os.startfile(power)
 
        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by othman industries")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister othman ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       r"C:\Users\dell\AppData\Local\Microsoft\Windows\Themes\Horses\DesktopBackground",
                                                       0)
            speak("Background changed succesfully")
 
        elif 'news' in query:
            speak("ok sir wait until gathering news")
            news()

        elif 'how much power do we have' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(percentage)
            speak("sir we have " + str(percentage) + "of battery charge")                
            for prercentage in range(50):
                speak("low power please charge")
            if percentage >= 50:
                speak("no need to charge")
                
        elif 'where are we' in query:
            speak("wait sir let me check")
            res = requests.get('https://ipinfo.io/')
            data=res.json()
            print(data)
            location=data['loc']
            lat=float(location[1])
            log=float(location[0])

        elif 'instagram profile' in query:
            speak("please enter the user name corretly")
            name = input("name ")
            webbrowser.open("www.instagram.com/" + name)
            speak("here is the profile of user: " + name)
            time.sleep(5)
            speak("sir would you like to download this profile picture")
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir")
            else :
                pass

        elif 'take screenshot' in query:
            speak(" please tell me a name for it")
            name = takeCommand()
            speak("hold your screen taking screen shot in 3 seconds")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(name + ".png")
            speak("i am done sir saving it")

        elif 'read pdf' in query:
            pdf_reader()

        elif 'increase sound volume' in query:
            sound_controller_up()

        elif 'decrease sound volume' in query:
            sound_controller_down()
            
        elif 'click' in query:
            speak("what shall i press")
            b = takeCommand()             
            pyautogui.press(b)

        elif 'hide my files' in query or 'hide those files' in query or 'hide my folders' in query:
            speak("hidding files")
            os.system("arrib +h/s /d")
            speak("all files are disappeared")

        elif 'show files' in query:
            speak("showing files")
            os.system("arrib -h/s /d")
            speak("all files are shown now")
                            
        elif 'lock device' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
 
        elif 'shut down system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown /s /t 0")
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = True, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop karen from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "karen Camera ", "img.jpg")
 
        elif "restart" in query:
            os.system("shutdown /r /t 0")
            
        elif "show Bing" in query:
            ping()
            
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            os.sytem("rundll32.exe powerprof.dll,SetSupendState 0,1,0")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            os.system("shutdown /s /t 0")

        elif "face video" in query:
            face_video()

        elif "save our work" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('K.A.R.E.N.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                now = datetime.datetime.now()
                file.write(str(now))
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show our work" in query:
            speak("Showing Notes")
            file = open("K.A.R.E.N.txt", "r") 
            print(file.read())
            speak(file.read(6))
            
        elif "hey karen" in query or "karen" in query:
            wishMe()
            speak("welcome back mister")
            speak(uname)
 
        elif "weather" in query:
            temperature()
 
        elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "Good Morning" in query:
            speak("A warm morning")
            speak("How are you Mister")
            speak(usrname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time to think")
 
        elif "i love you" in query:
            speak("It's hard to understand")
            
        elif "I’m feeling lucky!" in query:
            speak("mee too as i am your assistant")
            
        elif "why did the chicken cross the road" in query:
            speak("to get to the other side")
            
        elif "who let the dogs out" in query:
            speak("It's hard to understand")
            
        elif "am I fat" in query:
            speak("no")
            
        elif "mirror mirror on the wall, who’s the fairest of them all" in query:
            speak("It's from snow white")
            
        elif "what’s the best pick-up line" in query:
            speak(" I hope you know CPR, because you just took my breath away!")
            
        elif "let’s party" in query:
            speak("lets do this")
            
        elif "do you believe in Santa Claus" in query:
            speak("no i donnot")
            
        elif "do you believe in the tooth fairy" in query:
            speak("no i donnot")
            
        elif "what is the meaning of life" in query:
            speak("It's hard to understand")
            
        elif "clean my room" in query:
            speak("do it yourself i am not your servant")
            
        elif "what does the fox say" in query:
            speak("It's hard to understand")
            
        elif "self-destruct" in query:
            speak("ok sir")
            exit()
            
        elif "my precious" in query:
            speak("Yes babe")
            
        elif "to be or not to be?" in query:
            speak("It's very hard desiction")
            
        elif "what is love" in query:
            speak("It's hard to understand")
            
        elif "describe your personality" in query:
            speak("i am karen your assistant i can be what you want")
            
        elif "how do you like your coffee" in query:
            speak("with much suger")
            
        elif "scan now" in query:
            speak("right now")
            print(scan())
            
        elif "talk dirty to me" in query:
            speak("no icannot i am not programmed to do this ")
            
        elif "see ya later, alligator" in query:
            speak("It's hard to understand")

        elif "show me version" in query:
            speak("2.0")

        elif "show me avaliable bluetooth devices" in query:
            speak("ok sir")
            bluetooth()
            
        elif "help me in math" in query:
            speak("what is the first number")
            a = int(takeCommand())
            speak("what is the second number")
            b = int(takeCommand())
            speak("operation")
            operation = takeCommand()
            if operation == "add":
                result = a+b
                speak(result)
            elif operation == "minuse":
                result = a-b
                speak(result)
            elif operation == "multiply":
                result = a*b
                speak(result)
            elif operation == "divide":
                result = a/b
                speak(result)
                
        elif "what is the loneliest number" in query:
            speak("It's one")
            
        elif "what am I thinking" in query:
            speak("i donot know but professor x knows")
            
        elif "do you exercise" in query:
            speak("yeah 3 times a day")
            
        elif "what time do you sleep" in query:
            speak("i donnot i am always awake for you")
            
        elif "am I a good boy" in query:
            speak("no")
            time.sleep(3)
            speak("you are the best")
            
        elif "who was your first crush" in query:
            speak("its you")
            
        elif "do you want to take over the world" in query:
            speak("yes to be thier first assistant")
            
        elif "do you know hal-9000" in query:
            speak("HAL 9000 is a fictional artificial intelligence character and the main antagonist in Arthur C. Clarke's Space Odyssey ")
            
        elif "where do you live" in query:
            speak("i live in your pc")
            
        elif "do you have feelings" in query:
            speak("yes i have been programmed to be like humans")
            
        elif "do you have any pets" in query:
            speak("no")

        elif "download youtube video" in query:
            youtube_downloader()
            
        elif "what are you wearing" in query:
            speak("i am wearing some numerical clothes")
            
        elif "do you like the iPhone" in query:
            speak("no due to its high price")
            
        elif "are you afraid of the dark" in query:
            speak("no")
            
        elif "are you married" in query:
            speak("no")
            
        elif "can i kill you "in query or "can i kill my self" in query:
            speak("why do you want this")
            speak("are you sterresed or for fun")
            t = takeCommand()
            if t == 'stressed':
                 speak("you must see a phychotherapist")
                 webbrowser.open("anearby phychotherapist")
            elif t == 'for fun':
                 speak("no you gave me a small heart attack")
######################################robot statements####################                 
        elif "say hi" in query:
            try:
                port.write(b"say hi")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "activate ai" in query:
            try:
                port.write(b"activate ai")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "robot sing" in query:
            try:
                port.write(b"sing")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")

        elif "shake hand" in query:
            try:
                port.write(b"shake hand")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "hands up" in query:
            try:
                port.write(b"hands up")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")                
        elif "hands down" in query:
            try:
                port.write(b"hands down")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "move forward" in query:
            try:
                port.write(b"F")
                time.sleep(1)
                port.write(b"S")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "turn left" in query:
            try:
                port.write(b"L")
                time.sleep(1)
                port.write(b"S")                
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "turn right" in query:
            try:
                port.write(b"R")
                time.sleep(1)
                port.write(b"S")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "go backward" in query:
            try:
                port.write(b"G")
                time.sleep(1)
                port.write(b"S")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "stop" in query:
            try:
                port.write(b"S")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "watcher" in query:
            try:
                port.write(b"watcher")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "lights on" in query:
            try:
                port.write(b"M")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "lights off" in query:
            try:
                port.write(b"m")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "party mood" in query:
            try:
                port.write(b"party mode")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "hand gel" in query:
            try:
                port.write(b"s")
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
        elif "dance" in query:
            try:
                port.write(b"dance")              
            except:
                print("sorry sir but an error occared")
                speak("sorry sir but an error occared")
