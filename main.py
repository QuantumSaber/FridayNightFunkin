import pyautogui
from directkeys import W, S, A, D, PressKey, ReleaseKey
import time
import cv2


time.sleep(10)
while True:
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
	if pyautogui.pixel(551, 202) != [135, 163, 173]:
		PressKey(A)
	elif pyautogui.pixel(551, 202) == [135, 163, 173]:
		ReleaseKey(A)


	elif pyautogui.pixel(632, 228) != [135, 163, 173]:
		PressKey(S)
	elif pyautogui.pixel(632, 228) == [135, 163, 173]:
		ReleaseKey(S)


	elif pyautogui.pixel(708, 212) != [135, 163, 173]:
		PressKey(W)
	elif pyautogui.pixel(708, 212) == [135, 163, 173]:
		ReleaseKey(W)


	elif pyautogui.pixel(796, 222) != [135, 163, 173]:
		PressKey(D)
	elif pyautogui.pixel(796, 222) == [135, 163, 173]:
		ReleaseKey(D)
