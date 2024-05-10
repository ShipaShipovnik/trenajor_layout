from __future__ import print_function
import eel
from db.models import login_user, register_user, take_task

#https://github.com/ShipaShipovnik/trenajor_layout 

#import bottle_websocket as wbs

store = ''
task = []

eel.init("web")

@eel.expose
def log_g(username, password):
    msg = login_user(username, password)
    eel.login_return(str(msg))

@eel.expose
def reg_g(username, password):
    msg = register_user(username, password)
    eel.login_return(str(msg))

@eel.expose
def choose_subject(subject):
    global store
    store = subject
    #eel.subject_qw(str(subject))

@eel.expose
def response_subject():
    return store

@eel.expose
def take_t(pk):
    global task
    msg = take_task(pk)
    task = msg
    print(msg)
    print(task)

@eel.expose
def response_task():
    return task

eel.start("./pages_content/login.html", size=(1920, 1080))