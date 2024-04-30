eel.expose(login_return)
function login_return(status){
    if (status == "SUCCES"){
        location.href = "./class-choose.html"
    }
    if (status == "FAILED"){
        $('#login_txt').text("Неверный логин или пароль")
    }
    if (status == "FAIL"){
        console.log("Ошибка")
    }
}