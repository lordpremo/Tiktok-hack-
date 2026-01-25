import sys, time, random, os
from colorama import Fore, Style, init

init(autoreset=True)

quotes = [
    "Power belongs to LORD PREMO",
    "No system is safe",
    "Matrix is under my control",
    "Fear the name LORD PREMO",
    "Digital empire rising..."
]

def ascii_art():
    art = r"""
 _                     _   ____                      
| |    ___   ___  _ __| | |  _ \ _ __ ___   ___  ___ 
| |   / _ \ / _ \| '__| | | |_) | '__/ _ \ / _ \/ __|
| |__| (_) | (_) | |  | | |  __/| | | (_) |  __/\__ \
|_____\___/ \___/|_|  |_| |_|   |_|  \___/ \___||___/
    """
    print(Fore.RED + Style.BRIGHT + art)

def matrix_rain(duration=5, width=80):
    start = time.time()
    while time.time() - start < duration:
        line = "".join(random.choice("01ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(width))
        print(Fore.GREEN + line)
        time.sleep(0.05)

def progress_bar(task, length=30, delay=0.1):
    print(Fore.YELLOW + f"{task}")
    for i in range(length+1):
        bar = "[" + "#"*i + "-"*(length-i) + "]"
        percent = int((i/length)*100)
        print(Fore.GREEN + f"\r{bar} {percent}%", end="")
        time.sleep(delay)
    print("\n")
    print(Fore.CYAN + random.choice(quotes))

def hack(target):
    os.system("clear")
    ascii_art()
    print(Fore.GREEN + Style.BRIGHT + "\n" + "="*60)
    print(Fore.RED + Style.BRIGHT + "          LORD PREMO TIKTOK HACK SYSTEM")
    print(Fore.GREEN + Style.BRIGHT + "="*60 + "\n")
    time.sleep(2)

    matrix_rain(duration=6)
    progress_bar("Connecting to TikTok servers...")
    matrix_rain(duration=4)
    progress_bar("Bypassing security...")
    matrix_rain(duration=4)
    progress_bar(f"Hacking account: {target}")
    matrix_rain(duration=4)
    progress_bar("Extracting credentials...")

    print(Fore.GREEN + f"\n>>> SUCCESS! Account hacked by LORD PREMO: {target}")
    print(Fore.MAGENTA + ">>> Passwords found:\n")
    for i in range(5):
        password = target + str(random.randint(1000,9999))
        print(Fore.WHITE + password)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hack.py <target_name>")
    else:
        hack(sys.argv[1])
