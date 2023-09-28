import keyboard, pyautogui, threading, datetime

def lprint(s):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {s}")

clickerActive = False

def hotkeyCom():
    global clickerActive
    clickerActive = not clickerActive
    if clickerActive:
        lprint("Started")
    else:
        lprint("Stopped")

def clicker():
    global clickerActive
    while True:
        if clickerActive:
            pyautogui.click(clicks=10)

keyboard.add_hotkey('f6', hotkeyCom)
print("AUTO CLICKER")

t = threading.Thread(target=clicker, daemon=True)
t.start()
keyboard.wait()