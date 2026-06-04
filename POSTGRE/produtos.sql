
DROP TABLE IF EXISTS salvo;
DROP TABLE IF EXISTS seguidores;
DROP TABLE IF EXISTS fans;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS musica;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS ouvinte;
DROP TABLE IF EXISTS artista;
/*
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

*/