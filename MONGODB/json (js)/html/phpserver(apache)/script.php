<?php
/*
The PHP File
PHP has some built-in functions to handle JSON.

Objects in PHP can be converted 
into JSON by using the PHP function json_encode():
*/
$myObj = new stdClass();
$myObj->name = "John";
$myObj->age = 30;
$myObj->city = "New York";

$myJSON = json_encode($myObj);
echo "<h3>JSON gerado a partir de um Objeto:</h3>";
echo $myJSON;

/*
PHP Array
Arrays in PHP will also be converted into JSON
 when using the PHP function json_encode():
*/
$myArr = array("John", "Mary", "Peter", "Sally");

$myJSON2 = json_encode($myArr);
echo "<h3>JSON gerado a partir de um Array:</h3>";
echo $myJSON2;
?>