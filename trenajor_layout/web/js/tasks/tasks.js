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

function currentTask(elId) {
    if (elId == 0) {
        $('#level-' + elId).addClass('level-current');
    }else{
        $('#level-' + elId+1).addClass('level-current');
    }
    
}

async function checkTrue() {
    try {
        const true_list = await eel.check_true()();
        if (true_list != []) {
            let elemId = true_list[true_list.length - 1]
            true_list.forEach(elementId => {
                $('#level-' + elementId).addClass('level-done');
                
            });
            currentTask(elemId)
        } else {
            currentTask(0)
            return
        }
    } catch (error) {
        console.error('Error in checkTrue:', error);
        return
    }

}


$(document).ready(function () {
    checkTrue();
    $('.level-circle').click(function () {
        var nameValue = $(this).attr('name');
        eel.take_t(nameValue);
        location.href = "./TaskAsk.html";
    });
});
