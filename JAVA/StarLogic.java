
public class StarLogic {
    public static void main(String[] args) {
        System.out.println("Oii");
//JAVA STRINGS METHODS 
        //method length()
String a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
System.out.println("The length of the a string is: " + a.length());

        //toUpperCase() and toLowerCase() methods
String b = "Hello World";
System.out.println(b.toUpperCase());   // Outputs "HELLO WORLD"
System.out.println(b.toLowerCase());   // Outputs "hello world"

        //indexOf() method 
String c = "Please locate where 'locate' occurs!";
System.out.println(c.indexOf("locate")); // Outputs 7

        // andddaaa charAt() method
String d = "Hello";
System.out.println(d.charAt(0));  // H
System.out.println(d.charAt(4));  // o

        //comparing strings 
String e = "Hello";
String f = "Hello";

String g = "Greetings";
String h = "Great things";

System.out.println(e.equals(f));  // true
System.out.println(g.equals(h));  // false

// JAVA MATH METHODS
        //Math.max(x,y)
Math.max(5, 10); 
        //Math.min(x,y)
Math.min(5, 10);
        //Math.sqrt(x)
Math.sqrt(64);
        //Math.abs(x)
Math.abs(-4.7); //returns o módulo 
        //Math.pow(x, y)
Math.pow(2, 8);  // 256.0 base = primeiro, expoente = segundo

        //rounding methods
        /*
        Math.round(x)   - rounds to the nearest integer
        Math.ceil(x)    - rounds up (returns the smallest integer greater than or equal to x)
        Math.floor(x)   - rounds down (returns the largest integer less than or equal to x)
        */
Math.round(4.6);  // 5
Math.ceil(4.1);   // 5.0
Math.floor(4.9);  // 4.0

        //Random Numbers
Math.random();// a number in range(0.0, 1.0) 
int randomNum = (int)(Math.random() * 101);  // 0 to 100
System.out.println(randomNum); // randon returns a double, thats why it need to be casted into a int 


//Java If ... Else
/*
syntaxes

        //if 
if (condition) {
  // block of code to be executed if the condition is true
}

        //if else
if (condition) {
  // block of code to be executed if the condition is true
} else {
  // block of code to be executed if the condition is false
}

    //if else if else 
if (condition1) {
  // block of code to be executed if condition1 is true
} else if (condition2) {
  // block of code to be executed if condition1 is false and condition2 is true
} else {
  // block of code to be executed if both conditions are false
}

//if else short handed 
         Java Short Hand If...Else (Ternary Operator)
     variable = (condition) ? expressionTrue :  expressionFalse;


     //nested if 

if (condition1) {
  // code to run if condition1 is true
  if (condition2) {
    // code to run if both condition1 and condition2 are true
  }
}

*/
// TERNARY OPERATOR 
//ex normal
int time = 20;
if (time < 18) {
  System.out.println("Good day.");
} else {
  System.out.println("Good evening.");
}
//ex shorthand 
int time1= 20;
String result = (time1 < 18) ? "Good day." : "Good evening.";
System.out.println(result);
// ternary can be nested, but it's optional and kinda confunsing 
int time3 = 22;
String message = (time3 < 12) ? "Good morning."
               : (time3 < 18) ? "Good afternoon."
               : "Good evening.";
System.out.println(message);

    // Java Switch
/*  syntax

switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}

*/
int day = 4;
switch (day) {
  case 6:
    System.out.println("Today is Saturday");
    break;
  case 7:
    System.out.println("Today is Sunday");
    break;
  default:
    System.out.println("Looking forward to the Weekend");
}
// Outputs "Looking forward to the Weekend"

//Java While Loop

/* syntax 
while (condition) {
  // code block to be executed
  //increasement 
}
 */
int i = 0;
while (i < 5) {
  System.out.println(i);
  i++;
}

//Java Do/While Loop
/*syntax 

do {
  // code block to be executed
}
while (condition);

THE DO WHILE IS A WHILE VARIATION WHERE THE CODE BLOCK IS EXECUTED ONCE

*/
int i2 = 0;
do {
  System.out.println(i2);
  i2++;
}
while (i2 < 5);


// FOR LOOP 
/* syntax 
for (statement 1; statement 2; statement 3) {
  // code block to be executed
}

*/
for (int i3 = 0; i3 < 5; i3++) {
  System.out.println(i);
}

//nested loops 
// Outer loop
for (int i4 = 1; i4 <= 2; i4++) {
  System.out.println("Outer: " + i); // Executes 2 times
  
  // Inner loop
  for (int j = 1; j <= 3; j++) {
    System.out.println(" Inner: " + j); // Executes 6 times (2 * 3)
  }
} 

//Java For Each Loop
/*
syntax 
for (type variableName : arrayName) {
  // code block to be executed
}
*/
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (String car : cars) {
  System.out.println(car);
}

int[] numbers = {10, 20, 30, 40};

for (int num : numbers) {
  System.out.println(num);
}
//The colon (:) is read as "in". So you can read the loop as: "for each variable in array".




/*
BREAK & CONTINUE:
break = stop the loop completely.
continue = skip this round, but keep looping.
*/

//Java Arrays
// type[] array = {a1, a2, a3 ... an}
int[] myNum = {10, 20, 30, 40};
    //accesing itens 
System.out.println(myNum[0]);
myNum[0] = 1;
System.out.println(myNum.length);

//
String[] cars2 = new String[4]; // size is 4

cars2[0] = "Volvo";
cars2[1] = "BMW";
cars2[2] = "Ford";
cars2[3] = "Mazda";

System.out.println(cars2[0]); // Outputs Volvo47



for (int i4 = 0; i4 < cars.length; i4++) {
  System.out.println(cars2[i]);
}

//Multidimensional Arrays
int[][] myNumbers = { {1, 4, 2}, {3, 6, 8} };
/*
Here, myNumbers has two arrays (two rows):

First row: {1, 4, 2}
Second row: {3, 6, 8}

*/
//acessing
System.out.println(myNumbers[1][2]); // Outputs 8
System.out.println(myNumbers[0][1]); // Outputs 4

myNumbers[1][2] = 9;

int[][] myNumbers2 = { {1, 4, 2}, {3, 6, 8, 5, 2} };
System.out.println("Rows: " + myNumbers2.length);             // 2
System.out.println("Cols in row 0: " + myNumbers2[0].length); // 3
System.out.println("Cols in row 1: " + myNumbers2[1].length); // 5

//loopin thru a multimensional array
for (int row = 0; row < myNumbers2.length; row++) {
  for (int col = 0; col < myNumbers2[row].length; col++) {
    System.out.println("myNumbers2[" + row + "][" + col + "] = " + myNumbers2[row][col]);
  }
}


for (int[] row : myNumbers) {
  for (int num : row) {
    System.out.println(num);
  }
}



    }
}; 

