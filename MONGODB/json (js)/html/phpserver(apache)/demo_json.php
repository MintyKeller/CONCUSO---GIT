<?php
// Verifica se o valor 'x' foi enviado na URL
if (isset($_GET['x'])) {
    
    // 1. Pega a string JSON que veio do JavaScript
    $meuJSON = $_GET['x'];
    
    // 2. Converte o JSON em um Objeto PHP (para podermos acessar os dados)
    $obj = json_decode($meuJSON);
    
    // 3. Imprime na tela 
    echo "demo_json.php:<br><br>";
    echo $obj->name . " from " . $obj->city . " is " . $obj->age;
    
}
?>