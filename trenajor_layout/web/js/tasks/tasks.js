async function responseSubject() {
    const message = await eel.response_subject()(); // Вызов функции Python
    if (message == "") {
        alert('Произошла ошибка');
        location.href = "./class-choose.html";
    } else {
        let subjHeader = document.getElementById('name_subj');
        subjHeader.innerHTML = message;
    }
    //console.log(message);
}
responseSubject();



$(document).ready(function () {
    $('.level-circle').click(function () {
        var nameValue = $(this).attr('name');
        //eel.take_t(nameValue);
        location.href = "./TaskAsk.html";
        // Здесь вы можете использовать значение nameValue по вашему усмотрению
    });
});
