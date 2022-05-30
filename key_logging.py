from pynput.keyboard import Key, Listener
from time import time

start = 0

def measure_times(times):
    def on_press(key):
        global start
        start = time()

    def on_release(key):
        if len(times) == 10:
            return False
        else:
            finish = time()
            times.append(finish - start)

    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

    return times
