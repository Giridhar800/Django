function validationform(){
    var name=document.myform.name.value;
    var password=document.myform.pass.value;
    if (name==null || name==""){
        alert("Name can not be blank");
        return false;
    }else if(password.length<6){
        alert("password must be morethan 6 leters");
        return false;
    }

}