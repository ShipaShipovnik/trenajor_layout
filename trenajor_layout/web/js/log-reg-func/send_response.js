eel.expose(login_return)
function login_return(status){
    if (status == "SUCCES"){
        location.href = "./userprofule.html"
    }
    if (status == "FAILED"){
        $('#login_txt').text("Неверный логин или пароль")
    }
}