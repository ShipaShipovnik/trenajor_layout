from __future__ import print_function
import eel
from db.models import login_user, register_user, take_task

#https://github.com/ShipaShipovnik/trenajor_layout 

#import bottle_websocket as wbs
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
def take_t(pk):
    msg = take_task(pk)
    eel.task_response(str(msg))

eel.start("./pages_content/login.html", size=(640, 480))