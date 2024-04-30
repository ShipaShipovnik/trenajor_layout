//var username = $('#username').val();
//eel.take_t($('#username'))

$(document).ready(async function () {
    $('.level-circle').click(function () {
        var nameValue = $(this).attr('name');
        //eel.take_t(nameValue);
        location.href = "./TaskAsk.html"
        // Здесь вы можете использовать значение nameValue по вашему усмотрению
    });
});
