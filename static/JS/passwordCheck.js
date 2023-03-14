password1 = document.querySelector('#id_password1');
password2 = document.querySelector('#id_password2');

password1.onkeyup = function(){

    if (password1.value.length < 8 || password1.value.trim() == ''){
        password1.style.borderColor = 'rgb(192, 0, 0)';
    }
    else{
        password1.style.borderColor = 'green';
    }

}

password2.onkeyup = function(){

    if(password2.value != password1.value || password2.value.trim() == ''){
        password2.style.borderColor = 'rgb(192, 0, 0)';
    }
    else{
        password2.style.borderColor = 'green';
    }

}