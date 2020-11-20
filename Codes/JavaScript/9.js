

// replace text
function changeStyle() {

    var para = document.getElementsByClassName("para");

    var changeText = para[0].innerHTML = "New text 1";
    var changeText = para[1].innerHTML = "New text 2";
}




//combine text
function change2() {



    //these are orginal code, but if you click the button twice, it will delete the combinded message

    /*
    // combine two paragraph together to form third one and delete them
    var para = document.getElementsByClassName("p2");

    var firstp = para[0].innerHTML;
    var secondp = para[1].innerHTML;

    var addthem = para[2].innerHTML = firstp+secondp;//add two paragraph together
    var firstp = para[0].innerHTML = "";//get rid of first line
    var secondp = para[1].innerHTML = "";//get rid of second line

    */

    //now we wanna debug that

    //first way is to hide the button after being clicked
    var para = document.getElementsByClassName("p2");

    var firstp = para[0].innerHTML;
    var secondp = para[1].innerHTML;

    var addthem = para[2].innerHTML = firstp+secondp;
    var firstp = para[0].innerHTML = "";
    var secondp = para[1].innerHTML = "";

    document.getElementById("buttonCombine").style.visibility = "hidden";//get rid of the button
    //but we need to warn the user that the combine action cannot be reverted since the button will disapper, so we need a comformation textbox, which is the content of 14.html
    


}


function changePic() {

    var image = document.getElementById("image1").src = "Penguin.jpeg";
    image.height = '100';
    image.width = '100';
    
}