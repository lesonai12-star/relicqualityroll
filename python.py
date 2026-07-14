import time
import pyautogui
X = 395
Y = 421
U = 975
I = 600
C = (68, 14, 4)
CL = 0.05	
while True:
    c = pyautogui.pixel(X, Y)
    if c == C:
        pyautogui.click(U, I)
        time.sleep(CL)
    time.sleep(0.001)