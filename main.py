# Import the pyttsx3 module for text-to-speech (TTS)
import pyttsx3 
 
# Initialize the TTS engine
guru = pyttsx3.init()

# Get the list of available voices
voices = guru.getProperty('voices')

# Set the voice to the second one in the list (typically a female voice)
guru.setProperty('voice', voices[1].id)

# Set the speech rate (words per minute)
guru.setProperty("rate", 150)

# Set the volume level (1.0 is max)
guru.setProperty("volume", 1)

# Import the speech recognition module
import speech_recognition as sr

# Initialize the variable for storing recognized query
query = ""

# Function to record and recognize speech
def record_volume():
    # Create a Recognizer instance
    r = sr.Recognizer()
    
    # Use the microphone as the source of input
    with sr.Microphone(device_index=1) as source:  # You may need to change device_index depending on your system
        print('Setting...')
        
        # Adjust for background noise (0.5 seconds)
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        print('Listening...')
        
        # Listen for audio input from the microphone
        audio = r.listen(source)
    
    print('Heard.')

    try:
        # Recognize the spoken audio using Google Web Speech API
        query = r.recognize_google(audio, language='en-EN')
        
        # Convert the recognized text to lowercase
        text = query.lower()
        
        # Print the recognized text to console
        print(f'You said: {text}')
        
        # Speak the recognized text using pyttsx3
        guru.say(f'You said: {text}')
        guru.runAndWait()
        
    except:
        # Handle recognition errors
        print('Error')

# Keep listening until the user says "exit"
while query != 'exit':
    record_volume()
