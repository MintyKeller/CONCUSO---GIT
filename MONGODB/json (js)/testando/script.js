//pegando  o arquivo json e transformando ele num objeto pra mexer aqui
const db = require('./testing.json'); 


// OPERAÇÃO 1: VER (Acessar direto por posição)
//pegando o primeiro artista 
const primeiroArtista = db.artistas[0];
console.log("Primeiro artista da lista:", primeiroArtista.nome); //vai printar joão manô

// OPERAÇÃO 2: PROCURAR (O famoso find)
const artistaCinco = db.artistas.find(a => a.id === 5);
console.log("Quem é o artista com ID 5?:", artistaCinco.nome); //vai printar coldplay

// OPERAÇÃO 3: ADICIONAR (Equivale ao insert/push)
// Criando um artista novo na memória
/*const novoArtista = { 
    id: 13, 
    email: "paralamas@example.com", 
    nome: "Os Paralamas do Sucesso", 
    about: "Uma das bandas mais importantes do rock brasileiro, conhecida por misturar rock com ska e reggae em hits que atravessam gerações.", 
    foto_de_perfil: "fotoParalamasDoSucesso.jpg" 
};
// .push() coloca ele no final da lista de artistas
db.artistas.push(novoArtista);

console.log("Total de artistas agora:", db.artistas.length);
*/

const fs = require('fs'); 

console.log("Adicionando artista...");

// 2. Criamos o Paralamas completo
const novoArtista = { 
    id: 13, 
    email: "paralamas@example.com", 
    nome: "Os Paralamas do Sucesso", 
    about: "Uma das bandas mais importantes do rock brasileiro...", 
    foto_de_perfil: "fotoParalamasDoSucesso.jpg" 
};

// 3. Adicionamos na memória (RAM)
db.artistas.push(novoArtista);

// 4. A MÁGICA: Salvar de verdade no arquivo testing.json (Disco)
// O JSON.stringify transforma o objeto de volta em texto para o arquivo aceitar
fs.writeFileSync('./testing.json', JSON.stringify(db, null, 2));

console.log("Arquivo testing.json atualizado com sucesso!");


// OPERAÇÃO 4: MUDAR / ALTERAR (Equivale ao UPDATE)
db.artistas[0].nome = "João Manô - Versão Acústica";
console.log("Nome alterado do primeiro artista:", db.artistas[0].nome);
// Vai mostrar: João Manô - Versão Acústica