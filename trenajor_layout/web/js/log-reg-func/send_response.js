eel.expose(login_return)
function login_return(status){
    if (status == "success"){
        location.href = "ссылка на главную"
    }
    if (status == "success"){
        //Вывод ошибки
    }
}