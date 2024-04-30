eel.expose(take_t)
function take_t(data){
    
    if (data == "FAILED"){
        $('#login_txt').text("Неверный логин или пароль")
    }
    
}