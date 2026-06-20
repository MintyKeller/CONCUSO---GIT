// javascript objetcs 
/*
What are JavaScript Objects?
Objects are variables that can store both values and functions.

Values are stored as key:value pairs called properties.

Functions are stored as key:function() pairs called methods.
*/

// CODIGO NAO RODAVEL KKKKK 

const car = {
  type: "Fiat",
  model: "500",
  color: "white"
};

//You can also create an empty object, and add the properties later:

// Create an Object
const person = {};

// Add Properties
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";

/*
Object Properties
You can access object properties in two ways:

Dot notation
Bracket notation
*/

//dot notation 
//objectName.propertyName
person.firstName;
car.type; 


//Bracket Notation
//objectName["propertyName"]
person["firstName"];
car["type"]; 


//methods 
/*
Objects can also have methods.

Object methods are actions that can be performed on objects.

Object methods are function definitions stored as property values:
*/ 
const person = {
  firstName: "John",
  lastName : "Doe",
  age      : 50,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

delete person.age;
/*
The delete keyword deletes both the value and the property.

After deleting, the property is removed. Accessing it will return undefined.
*/ 

let result = ("firstName" in person); //checkin if it exists 

//nested objects 
myObj = {
  name:"John",
  age:30,
  myCars: {
    car1:"Ford",
    car2:"BMW",
    car3:"Fiat"
  }
}

//accesing 
myObj.myCars.car2;

//  THIS keyword
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  getId: function() {
    return this.id;
  },
    fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};

let number = person.getId();

/*
In the example above, this refers to the person object.

this.firstName means the firstName property of the person object.

this.lastName means the lastName property of the person object.

this.id means the id property of the person object.
*/
//to call afunction to execute, must use (), if not, you call the function itself, as here we delete it
delete person.fullName;

// Assign person.name to a function, and then here we add it to the object 
person.fullName = function () {
  return this.firstName + " " + this.lastName;
};

const person1 = {
  name: "John",
  hello: function() {
    return "Hello " + this.name;
  }
};

const person2 = {
  name: "Anna",
  hello: function() {
    return "Hello " + this.name;
  }
};


/*
Summary
    -In an object method, this refers to the object
    -this lets methods access object properties
    -Used alone, this refers to the global object
*/

//Displaying Object Properties
    //string
// Create an Object
const person = {
  name: "John",
  age: 30,
  city: "New York"
};

// Add Properties
let text = person.name + "," + person.age + "," + person.city;

//For .. In Loop
// Create an Object
const person = {
  name: "John",
  age: 30,
  city: "New York"
};

// Build a Text
let text = "";
for (let x in person) {
  text += person[x] + " ";
};

//Object.values()

// Create an Object
const person = {
  name: "John",
  age: 30,
  city: "New York"
};

// Create an Array
const myArray = Object.values(person);

// Stringify the Array
let text = myArray.toString();

//Object.entries()
const fruits = {Bananas:300, Oranges:200, Apples:500};

let text = "";
for (let [fruit, value] of Object.entries(fruits)) {
  text += fruit + ": " + value + "<br>";
}

/*
Using JSON.stringify()
JavaScript objects can be converted to a string with JSON method JSON.stringify().

JSON.stringify() is included in JavaScript and supported in all browsers.

The result will be a string written in JSON notation:

{"name":"John","age":50,"city":"New York"}
*/
// Create an Object
const person = {
  name: "John",
  age: 30,
  city: "New York"
};

// Stringify Object
let text = JSON.stringify(person);