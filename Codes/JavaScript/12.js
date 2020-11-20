function refresh(){
    location.reload(true)
//false - Default. Reloads the current page from the cache.
// true - Reloads the current page from the server
}


function changeChildText(){

    var parent = document.getElementById("main");

    var child = parent.childNodes[3];
    //however blank space is treated also as a child node
    //so you know, [0] and [2] doesn't work

    child.style.color = 'blue';

    var child1 = parent.firstElementChild;
    //the first child element, auto-ignore blank space

    child1.style.color = 'red';


}



function changeParentText(){

    var child = document.getElementById('p3');

    var parent = child.parentNode;
    //get parent element and change all the style
    //of its children
    var parent2 = child.parentElement;//work the same

    parent.style.color='green';
}



function changeSiblingText(){

    var para2 = document.getElementById('p4');
    var sibling = para2.nextElementSibling;
    sibling.style.color='yellow';


    var siblingL = para2.previousElementSibling;
    //use previousElementSibling instead of
    //previousSibling, is to prevent refer to white space
    siblingL.style.color='white';

}