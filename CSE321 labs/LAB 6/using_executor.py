from concurrent.futures import ThreadPoolExecutor
import time
import random

def study(fname, lname):
    for i in range(10):
        print(f"{fname} {lname} studying {i}....")
        time.sleep(random.random())

def listen_to_music(fname, lname):
    for i in range(10):
        print(f"{fname} {lname} listening to music {i}.....")
        time.sleep(random.random())

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        arguments = [["A", "C"], ["B", "D"]]
        # executor.submit(study, *arguments)
        # executor.submit(listen_to_music, *arguments)
        executor.map(study, *arguments)
        executor.map(listen_to_music, *arguments)