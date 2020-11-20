function changeStyle() {
    // grab element ID, get element by id
    var text = document.getElementById ("para1").style.color = "Blue"; //alter text, style paragraph attribute
        //style is object, color is property
    // document is the largest object in html

}



function changeStyle2(){
    //grab element by tags
    var paragraph = document.getElementsByTagName("p");
    // always use "" to specify element name

    var changeParaText = paragraph[1].style.fontStyle = "italic";
    //change the second paragraph

    var changeParaText = paragraph[0].style.fontStyle = "italic";
    var changeParaText = paragraph[2].style.fontStyle = "italic";
    var changeParaText = paragraph[3].style.fontStyle = "italic";
    var changeParaText = paragraph[4].style.fontStyle = "italic";

}



function changeAll() {
    var paragraph = document.getElementsByTagName("p");

    for (var _ = 0; _ < paragraph.length; _++) {

        paragraph[_].style.backgroundColor = "grey";

    }
}



function changeClass() {

    var para = document.getElementsByClassName("para");

    var changeTedxt = para[0].style.color = 'grey';
}