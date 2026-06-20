use('bd_spot_file');

//artistas
db.artistas.insertMany([
  { email: 'joaomano@gmail.com', senha: 'barcoDiPapel', nome: 'João Manô', about: 'João Manô é cantor, compositor e poeta brasileiro...', foto_de_perfil: 'fotoJoaoManô.jpg' },
  { email: 'thecranberries@example.com', senha: 'linger', nome: 'The Cranberries', about: 'Combining the melodic jangle of post-Smiths indie guitar pop...', foto_de_perfil: 'fotoTheCranberries.jpg' },
  { email: 'rhcp@example.com', senha: 'californication', nome: 'Red Hot Chili Peppers', about: 'Banda norte-americana formada em Los Angeles...', foto_de_perfil: 'fotoRHCP.jpg' },
  { email: 'u2@example.com', senha: 'withorwithoutyou', nome: 'U2', about: 'Grupo irlandês formado em Dublin...', foto_de_perfil: 'fotoU2.jpg' },
  { email: 'coldplay@example.com', senha: 'yellow', nome: 'Coldplay', about: 'Banda britânica de rock alternativo...', foto_de_perfil: 'fotoColdplay.jpg' },
  { email: 'pinkfloyd@example.com', senha: 'comfortablynumb', nome: 'Pink Floyd', about: 'Uma das bandas mais influentes da história...', foto_de_perfil: 'fotoPinkFloyd.jpg' },
  { email: 'weezer@example.com', senha: 'buddyholly', nome: 'Weezer', about: 'Banda norte-americana de rock alternativo...', foto_de_perfil: 'fotoWeezer.jpg' },
  { email: 'legiaourbana@example.com', senha: 'tempoperdido', nome: 'Legião Urbana', about: 'Uma das bandas mais importantes do rock brasileiro...', foto_de_perfil: 'fotoLegiaoUrbana.jpg' },
  { email: 'skank@example.com', senha: 'resposta', nome: 'Skank', about: 'Grupo mineiro que combinou rock, reggae...', foto_de_perfil: 'fotoSkank.jpg' },
  { email: 'greenday@example.com', senha: 'basketcase', nome: 'Green Day', about: 'Banda norte-americana que popularizou o punk rock...', foto_de_perfil: 'fotoGreenDay.jpg' },
  { email: 'thesmiths@example.com', senha: 'thereisalight', nome: 'The Smiths', about: 'Grupo britânico de rock alternativo formado nos anos 1980...', foto_de_perfil: 'fotoTheSmiths.jpg' },
  { email: 'calmara@example.com', senha: 'espera', nome: 'Calmará', about: 'Banda brasileira de indie folk...', foto_de_perfil: 'fotoCalmara.jpg' }
]);

const joao = db.artistas.findOne({ email: 'joaomano@gmail.com' });
const cranberries = db.artistas.findOne({ email: 'thecranberries@example.com' });
const rhcp = db.artistas.findOne({ email: 'rhcp@example.com' });
const u2 = db.artistas.findOne({ email: 'u2@example.com' });
const coldplay = db.artistas.findOne({ email: 'coldplay@example.com' });
const pinkfloyd = db.artistas.findOne({ email: 'pinkfloyd@example.com' });
const weezer = db.artistas.findOne({ email: 'weezer@example.com' });
const legiao = db.artistas.findOne({ email: 'legiaourbana@example.com' });
const greenday = db.artistas.findOne({ email: 'greenday@example.com' });
const calmara = db.artistas.findOne({ email: 'calmara@example.com' });

//albuns e musicas

