import pyttsx3

text = str(input("Enter the text to voice convert: "))

    
aaaa=str(input("are you male or female:"))
     

                 
engine = pyttsx3.init()

engine.setProperty('rate', 150)  


engine.setProperty('volume', 0.9)  


voices = engine.getProperty('voices')

if aaaa =="male":#male voice
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.save_to_file(text, 'voice_test.mp3')
    engine.runAndWait()
    print("sava voice_test.mp3  file")
              
elif aaaa =="female": #female voice
    
    engine.setProperty('voice', voices[1].id)
              


    engine.say(text)
    engine.save_to_file(text, 'voice_test.mp3')
    engine.runAndWait()
    print("sava voice_test.mp3  file")
 
