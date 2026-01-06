import os
import argparse
import pyautogui
import time

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="absolute path to store screenshot.", default=r"./Capture Screenshots At Regular Intervals of Time/images")
parser.add_argument("-t", "--type", help="h (in hour) or m (in minutes) or s (in seconds)", default="h")
parser.add_argument("-f", "--frequency", help="frequency for taking screenshot per h/m/s.", default=1, type=int)
args = parser.parse_args()

sec = 0.0
if args.type == "h":
    sec = 60 * 60 / args.frequency
elif args.type == "m":
    sec = 60 / args.frequency
elif args.type == "s":
    sec = 1 / args.frequency

if sec < 1.0:
    sec = 1.0

os.makedirs(args.path, exist_ok=True)

try:
    while True:
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        file = current_time + ".jpg"
        image_path = os.path.join(args.path, file)
        pyautogui.screenshot(image_path)
        print(f"{file} saved successfully at {image_path}.\n")
        time.sleep(sec)
except KeyboardInterrupt:
    print("End of script by user interrupt")
