import threading
import subprocess
import pyautogui
import webbrowser
import time
import random
import string
import keyboard  # pip install keyboard

running = True  # Global flag


def generate_random_query():
    length = random.randint(3, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def launch_edge():
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    # This is usually "Profile 1", "Profile 2", etc.
    profile_name = input("Enter the profile name (e.g., 'Profile 1'): ")
    if not profile_name:
        profile_name = "Default"
    start_url = "https://www.bing.com"

    subprocess.Popen(
        [edge_path, f"--profile-directory={profile_name}", start_url])


def do_search():
    query = generate_random_query()
    print(f"🔍 Searching for: {query}")
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    for char in query:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.2))

    # Press backspace to remove one character
    pyautogui.press('backspace')
    pyautogui.press('enter')
    time.sleep(1.5)


def stop_running():
    global running
    print("🛑 ESC pressed! Terminating search loop...")
    running = False


def start_search_loop():
    launch_edge()
    time.sleep(5)
    keyboard.add_hotkey('esc', stop_running)

    while running:
        do_search()
        time.sleep(random.uniform(4, 8))

    print("💤 Rewards Ninja has logged off...")


threading.Thread(target=start_search_loop).start()
