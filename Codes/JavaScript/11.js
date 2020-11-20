 /* create a single element =============================*/
function newParagraph() {

    //just create paragraph without headings

    var element = document.createElement("p");
    
    var main = document.getElementById("main");
    
    main.appendChild(element); // append additional elemnet as <p>
    
    var text = document.createTextNode("The Battle of Salamis was \
    fought between an alliance of Greek cities and the Persian \
    Empire in 480 BC.  The Greeks decisively defeated the Persian \
    navy.");
    
    element.appendChild(text); // attach text node to paragraph node 

    // these are three steps process
    
}

/* create multiple element ================================*/
function newHeader() {

    //this part is for creating heading
    var elementH = document.createElement("h2");

    //create main to hold and append elements to it
    var main = document.getElementById("main");

    //append to child to the div
    main.appendChild(elementH);

    //text node for heading
    var textH = document.createTextNode("The Battle of Salamis");

    //attach text node to heading node
    elementH.appendChild(textH);



    //this part is for creating paragraph
    var element = document.createElement("p");

    //attach to div
    main.appendChild(element);

    //create text
    var text = document.createTextNode("The Battle of Salamis was \
    fought between an alliance of Greek cities and the Persian \
    Empire in 480 BC.  The Greeks decisively defeated the Persian \
    navy.");

    //append
    element.appendChild(text);

}


/* remove multiple element ============================*/
function removeHeader() {
    //var elementH = document.getElementsByTagName("h2")[2]; will also work fine
    var elementH = document.getElementsByTagName("h2")[document.getElementsByTagName("h2").length-1];

    //get parent node of heading node so that we can delete
    //everthing under the heading, which is div here
    var parent = elementH.parentNode;

    parent.removeChild(elementH);


    //delete paragraph
    var elementP = document.getElementsByTagName("p")[document.getElementsByTagName("p").length-1];

    //since the parent object is already created, we just
    //need to reuse them here
    parent.removeChild(elementP);

}

/* create element and give them new style ==================*/
function newHeaderStyle() {

    var elementH = document.createElement("h2");

    var main = document.getElementById("main");

    main.appendChild(elementH);

    var textH = document.createTextNode("The Battle of Salamis");

    elementH.appendChild(textH);

    var element = document.createElement("p");//we will reuse that

    main.appendChild(element);

    var text = document.createTextNode("The Battle of Salamis was \
    fought between an alliance of Greek cities and the Persian \
    Empire in 480 BC.  The Greeks decisively defeated the Persian \
    navy.");

    element.appendChild(text);

    //add style

    //give us attribute node
    var pAttribute = document.createAttribute("id");//we can create a source attribute/href attribute/lang attribute, just call it by name
    pAttribute.value = "test";//assign value to the id in CSS
    element.setAttributeNode(pAttribute);//reuse element oblect
}