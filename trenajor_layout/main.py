from __future__ import print_function
import eel
from db.models import login_user, register_user


#import bottle_websocket as wbs
eel.init("web")

@eel.expose
def log_g(username, password):
    msg = login_user(username, password)
    eel.login_return(str(msg))
"""
@eel.expose
def get_user_online():
    get_user = login_session()
    print(get_user)
    eel.get_user(str(get_user))
"""
eel.start("./pages_content/login.html", size=(640, 480))