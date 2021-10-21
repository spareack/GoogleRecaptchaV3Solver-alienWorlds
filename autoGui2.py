
import speech_recognition as sr
import pyautogui
import telebot
import requests
from tkinter import Tk
from pydub import AudioSegment
import os

screenName = 'screenShot.png'

claim = '2.png'
captcha = '3.png'
minningHub = '4.png'
mine = '5.png'
closeError = '6.png'
audioIcon = '7.png'
audioIcon2 = '14.png'

audioDownload = '8.png'
copyAdress = '9.png'
approved = '10.png'
ansArea = '11.png'
ansArea2 = '15.png'

acceptAudio = '12.png'
captchaError = '13.png'


claim_fire = '2_1.png'
claim_fire2 = '2_1_2.png'

captcha_fire = '3_1.png'
minningHub_fire = '4_1.png'
mine_fire = '5_1.png'
closeError_fire = '6_1.png'
audioIcon_fire = '7_1.png'
audioIcon2_fire = '14_1.png'

audioDownload_fire = '8_1.png'
copyAdress_fire = '9_1.png'
approved_fire = '10_1.png'
approved_fire2 = '10_1_2.png'
ansArea_fire = '11_1.png'
ansArea2_fire = '15_1.png'

acceptAudio_fire = '12_1.png'
captchaError_fire = '13_1.png'

errorTryLater_fire = '19.png'
errorTryLaterDeny_fire = '20_1.png'
errorTryLaterDenyActive_fire = '21_1.png'
errorTryLaterClose_fire = '22_1.png'



def checkCaptcha():
	checkButton(captcha)

	check = pyautogui.locateCenterOnScreen(approved)
	check = pyautogui.locateCenterOnScreen(approved)
	check = pyautogui.locateCenterOnScreen(approved)
	if (check == None):
		print(pyautogui.locateCenterOnScreen(audioIcon2))
		print(pyautogui.locateCenterOnScreen(audioIcon2))
		checkButton(audioIcon2)
		audioCaptchaSolve()
	checkButton(approved)	

def audioCaptchaSolve(error = False):
		checkButtonRight(audioDownload)
		checkButton(copyAdress)

		adress = Tk().clipboard_get()

		saveAudio(adress)

		getWavClip()
		ans = recognize()

		if error:
			checkButton(ansArea2)
		else:
			checkButton(ansArea)

		print('Recognized text: ' + ans)

		pyautogui.write(ans)
		checkButton(acceptAudio)

		errorCheck = pyautogui.locateCenterOnScreen(captchaError)
		errorCheck = pyautogui.locateCenterOnScreen(captchaError)
		errorCheck = pyautogui.locateCenterOnScreen(captchaError)
		if  errorCheck != None:
			audioCaptchaSolve(True)


def checkCaptcha_fire():
	checkButton(captcha_fire)

	check = pyautogui.locateCenterOnScreen(approved_fire)
	check = pyautogui.locateCenterOnScreen(approved_fire)
	check = pyautogui.locateCenterOnScreen(approved_fire)
	if (check == None):
		checkButton(audioIcon2_fire, 1)

		check = pyautogui.locateCenterOnScreen(errorTryLater_fire)
		check = pyautogui.locateCenterOnScreen(errorTryLater_fire)
		if check != None:
			checkButton(errorTryLater_fire)
			checkButton(errorTryLaterDeny_fire)
			checkButton(errorTryLaterDenyActive_fire)
			checkButton(errorTryLaterClose_fire)
			return 1
		
		audioCaptchaSolve_fire()
	checkButtons(approved_fire, approved_fire2)
	return 0

def audioCaptchaSolve_fire(error = False):
		checkButtonRight(audioDownload_fire)
		checkButton(copyAdress_fire)

		adress = Tk().clipboard_get()

		saveAudio(adress)

		getWavClip()
		ans = recognize()

		if error:
			checkButton(ansArea2_fire)
		else:
			checkButton(ansArea_fire)

		print('Recognized text: ' + ans)

		pyautogui.write(ans)
		checkButton(acceptAudio_fire)

		# errorCheck = pyautogui.locateCenterOnScreen(captchaError)
		# errorCheck = pyautogui.locateCenterOnScreen(captchaError)
		# errorCheck = pyautogui.locateCenterOnScreen(captchaError)
		# if  errorCheck != None:
		# 	audioCaptchaSolve_fire(True)


def saveAudio(adress):
	ufr = requests.get(adress)
	with open('audio.mp3',"wb") as file:
		file.write(ufr.content)

def makeScreen():
	bot = telebot.TeleBot("809026438:AAGK1O8X7g_FjMUj1pYJHym5Hqi6PDO7zF4")
	pyautogui.screenshot(screenName)
	with open(screenName, 'rb') as file:
		bot.send_document('648967686', file)

def checkButton(button, duration = None):
	check = pyautogui.locateCenterOnScreen(button)
	while check == None:
		check = pyautogui.locateCenterOnScreen(button)
	if duration == None:
		pyautogui.click(check)
	else:
		pyautogui.click(check, duration = 0.5)

def checkButtons(button1, button2):
	check1 = pyautogui.locateCenterOnScreen(button1)
	check1 = pyautogui.locateCenterOnScreen(button1)
	check2 = pyautogui.locateCenterOnScreen(button2)
	while check1 == None and check2 == None:
		check1 = pyautogui.locateCenterOnScreen(button1)
		check2 = pyautogui.locateCenterOnScreen(button2)
	if check1 == None:
		pyautogui.click(check2)
	else:
		pyautogui.click(check1)

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


if __name__ == '__main__':
	while True:
		# checkButtons(claim_fire, claim_fire2)
		# print('Claim - pressed!')
		# if checkCaptcha_fire() == 1:
		# 	continue
		# print('Captcha solved')
		# checkButton(minningHub_fire)
		# print('minningHub - pressed!')
		# checkButton(mine_fire)
		# print('Mine - pressed!')

		checkCaptcha_fire()
