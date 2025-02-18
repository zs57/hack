import os
import time
import random
import sys
import threading
import curses
import pyttsx3
import requests
from colorama import init, Fore
from pyfiglet import figlet_format
from rich.console import Console
from rich.text import Text

init(autoreset=True)
console = Console()
engine = pyttsx3.init()

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_hack():
    messages = [
        "[ACCESS GRANTED] Connecting to the dark web...",
        "[ERROR] System compromised! Attempting to regain control...",
        "[WARNING] Intrusion detected! Encrypting files...",
        "[SUCCESS] Bypassing firewall security...",
        "[FAILURE] Self-destruct initiated in 10 seconds..."
    ]
    for msg in messages:
        type_effect(Fore.RED + msg, 0.1)
        time.sleep(1)

def matrix_effect(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    col_vals = [random.randint(0, sh - 1) for _ in range(sw)]
    
    while True:
        stdscr.clear()
        for i, val in enumerate(col_vals):
            char = random.choice(chars)
            stdscr.addstr(val, i, char, curses.color_pair(1))
            col_vals[i] = (val + 1) % sh
        stdscr.refresh()
        time.sleep(0.1)

def chatbot():
    responses = {
        "hello": "Hello, mortal. Ready for the chaos?",
        "who are you": "I am the Chaos Terminal. Your digital nightmare.",
        "exit": "Escaping is futile... but I'll let you go."
    }
    type_effect(Fore.CYAN + "[AI] Chatbot activated. Type 'exit' to quit.")
    while True:
        user_input = input(Fore.YELLOW + "You: ")
        if user_input.lower() in responses:
            response = responses[user_input.lower()]
        else:
            response = "I don't understand your human words."
        type_effect(Fore.MAGENTA + "Bot: " + response)
        engine.say(response)
        engine.runAndWait()
        if user_input.lower() == "exit":
            break

def main():
    os.system("clear")
    console.print(Text(figlet_format("CHAOS TERMINAL"), style="bold red"))
    while True:
        cmd = input(Fore.YELLOW + "chaos> ")
        if cmd == "hack-mode":
            fake_hack()
        elif cmd == "matrix":
            curses.wrapper(matrix_effect)
        elif cmd == "chat":
            chatbot()
        elif cmd == "exit":
            type_effect(Fore.GREEN + "Goodbye, hacker!")
            break
        else:
            type_effect(Fore.RED + "Unknown command! Try 'hack-mode', 'matrix', 'chat', or 'exit'.")

if __name__ == "__main__":
    main()