db.albuns.insertMany([
  {
    "nome": "Volver",
    "ano_lancamento": 2020,
    "foto_da_capa_url": "volver.jpg",
    "tempo_de_streaming": 0,
    "id_artista": joao._id,
    "musicas": [
      { "nome": "Volver", "duracao": 214 },
      { "nome": "Temporais", "duracao": 268 },
      { "nome": "Maturidade", "duracao": 280 },
      { "nome": "Esperanca", "duracao": 309 },
      { "nome": "Paciencia", "duracao": 185 }
    ]
  },
  {
    "nome": "Blood Sugar Sex Magik",
    "ano_lancamento": 1991,
    "foto_da_capa_url": "bloodSugarSexMagik.jpg",
    "tempo_de_streaming": 0,
    "id_artista": rhcp._id,
    "musicas": [
      { "nome": "The Power of Equality", "duracao": 243 },
      { "nome": "If You Have to Ask", "duracao": 216 },
      { "nome": "Breaking the Girl", "duracao": 295 },
      { "nome": "Funky Monks", "duracao": 323 },
      { "nome": "Suck My Kiss", "duracao": 217 },
      { "nome": "I Could Have Lied", "duracao": 244 }
    ]
  },
  {
    "nome": "Parachutes",
    "ano_lancamento": 2000,
    "foto_da_capa_url": "parachutes.jpg",
    "tempo_de_streaming": 0,
    "id_artista": coldplay._id,
    "musicas": [
      { "nome": "Dont Panic", "duracao": 136 },
      { "nome": "Shiver", "duracao": 304 },
      { "nome": "Spies", "duracao": 318 },
      { "nome": "Sparks", "duracao": 227 },
      { "nome": "Yellow", "duracao": 266 },
      { "nome": "Trouble", "duracao": 273 }
    ]
  },
  {
    "nome": "Atom Heart Mother",
    "ano_lancamento": 1970,
    "foto_da_capa_url": "atomHeartMother.jpg",
    "tempo_de_streaming": 0,
    "id_artista": pinkfloyd._id,
    "musicas": [
      { "nome": "Atom Heart Mother", "duracao": 1421 },
      { "nome": "If", "duracao": 270 },
      { "nome": "Summer 68", "duracao": 328 },
      { "nome": "Fat Old Sun", "duracao": 323 },
      { "nome": "Alans Psychedelic Breakfast", "duracao": 780 }
    ]
  },
  {
    "nome": "Pinkerton",
    "ano_lancamento": 1996,
    "foto_da_capa_url": "pinkerton.jpg",
    "tempo_de_streaming": 0,
    "id_artista": weezer._id,
    "musicas": [
      { "nome": "Tired Of Sex", "duracao": 181 },
      { "nome": "Getchoo", "duracao": 172 },
      { "nome": "No Other One", "duracao": 181 },
      { "nome": "Why Bother?", "duracao": 128 },
      { "nome": "Across The Sea", "duracao": 272 },
      { "nome": "The Good Life", "duracao": 257 },
      { "nome": "El Scorcho", "duracao": 243 },
      { "nome": "Pink Triangle", "duracao": 233 },
      { "nome": "Falling For You", "duracao": 227 },
      { "nome": "Butterfly", "duracao": 173 }
    ]
  },
  {
    "nome": "Everybody Else Is Doing It, So Why Cant We",
    "ano_lancamento": 1993,
    "foto_da_capa_url": "everybody_else.jpg",
    "tempo_de_streaming": 0,
    "id_artista": cranberries._id,
    "musicas": [
      { "nome": "I Still Do", "duracao": 197 },
      { "nome": "Dreams", "duracao": 273 },
      { "nome": "Sunday ", "duracao": 210 },
      { "nome": "Pretty", "duracao": 136 },
      { "nome": "Waltzing Back", "duracao": 217 },
      { "nome": "Not Sorry", "duracao": 263 },
      { "nome": "Linger", "duracao": 274 }
    ]
  },
  {
    "nome": "As Quatro Estações",
    "ano_lancamento": 1989,
    "foto_da_capa_url": "as_quatro_estacoes.jpg",
    "tempo_de_streaming": 0,
    "id_artista": legiao._id,
    "musicas": [
      { "nome": "Ha Tempos", "duracao": 198 },
      { "nome": "Pais E Filhos", "duracao": 308 },
      { "nome": "Feedback Song For A Dying Friend", "duracao": 325 },
      { "nome": "Quando O Sol Bater Na Janela Do Teu Quarto", "duracao": 193 },
      { "nome": "Eu Era Um Lobisomem Juvenil", "duracao": 406 },
      { "nome": "1965 Duas Tribos", "duracao": 225 },
      { "nome": "Monte Castelo", "duracao": 230 },
      { "nome": "Mauricio", "duracao": 198 },
      { "nome": "Meninos E Meninas", "duracao": 203 }
    ]
  },
  {
    "nome": "All That You Cant Leave Behind",
    "ano_lancamento": 2000,
    "foto_da_capa_url": "all_that_you_cant_leave_behind.jpg",
    "tempo_de_streaming": 0,
    "id_artista": u2._id,
    "musicas": [
      { "nome": "Beautiful Day", "duracao": 248 },
      { "nome": "Stuck In A Moment You Cant Get Out Of", "duracao": 273 },
      { "nome": "Elevation", "duracao": 226 },
      { "nome": "Walk On", "duracao": 296 },
      { "nome": "Kite", "duracao": 264 },
      { "nome": "In A Little While", "duracao": 220 },
      { "nome": "Wild Honey", "duracao": 226 }
    ]
  },
  {
    "nome": "Dookie",
    "ano_lancamento": 1994,
    "foto_da_capa_url": "dookie.jpg",
    "tempo_de_streaming": 0,
    "id_artista": greenday._id,
    "musicas": [
      { "nome": "Burnout", "duracao": 127 },
      { "nome": "Having a Blast", "duracao": 164 },
      { "nome": "Chump", "duracao": 174 },
      { "nome": "Longview", "duracao": 233 },
      { "nome": "Welcome to Paradise", "duracao": 224 },
      { "nome": "Pulling Teeth", "duracao": 150 },
      { "nome": "Basket Case", "duracao": 181 }
    ]
  },
  {
    "nome": "Calmará",
    "ano_lancamento": 2021,
    "foto_da_capa_url": "calmara.jpg",
    "tempo_de_streaming": 0,
    "id_artista": calmara._id,
    "musicas": [
      { "nome": "Sereno do Alarido", "duracao": 71 },
      { "nome": "Patrício, de Onde Vim", "duracao": 198 },
      { "nome": "É de Manhã", "duracao": 200 },
      { "nome": "Outra Vez Além Zabelê", "duracao": 151 },
      { "nome": "Hillsamba", "duracao": 196 },
      { "nome": "Volta a Alta Terra", "duracao": 208 },
      { "nome": "Luzia", "duracao": 204 }
    ]
  }
]);

// consultas

//equivale a SELECT * FROM album WHERE nome = 'Dookie'
db.albuns.find({ nome: "Dookie" });


//SELECT * FROM album WHERE ano_lancamento BETWEEN 1990 AND 1999 ORDER BY ano_lancamento ASC
db.albuns.find({
  ano_lancamento: { $gte: 1990, $lte: 1999 }
}).sort({ ano_lancamento: 1 });

// SELECT nome FROM album..
db.albuns.find(
  {}, // Primeiro objeto vazio significa: "trazer todos os álbuns"
  { nome: 1, musicas: 1, _id: 0 } // Mostra nome e músicas, esconde o ID
);


db.albuns.find({ "musicas.nome": "Yellow" });

// JOIN artista ON ...
db.albuns.aggregate([
  {
    $lookup: {
      from: "artistas",         // Coleção onde vamos buscar os dados
      localField: "id_artista", // Campo que temos no Álbum
      foreignField: "_id",      // Campo correspondente na coleção Artistas
      as: "dados_do_artista"    // Nome da nova propriedade que será criada
    }
  }
]);