/*
Java data types: 

byte	    Stores whole numbers from -128 to 127
short	    Stores whole numbers from -32,768 to 32,767
int	        Stores whole numbers from -2,147,483,648 to 2,147,483,647
long	    Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
float	    Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
double	    Stores fractional numbers. Sufficient for storing 15 to 16 decimal digits
boolean	    Stores true or false values
char	    Stores a single character/letter or ASCII values


*/

/*
Arithmetic Operators

+	Addition	    Adds together two values	                x + y	
-	Subtraction	    Subtracts one value from another	        x - y	
*	Multiplication	Multiplies two values	                    x * y	
/	Division	    Divides one value by another	            x / y	
%	Modulus	        Returns the division remainder	            x % y	
++	Increment	    Increases the value of a variable by 1	     ++x	
--	Decrement	    Decreases the value of a variable by 1	     --x


Some Assignment Operators
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3

Logical Operators
&& 	    Logical and	Returns true if both statements are true	                x < 5 &&  x < 10	
|| 	    Logical or	Returns true if one of the statements is true	            x < 5 || x < 4	
!	    Logical not	Reverse the result, returns false if the result is true	    !(x < 5 && x < 10)
 */

/*
escape characters

Escape character	 Result	    Description
\'	                    '	     Single quote
\"                  	"	     Double quote
\\	                    \	     Backslash

*/


