# Imtiaz Adar
# Phone : +8801778 767775
# Email : imtiaz-adar@hotmail.com
# Project : Text To Speech
# Language Used : Python

import pyttsx3 as audio
engine = audio.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
text = input()
engine.say(text)
engine.save_to_file(text, 'Imtiaz Adar.mp3')
print(text)
engine.runAndWait()
engine.stop()