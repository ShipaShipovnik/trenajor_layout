async function responseTask() {
    const message = await eel.response_task()(); // Вызов функции Python
    if (message == []) {
        alert('Произошла ошибка');
        location.href = "./levels-main.html";
    } else {
        //let subjHeader = document.getElementById('name_subj');
        //subjHeader.innerHTML = message;
        console.log(message);
    }
    //console.log(message);
}
responseTask();
console.log('xui')