def login_user(username, password):
    print(username)
    print(password)
    try:
        msg = "SUCCES"
        return msg
    
    except Exception as Error:
        print(Error)
        msg = "FAILED"
        return msg