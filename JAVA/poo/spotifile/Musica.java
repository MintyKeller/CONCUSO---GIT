package poo.spotifile;

public class Musica {
    //atributes
    private long idMusica;
	private String nome;
	private int duracaoMusica;
	private long idAlbum;

    //constructor
	public Musica(long idMusica, String nome, int duracaoMusica, long idAlbum) {
		this.idMusica = idMusica;
		this.nome = nome;
		this.duracaoMusica = duracaoMusica;
		this.idAlbum = idAlbum;
	}

    //empty constructor
	public Musica() {

	}

	//getters
	public long getIdMusica() {
		return idMusica;
	}

	public String getNome() {
		return nome;
	}

	public int getDuracaoMusica() {
		return duracaoMusica;
	}

	public long getIdAlbum() {
		return idAlbum;
	}


    //setters
	public void setIdMusica(long idMusica) {
		this.idMusica = idMusica;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public void setDuracaoMusica(int duracaoMusica) {
		this.duracaoMusica = duracaoMusica;
	}

	public void setIdAlbum(long idAlbum) {
		this.idAlbum = idAlbum;
	}

    //methodsss
	public String printarInfos() {
		String printarInfos;
		int segs = getDuracaoMusica();
		int mins = 0;
		int horas = 0;
		while (segs > 60) {
			mins++;
			segs -= 60;
		}
		while (mins > 60) {
			horas++;
			mins -= 60;
		}
		if (horas > 0) {
			printarInfos = horas + " horas e " + mins + " minutos";
		} else if (mins > 0) {
			printarInfos = mins + " minutos e " + segs + " segundos";
		} else if (mins == 0 && horas == 0) {
			printarInfos = segs + " segundos";
		} else {
			printarInfos = segs + " segundos!"; // nao dar ponto de exclamação
		}

		return (printarInfos);

	}
}
