import pyautogui as pyauto
import time
pyauto.PAUSE= 2
pyauto.alert("voce esta prestes a abrir o bloco de notas")

#abrir blocos de notas
pyauto.hotkey("win","r")
pyauto.write("notepad")
pyauto.press("enter")