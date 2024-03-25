import eel
from web.models.login import login_user



eel.init("web")

@eel.expose
def log_g(username, password):
    msg = login_user(username, password)
    eel.login_return(str(msg))


eel.start("./pages_content/login.html", size=(1920, 1080))