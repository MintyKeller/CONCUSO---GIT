
-- DDL DATA DEFINITION LANGUAGE
DROP TABLE IF EXISTS salvo;
DROP TABLE IF EXISTS seguidores;
DROP TABLE IF EXISTS fans;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS musica;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS ouvinte;
DROP TABLE IF EXISTS artista;

\c bd_spot_file;

CREATE TABLE artista ( 
id_artista  SERIAL,
PRIMARY KEY (id_artista),
email VARCHAR(50) UNIQUE NOT NULL, 
senha VARCHAR(40) NOT NULL, 
nome VARCHAR(40) NOT NULL, 
about TEXT NOT NULL, 
foto_de_perfil TEXT NOT NULL
);

CREATE TABLE ouvinte(
id_ouvinte  SERIAL,
PRIMARY KEY (id_ouvinte),
email VARCHAR(50) UNIQUE NOT NULL, 
senha VARCHAR(40) NOT NULL, 
nome VARCHAR(40) NOT NULL, 
foto_de_perfil TEXT
);

CREATE TABLE album ( 
id_album  SERIAL, 
PRIMARY KEY (id_album),
ano_lancamento SMALLINT NOT NULL, 
nome VARCHAR(60) NOT NULL, 
foto_da_capa_url TEXT NOT NULL, 
tempo_de_streaming INT NOT NULL, 
id_artista INTEGER NOT NULL, 
FOREIGN KEY (id_artista) REFERENCES artista(id_artista)
);

CREATE TABLE musica ( 
id_musica  SERIAL, 
PRIMARY KEY (id_musica), 
nome VARCHAR(50) NOT NULL, 
duracao SMALLINT NOT NULL, -- em segundos 
id_album INTEGER NOT NULL,
FOREIGN KEY (id_album) REFERENCES album(id_album)
);

CREATE TABLE playlist (
id_playlist  SERIAL, 
PRIMARY KEY (id_playlist), 
nome VARCHAR(60) DEFAULT 'MyPlaylist#000',
foto_da_capa_url TEXT, 
bio TEXT, 
tempo_de_streaming INT NOT NULL, 
id_ouvinte INTEGER NOT NULL, 
FOREIGN KEY (id_ouvinte) references ouvinte(id_ouvinte)
);

-- relacionamentos

CREATE TABLE fans( 
id_artista INTEGER NOT NULL, 
id_ouvinte INTEGER NOT NULL,
PRIMARY KEY (id_artista, id_ouvinte),
FOREIGN KEY (id_ouvinte) REFERENCES ouvinte(id_ouvinte),
FOREIGN KEY (id_artista) REFERENCES artista(id_artista) 
); 

CREATE TABLE seguidores ( 
id_seguido INTEGER NOT NULL,
PRIMARY KEY (id_seguido), 
id_seguidor INTEGER NOT NULL, 
FOREIGN KEY (id_seguido) REFERENCES ouvinte(id_ouvinte),
FOREIGN KEY (id_seguidor) REFERENCES ouvinte(id_ouvinte)
);

CREATE TABLE salvo ( 
id_playlist INTEGER NOT NULL,
PRIMARY KEY (id_playlist), 
id_musica INTEGER NOT NULL, 
FOREIGN KEY (id_playlist) REFERENCES playlist(id_playlist),
FOREIGN KEY (id_musica) REFERENCES musica(id_musica)
);

SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';

--DML DATA MANIPULATION LANGUAGE

INSERT INTO artista (email, senha, nome, about, foto_de_perfil) VALUES
('joaomano@gmail.com', 'barcoDiPapel', 'João Manô', 'João Manô é cantor, compositor e poeta brasileiro, com uma obra situada entre o indie e a música popular brasileira, marcada por lirismo, contemplação e uma espiritualidade encarnada no cotidiano. Suas canções dialogam com temas como fé, espera, fragilidade humana e beleza, propondo uma escuta atenta em meio ao excesso de ruídos do tempo presente', 'fotoJoaoManô.jpg'), 
('thecranberries@example.com', 'linger', 'The Cranberries', 'Combining the melodic jangle of post-Smiths indie guitar pop with the lilting, trance-inducing sonic textures of late 80s dream pop and adding a slight Celtic tint, the Cranberries became one of the more successful groups to emerge from the pre-Brit-pop indie scene of the early 90s.', 'fotoTheCranberries.jpg');

