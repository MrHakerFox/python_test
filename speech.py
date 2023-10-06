import pyttsx3

text = input()
#text = 'Привет, Мася. Привет, Сальма. Погода нынче хорошая и замечательная!!!'
tts = pyttsx3.init()
rate = tts.getProperty('rate') #Скорость произношения
tts.setProperty('rate', rate - 40)

volume = tts.getProperty('volume') #Громкость голоса
tts.setProperty('volume', volume + 0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос
#for voice in voices:
#	if voice.name == 'Elena':
#		tts.setProperty('voice', voice.id)

tts.say(text)

#for voice in voices:
#	tts.say(voice.name)


tts.runAndWait()
