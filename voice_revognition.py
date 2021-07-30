# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:37:56 2021

@author: Tuf Gaming
"""

import speech_recognition as sr

#%%

def recognize_speech_from_mic(recognizer, microphone):
  
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # sesuaikan sensitivitas pengenal terhadap kebisingan sekitar dan rekam audio
    # dari mikrofon
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        audio = recognizer.listen(source)

    # mengatur objek respons
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # coba kenali ucapan dalam rekaman
    # jika pengecualian RequestError atau UnknownValueError tertangkap,
    # perbarui objek respons yang sesuai
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API tidak dapat dijangkau atau tidak responsif
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        # ucapan tidak dapat dipahami
        response["error"] = "Unable to recognize speech"

    return response

#%%

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    response = recognize_speech_from_mic(recognizer, mic)
    print('\nSuccess : {}\nError   : {}\n\nText from Speech\n{}\n\n{}' \
          .format(response['success'],
                  response['error'],
                  '-'*17,
                  response['transcription']))