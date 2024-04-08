//get_data_from_reg.js

function valid(pas, pass){
    if (pas==pass){
        eel.reg_g(
            $('#username').val(),
            pas
        )
    }
    else{
        alert('Пароли не совпадают!')
    }
    
}

function main(){
    valid($('#pass_1').val(), $('#pass_2').val())
}

$("#btn_sign_up").click(function(){
    main()
})