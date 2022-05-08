def takeCommandHindi():
         
    r = sr.Recognizer()
    with sr.Microphone() as source:
          
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        print('Listening')
        r.pause_threshold = 0.7  
        audio = r.listen(source)  
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='hi-In')
              
            # for listening the command in indian english
            with open('response.txt', 'w', encoding='utf8') as file:
                file.write(Query)
            print("the query is printed='", Query, "'")
          
        # handling the exception, so that assistant can 
        # ask for telling again the command
        except Exception as e:
            print(e)  
            print("Say that again sir")
            return "None"
        return Query


import speech_recognition as sr

r = sr.Recognizer()
if __name__=='__main__':
    takeCommandHindi()