/*

object::

*/



/*
//describe property instead of action
var orc = {
    color: "red";  //name:value
    height: 12;
    weight: 180
}


usage::

orc.color;

*/



/*
// property that describe actions
var orc = {
    yell : function () { //function inside object is called method
        document.write("statements to act")
    }
}


ordinary function is :: function name(){}

usage::

orc.yell();

*/


//an example
var orc = {
    hair : "brown",  // string object
    age: 63, // math object
    height: 140,
    eat: function(){
        document.write("oh shit");
    }
}

var newAge = orc.age + 10;

document.write(orc.age);

if (orc.height <= 170) {
    orc.eat();
} else {
    orc.height = null;
    orc.living = "dead";
    delete orc.hair;
    orc.IQ;
}

document.write(orc.height);
document.write(orc.living);
document.write(orc.hair);
document.write(orc.IQ);







// string object

var s1 = "<br>hello<br>";

document.write(s1.toUpperCase());
document.write(s1.length);
document.write(s1.charAt(4));
document.write(s1.replace("lo",'nq'));
document.write(s1.bold());
document.write(s1.italics());

s1 = s1.toUpperCase(); // method
s1.length; // property
//length is # of letter +1, since JS throws extra unit at the end of 
// the string
s4 = s1.charAt(4); // "o"
s1 = s1.replace("lo",'nq');
s1 = s1.bold();
s1 = s1.italics();//italicize the string







//math object

var  number = 4.4 ;
var newNumber = 26 + Math.round(number);

document.write(newNumber);
document.write(Math.ceil(number));
document.write(Math.sqrt(number))






//date object

var toDate = new Date();//new keyword can create an object ,
// it always us copy existing pbject and use it
// Date is reference object, toDate is instance, () is constructor
document.write('<br>');
document.write(toDate);
//convert it to readable string
var strDate = toDate.toDateString();
document.write('<br>');
document.write(strDate);
toDate.setYear(2017);
document.write('<br>');
document.write(toDate);