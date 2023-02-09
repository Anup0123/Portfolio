function validation(){
    let username= document.getElementById("uname").value;
    let password=document.getElementById("pass").value;
    if(username==""){
        alert("Username must be entered");
        return false
    }else if(password==""){
        alert("Password must be entered");
        return false
    }else if(password.length<5){
        alert("Password must be of aleast 5 characters");
        return false
    }else{
        alert("login success");
        return true
    }
}



document.querySelector('.menubar').addEventListener("click", () =>{
    document.querySelector('.sidebar').classList.toggle('toggle');
});