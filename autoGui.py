
import speech_recognition as sr
import pyautogui
import telebot
import requests
from tkinter import Tk
from pydub import AudioSegment
import os

screenName = 'screenShot.png'

# claim = 'img/2.png'
claim2 = 'img/21.png'
claim = 'img/2small.png'
mainMine = 'img/23.png'

captcha = 'img/3.png'
# minningHub = 'img/4.png'
minningHub = 'img/42.png'
# mine = 'img/5.png'
mine = 'img/5small.png'
closeError = 'img/6.png'
audioIcon = 'img/7.png'
audioIcon2 = 'img/14.png'

audioDownload = 'img/8.png'
copyAdress = 'img/9.png'
approved = 'img/10.png'
approved2 = 'img/10num2.png'

ansArea = 'img/11.png'
ansArea2 = 'img/15.png'

acceptAudio = 'img/12.png'
captchaError = 'img/13.png'

refresh = 'img/16.png'
login = 'img/17.png'
mineMainMenu = 'img/18.png'

flagError = 'img/24.png'
deny = 'img/25.png'

resetAudioCaptcha = 'img/26.png'

tryLater = 'img/tryLater.png'
denyInactive = 'img/denyInactive.png'


def checkCaptcha():
	checkButton(captcha)
	check = pyautogui.locateCenterOnScreen(approved)
	check = pyautogui.locateCenterOnScreen(approved)
	check = pyautogui.locateCenterOnScreen(approved)
	check = pyautogui.locateCenterOnScreen(approved)
	check2 = pyautogui.locateCenterOnScreen(approved2)
	if (check == None and check2 == None):
		checkButton(audioIcon2)
		audioCaptchaSolve()
	checkButton(approved2)	

def audioCaptchaSolve(error = False):
		checkButtonRight(audioDownload)
		checkButton(copyAdress)

		adress = Tk().clipboard_get()

		saveAudio(adress)
		getWavClip()

		try:
			ans = recognize()
		except Exception as e:
			pyautogui.click(pyautogui.locateCenterOnScreen(resetAudioCaptcha, confidence=0.8))
			newMainLoop()
		if error:
			checkButton(ansArea2)
		else:
			checkButton(ansArea)

		print('Recognized text: ' + ans)
		pyautogui.write(ans)
		checkButton(acceptAudio)
		print('endCaptcha!')


def saveAudio(adress):
	ufr = requests.get(adress)
	with open('audio.mp3',"wb") as file:
		file.write(ufr.content)

def makeScreen():
	try:
		bot = telebot.TeleBot("809026438:AAGK1O8X7g_FjMUj1pYJHym5Hqi6PDO7zF4")
		pyautogui.screenshot(screenName)
		with open(screenName, 'rb') as file:
			bot.send_document('648967686', file)
	except Exception as e:
		with open('errorInfo.txt', 'w+') as file:
			file.write(str(e))

def checkButton(button):
	check = pyautogui.locateCenterOnScreen(button, confidence=0.8)
	while check == None:
		check = pyautogui.locateCenterOnScreen(button, confidence=0.8)
	pyautogui.click(check, duration = 0.5)


def checkDefaultButtons():

	check = pyautogui.locateCenterOnScreen(claim, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	check = pyautogui.locateCenterOnScreen(mainMine, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	check = pyautogui.locateCenterOnScreen(captcha, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	check = pyautogui.locateCenterOnScreen(mine, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	check = pyautogui.locateCenterOnScreen(audioIcon2, confidence=0.8)
	if check != None:
		checkButton(audioIcon2)

	check = pyautogui.locateCenterOnScreen(closeError, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	if pyautogui.locateCenterOnScreen(audioDownload, confidence=0.8) != None:
		audioCaptchaSolve()

	checkError = pyautogui.locateCenterOnScreen(tryLater)
	if checkError != None:
		checkButton(denyInactive)
		checkButton(deny)

	check = pyautogui.locateCenterOnScreen(flagError, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	check = pyautogui.locateCenterOnScreen(approved2, confidence=0.8)
	if check != None:
		pyautogui.click(check)

	check = pyautogui.locateCenterOnScreen(captchaError, confidence=0.8)
	if check != None:
		audioCaptchaSolve(True)

	check = pyautogui.locateCenterOnScreen(minningHub, confidence=0.8)
	if check != None:
		pyautogui.click(check)


def checkButtons(button1, button2):
	check1 = pyautogui.locateCenterOnScreen(button1)
	check1 = pyautogui.locateCenterOnScreen(button1)
	check2 = pyautogui.locateCenterOnScreen(button2)
	while check1 == None and check2 == None:
		check1 = pyautogui.locateCenterOnScreen(button1, confidence=0.8)
		check2 = pyautogui.locateCenterOnScreen(button2, confidence=0.8)
	if check1 == None:
		pyautogui.click(check2, duration = 0.5)
	else:
		pyautogui.click(check1, duration = 0.5)

def checkButtonRight(button):
	check = pyautogui.locateCenterOnScreen(button)
	while check == None:
		check = pyautogui.locateCenterOnScreen(button)

	pyautogui.click(check, button='right')

def getWavClip():
	sound = AudioSegment.from_mp3("audio.mp3")
	sound.export("audio.wav", format="wav")

def recognize():
	recog = sr.Recognizer()
	sample_audio = sr.AudioFile('audio.wav')
	with sample_audio as source:
		audio_content = recog.record(source)
		return recog.recognize_google(audio_content)

def checkForError():
	check = pyautogui.locateCenterOnScreen(closeError)
	check = pyautogui.locateCenterOnScreen(closeError)
	check = pyautogui.locateCenterOnScreen(closeError)
	if check != None:
		makeScreen()
		checkButton(closeError)
		mainLoop()

def checkForCpuError():
	check = pyautogui.locateCenterOnScreen(closeError)
	check = pyautogui.locateCenterOnScreen(closeError)
	check = pyautogui.locateCenterOnScreen(closeError)
	if check != None:
		makeScreen()
		checkButton(refresh)
		checkButton(login)
		checkButton(mineMainMenu)
		return 1
	return 0


def mainLoop():
	try:
		while True:
			checkButton(claim)
			checkForError()

			checkCaptcha()
			checkForError()

			checkButton(minningHub)
			checkButton(mine)
	except Exception as e:
		with open('errorInfo.txt', 'w+') as file:
			file.write(str(e))

# if __name__ == '__main__':
# 	checkButton(mine)
# 	mainLoop()

def newMainLoop():
	try:
		while True:
			checkDefaultButtons()
	except:
		print('RESTART !!!')
		newMainLoop()


if __name__ == '__main__':
	newMainLoop()

