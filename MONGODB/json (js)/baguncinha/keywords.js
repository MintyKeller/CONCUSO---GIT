/*
JSON.parse()  - TO RECEIVE 
A common use of JSON is to exchange data to/from a web server.

When receiving data from a web server, the data is always a string.

Parse the data with JSON.parse(), and the data becomes a JavaScript object.

*/

//Imagine we received this text from a web server:
//'{"name":"John", "age":30, "city":"New York"}'
const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
//IT RETURNS AN OBJECT 

//Array as JSON
const text = '["Ford", "BMW", "Audi", "Fiat"]';
const myArr = JSON.parse(text);
//it RETURNS an ARRAY 

/*
JSON.stringify() - TO SEND 
A common use of JSON is to exchange data to/from a web server.

When sending data to a web server, the data has to be a string.

You can convert any JavaScript datatype into a string with JSON.stringify().
*/

const obj3 = {name: "John", age: 30, city: "New York"};
const myJSON = JSON.stringify(obj);
//myJSON is now a string, and ready to be sent to a server:

//Stringify a JavaScript Array
const arr = ["John", "Peter", "Sally", "Jane"];
const myJSONArr = JSON.stringify(arr);

/*
Storing Data
When storing data, the data has to be a certain format,
 and regardless of where you choose to store it, 
 text is always one of the legal formats.

JSON makes it possible to store JavaScript objects as text.

*/
// Storing data:
/*
const myObj2 = {name: "John", age: 31, city: "New York"};
const myJSON2 = JSON.stringify(myObj2);
localStorage.setItem("testJSON", myJSON2);

// Retrieving data:
let text2 = localStorage.getItem("testJSON");
let obj2 = JSON.parse(text);
document.getElementById("demo").innerHTML = obj2.name;

html/localstorage.html
*/

/*
It is a common mistake to call a JSON object literal "a JSON object".

JSON cannot be an object. JSON is a string format.

The data is only JSON when it is in a string format.
When it is converted to a JavaScript variable, it becomes a JavaScript object.
*/

myJSON4 = '{"name":"John", "age":30, "car":null}';
myObj4 = JSON.parse(myJSON4);

x = myObj4.name; //two diferent ways of accesing info
x = myObj4["age"];
//You can loop through object properties with a for-in loop:
let text = "";
for (const x in myObj) {
  text += x + ", ";
}
//In a for-in loop, use the bracket notation to access the property values:
let text = "";
for (const x in myObj) {
  text += myObj[x] + ", ";
}

//ARRAYS 

myJSON5 = '["Ford", "BMW", "Fiat"]';
myArray5 = JSON.parse(myJSON5);
y = myArray5[0];

a = {
"name":"John",
"age":30,
"cars":["Ford", "BMW", "Fiat"]
}; 

w = a.cars[0];

//Looping Through an Array
    //with for in
for (let i in a.cars) {
  x += a.cars[0];;
}
    //wit for 
for (let i = 0; i < a.cars.length; i++) {
  x += a.cars[i];
}

//If you have data stored in a JavaScript object, 
// you can convert the object into JSON, and send it to a server:
const myObj6 = {name: "John", age: 31, city: "New York"};
const myJSON6 = JSON.stringify(myObj6);
window.location = "demo_json.php?x=" + myJSON6;

//If you receive data in JSON format, 
// you can easily convert it into a JavaScript object:
const myJSON7 = '{"name":"John", "age":31, "city":"New York"}';
const myObj7 = JSON.parse(myJSON);
document.getElementById("demo").innerHTML = myObj7.name;
