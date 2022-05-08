def speech_read(source):
    print("Talk")
    #r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        x=r.recognize_google(audio_text)
        #print("Text: "+x)
        return x
    except:
         print("Sorry, I did not get that")
    return 'read_error'


def say(mytext):
    command = "speak.vbs \""+mytext+"\" 1"
    os.system(command)

def playing(sound):
    s=os.getcwd()+"\\"+sound
    playsound(s)

def starting():
    playing("INTRO.mp3")
    say("MiRA WELCOMES YOU, USER")
    with sr.Microphone() as source:
        gate=True
        
        while gate:
            say("Speak your wish, user")
            response=speech_read(source)
            if(response!='read_error'):
                print(response)
                if(response.lower() in tw):

                    say("Sure.. terminating")
                    playing("OUTTRO.mp3")
                    gate=False


#import library

import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import constants
tw=constants.terminate_words
r = sr.Recognizer()
if __name__=='__main__':
    starting()  