('rhcp@example.com', 'californication', 'Red Hot Chili Peppers', 'Banda norte-americana formada em Los Angeles, conhecida por misturar rock alternativo, funk, punk e elementos de rap. Suas músicas combinam energia explosiva, grooves marcantes e letras que transitam entre experiências pessoais, crítica social e a cultura californiana.', 'fotoRHCP.jpg'),

('u2@example.com', 'withorwithoutyou', 'U2', 'Grupo irlandês formado em Dublin, reconhecido mundialmente por seu rock atmosférico, letras reflexivas e engajamento em causas humanitárias. Sua trajetória atravessa décadas, unindo experimentação sonora, espiritualidade e grandes sucessos de estádio.', 'fotoU2.jpg'),

('coldplay@example.com', 'yellow', 'Coldplay', 'Banda britânica de rock alternativo conhecida por melodias emotivas, arranjos grandiosos e letras que exploram amor, esperança, perda e superação. Ao longo dos anos, incorporou elementos eletrônicos e pop sem abandonar sua identidade melódica.', 'fotoColdplay.jpg'),

('pinkfloyd@example.com', 'comfortablynumb', 'Pink Floyd', 'Uma das bandas mais influentes da história do rock progressivo, famosa por seus álbuns conceituais, composições extensas e experimentação sonora. Suas obras abordam temas como alienação, guerra, tempo, loucura e a condição humana.', 'fotoPinkFloyd.jpg'),

('weezer@example.com', 'buddyholly', 'Weezer', 'Banda norte-americana de rock alternativo caracterizada por guitarras marcantes, letras bem-humoradas e referências à cultura nerd. Suas canções frequentemente exploram inseguranças, relacionamentos e o cotidiano com sinceridade e ironia.', 'fotoWeezer.jpg'),

('legiaourbana@example.com', 'tempoperdido', 'Legião Urbana', 'Uma das bandas mais importantes do rock brasileiro, liderada por Renato Russo. Suas músicas abordam política, existencialismo, juventude, amor e espiritualidade, tornando-se trilha sonora de gerações inteiras.', 'fotoLegiaoUrbana.jpg'),

('skank@example.com', 'resposta', 'Skank', 'Grupo mineiro que combinou rock, reggae, pop e música brasileira em uma sonoridade acessível e marcante. Conhecido por melodias cativantes e letras que transitam entre romance, cotidiano e observações sociais.', 'fotoSkank.jpg'),

('greenday@example.com', 'basketcase', 'Green Day', 'Banda norte-americana que popularizou o punk rock para uma nova geração nos anos 1990. Suas músicas unem energia, irreverência e comentários sobre juventude, política e inconformismo social.', 'fotoGreenDay.jpg'),

('thesmiths@example.com', 'thereisalight', 'The Smiths', 'Grupo britânico de rock alternativo formado nos anos 1980, conhecido pela combinação das guitarras melódicas de Johnny Marr com as letras melancólicas e literárias de Morrissey. Sua influência permanece forte na música independente contemporânea.', 'fotoTheSmiths.jpg'),

('calmara@example.com', 'espera', 'Calmará', 'Banda brasileira de indie folk e rock alternativo que constrói canções intimistas marcadas por reflexões sobre fé, relacionamentos, amadurecimento e esperança. Sua sonoridade delicada valoriza letras contemplativas e emotivas.', 'fotoCalmara.jpg');
SELECT * FROM artista;


SELECT id_artista, nome
FROM artista
ORDER BY id_artista;

INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista) VALUES

(2020,'Volver','volver.jpg',0,1),

(1991,'Blood Sugar Sex Magik','bloodSugarSexMagik.jpg',0,3),

(2000,'Parachutes','parachutes.jpg',0,5),

(1970,'Atom Heart Mother','atomHeartMother.jpg',0,6);

