function change2() {

    //add confirmation box
    //diff than alert box, it has concel button
    var confirmation = confirm("These chnages are final, not reverted");

    if (confirmation == false){
        return null//so we don't need to put everything down here to if statement :)
    }


    var p = document.getElementsByClassName("p2");

    var p1 = p[0].innerHTML;
    var p2 = p[1].innerHTML;

    var p3 = p[2].innerHTML = p1+p2;

    var p1 = p[0].innerHTML = "";
    var p2 = p[1].innerHTML = "";

    document.getElementById("buttonCombine").style.visibility = 'hidden';
}