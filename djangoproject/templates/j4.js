function matchpass(){
    var pass1=document.giri.passone.value;
    var pass2=document.giri.passtwo.value;
    if(pass1==pass2){
        return true;
    }else{
        alert(" password must be same!!!")
        return false
    }
}