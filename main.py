import pyttsx3

guru = pyttsx3.init()
voices = guru.getProperty('voices')
# guru.setProperty('voice', '')
guru.setProperty('voice', voices[1].id)
guru.setProperty("rate", 150)
guru.setProperty("volume", 1)

import speech_recognition as sr
query=""
def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Setting...')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('Listening...')
        audio = r.listen(source)
    print('Heard.')
    try:
        query = r.recognize_google(audio, language = 'en-EN')
        text = query.lower()
        print(f'You said: {query.lower()}')
        guru.say(f'You said: {query.lower()}')
        guru.runAndWait()
    except:
        print('Error')

while query!='exit':
    record_volume()