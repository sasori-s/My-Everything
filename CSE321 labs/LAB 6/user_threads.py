import time
import random
import threading
def study(fname, lname):
    for i in range(10):
        print(f'{fname} {lname} studying...')
        time.sleep(random.random())

def listen_to_music(fname, lname):
    for i in range(10):
        print(f'{fname} {lname} listening to music...')
        time.sleep(random.random())


if __name__ == '__main__':
    st = threading.Thread(target=study, args=('A', 'C'))
    mt = threading.Thread(target=listen_to_music, args=('B', 'C') )
    st.start()
    mt.start()