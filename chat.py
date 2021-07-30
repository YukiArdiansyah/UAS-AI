# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:38:17 2021

@author: Tuf Gaming
"""

import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr
from speech_recognition.__main__ import r, audio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)

salam = ['hai di sana', 'halo', 'hai', 'Hai', 'hei!', 'hai']
pertanyaan = ['Apa kabar?', 'Apa kabar?']
tanggapan = ['Oke', "Saya baik-baik saja"]
var1 = ['siapa yang membuat Anda', 'siapa yang menciptakan Anda']
var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['jam berapa sekarang', 'jam berapa', 'waktu']
var4 = ['siapa kamu', 'siapa namamu']
cmd1 = ['buka browser', 'buka google']
cmd2 = ['putar musik', 'putar lagu', 'putar lagu', 'buka pemutar musik']
cmd3 = ['buka youtube', 'saya ingin menonton video']
cmd4 = ['beritahu saya cuacanya', 'cuaca', 'bagaimana dengan cuacanya']
cmd5 = ['keluar', 'tutup', 'selamat tinggal', 'tidak ada']
cmd6 = ['apa warnamu', 'apa warnamu', 'warnamu', 'warnamu?']
colrep = ['Sekarang ini pelangi', 'Sekarang transparan', 'Sekarang tidak berwarna']
cmd7 = ['apa warna favoritmu', 'apa warna favoritmu']
cmd8 = ['terima kasih']



while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan Berbicara untuk bisa dipahami:")
        audio = r.listen(source)
        try:
            print("Anda Berbicara:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Tidak Bisa Memahami Audio")
            engine.say('Jalankan kembali kodinganya')

            engine.runAndWait()
    if r.recognize_google(audio) in salam:
        random_salam = random.choice(salam)
        print(random_salam)
        engine.say(random_salam)
        import win32com.client as wincl
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(random_salam)
        engine.runAndWait()
    elif r.recognize_google(audio) in pertanyaan:
        engine.say('I am fine')
        engine.runAndWait()
        print('I am fine')
    elif r.recognize_google(audio) in var1:
        engine.say('Dibuat Ardi')
        engine.runAndWait()
        reply = random.choice(var2)
        print(reply)
    
    elif r.recognize_google(audio) in cmd7:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('Itu terus berubah setiap mikro detik')
        engine.say('Itu terus berubah setiap mikro detik')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd8:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd2:
        mixer.init()
        mixer.music.load("song.wav")
        mixer.music.play()
    elif r.recognize_google(audio) in var4:
        engine.say('I am a bot, silly')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd4:
        webbrowser.open('www.youtube.com')
    elif r.recognize_google(audio) in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()
    

        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
        webbrowser.open('www.google.com')
    
    else:
        engine.say("please wait")
        engine.runAndWait()
        print(wikipedia.summary(r.recognize_google(audio)))
        engine.say(wikipedia.summary(r.recognize_google(audio)))
        engine.runAndWait()
        userInput3 = input("or else search in google")
        webbrowser.open_new('www.google.com/search?q=' + userInput3)