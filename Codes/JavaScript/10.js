/* on mouse over event =================================================*/


// func on change text

function changeBackground() {
    
    var text = document.getElementById("para").style.backgroundColor="red";

}

function backNormal() {

    var text = document.getElementById("para").style.backgroundColor = "";
}


// func on change pic

function oldPic() {
    
    document.getElementById("img1").src = "truth.jpg";

}

function newPic() {
    
    document.getElementById("img1").src = "trump.png";
    
}