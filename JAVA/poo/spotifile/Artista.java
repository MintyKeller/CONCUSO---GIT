package poo.spotifile;
import java.util.List;
// EXTENDS -- Inheritance
/*
In Java, it is possible to inherit attributes and methods from one class to another. We group the "inheritance concept" into two categories:

subclass (child) - the class that inherits from another class
superclass (parent) - the class being inherited from
To inherit from a class, use the extends keyword.
*/
public class Artista extends Usuario{
    // atributes 
    // are privated because of Encapsulation, and will only be acessed by gets and sets 
    private long idArtista;
	private String about; 
	private List<Album> albuns;
	private List<Ouvinte> fans;

    //constructor
    	public Artista(String nome, String email, String senha, String fotoPerfil, long idArtista, String about,
		List<Album> albuns, List<Ouvinte> fans) {
		super(nome, email, senha, fotoPerfil); // here is where the constructor calls the super (abstract mother class) by super()
		this.idArtista = idArtista;
		this.about = about;
		this.albuns = albuns;
		this.fans = fans;
	}

    //empty constructor 
	public Artista() {
		super();
	}

    //getters
    public long getIdArtista() {
		return idArtista;
	}

	public String getAbout() {
		return about;
	}

	public List<Album> getAlbuns() {
		return albuns;
	}

	public List<Ouvinte> getFans() {
		return fans;
	}

        //setters
	public void setIdArtista(long idArtista) {
		this.idArtista = idArtista;
	}

	public void setAbout(String about) {
		this.about = about;
	}

	public void setAlbuns(List<Album> albuns) {
		this.albuns = albuns;
	}

	public void setFans(List<Ouvinte> fans) {
		this.fans = fans;
	}

}
