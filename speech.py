import speech_recognition, pyaudio

def speech():
    mic = speech_recognition.Microphone()
    recog = speech_recognition.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        return recog.recognize_google(audio, language = "en-US")
    
def forGame():   
    mic = speech_recognition.Microphone()
    recog = speech_recognition.Recognizer()

    with mic as audio_file:
        print("SAY SOMETHING DIGGA")
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        
        print("Alr, we are interpreting ya'")
        print(f"You have just said: {recog.recognize_google(audio, language='fr-FR')}")
        
        return recog.recognize_google(audio, language='fr-FR')