---------------------------------------------------------
INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista)
VALUES (1996, 'Pinkerton', 'pinkerton.jpg', 0, 7);

INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista)
VALUES (1993, 'Everybody Else Is Doing It, So Why Cant We', 'everybody_else.jpg', 0, 2);

INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista)
VALUES (1989, 'As Quatro Estações', 'as_quatro_estacoes.jpg', 0, 8);

INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista)
VALUES (2000, 'All That You Cant Leave Behind', 'all_that_you_cant_leave_behind.jpg', 0, 4);

INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista)
VALUES (1994, 'Dookie', 'dookie.jpg', 0, 10);

INSERT INTO album (ano_lancamento, nome, foto_da_capa_url, tempo_de_streaming, id_artista)
VALUES (2021, 'Calmará', 'calmara.jpg', 0, 12);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Volver', 214, 1),
('Temporais', 268, 1),
('Maturidade', 280, 1),
('Esperanca', 309, 1),
('Paciencia', 185, 1);

INSERT INTO musica (nome, duracao, id_album) VALUES
('The Power of Equality', 243, 2),
('If You Have to Ask', 216, 2),
('Breaking the Girl', 295, 2),
('Funky Monks', 323, 2),
('Suck My Kiss', 217, 2),
('I Could Have Lied', 244, 2);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Dont Panic', 136, 3),
('Shiver', 304, 3),
('Spies', 318, 3),
('Sparks', 227, 3),
('Yellow', 266, 3),
('Trouble', 273, 3);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Atom Heart Mother', 1421, 4),
('If', 270, 4),
('Summer 68', 328, 4),
('Fat Old Sun', 323, 4),
('Alans Psychedelic Breakfast', 780, 4);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Tired Of Sex', 181, 5),
('Getchoo', 172, 5),
('No Other One', 181, 5),
('Why Bother?', 128, 5),
('Across The Sea', 272, 5),
('The Good Life', 257, 5),
('El Scorcho', 243, 5),
('Pink Triangle', 233, 5),
('Falling For You', 227, 5),
('Butterfly', 173, 5);

INSERT INTO musica (nome, duracao, id_album) VALUES
('I Still Do', 197, 6),
('Dreams', 273, 6),
('Sunday ', 210, 6),
('Pretty', 136, 6),
('Waltzing Back', 217, 6),
('Not Sorry', 263, 6),
('Linger', 274, 6);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Ha Tempos', 198, 7),
('Pais E Filhos', 308, 7),
('Feedback Song For A Dying Friend', 325, 7),
('Quando O Sol Bater Na Janela Do Teu Quarto', 193, 7),
('Eu Era Um Lobisomem Juvenil', 406, 7),
('1965 Duas Tribos', 225, 7),
('Monte Castelo', 230, 7),
('Mauricio', 198, 7),
('Meninos E Meninas', 203, 7);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Beautiful Day', 248, 8),
('Stuck In A Moment You Cant Get Out Of', 273, 8),
('Elevation', 226, 8),
('Walk On', 296, 8),
('Kite', 264, 8),
('In A Little While', 220, 8),
('Wild Honey', 226, 8);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Burnout', 127, 9),
('Having a Blast', 164, 9),
('Chump', 174, 9),
('Longview', 233, 9),
('Welcome to Paradise', 224, 9),
('Pulling Teeth', 150, 9),
('Basket Case', 181, 9);

INSERT INTO musica (nome, duracao, id_album) VALUES
('Sereno do Alarido', 71, 10),
('Patrício, de Onde Vim', 198, 10),
('É de Manhã', 200, 10),
('Outra Vez Além Zabelê', 151, 10),
('Hillsamba', 196, 10),
('Volta a Alta Terra', 208, 10),
('Luzia', 204, 10);


--testes em DQL - DATA QUERY LANGUAGE 

SELECT * FROM album; 
SELECT * FROM musica; 

SELECT 
    album.nome AS nome_do_album, 
    musica.nome AS nome_da_musica
FROM album
INNER JOIN musica ON album.id_album = musica.id_album;

