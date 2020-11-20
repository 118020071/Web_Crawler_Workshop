function validateTextbox() {

    var nameBox = document.getElementById("name");
    var addressBox = document.getElementById("address");

    //if input is null
    if (nameBox.value == "" || addressBox.value == "" ) {
        alert("Please fill in box, which field is marked red")



        //focus method will help highlight (error)text box border
        nameBox.focus();//highlight box
        nameBox.style.border = "solid 3px red";//more style than just focus() method





        return false;
        //stop the form being submitted, aka stop onSubmit action
    } else if (addressBox.value.length < 5) {
        alert("Invalid address field");

        return false;
    }
}



