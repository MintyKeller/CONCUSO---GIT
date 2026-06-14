package poo.spotifile;
import java.util.List;

public class Album extends Colecao {
    //atributes
   private long idAlbum;
	private int anoLancamento;
	private long idArtista;
	

	//constructor
	public Album(List<Musica> musicas, String fotoDaCapaUrl, int tempoStreaming, String nome, long idAlbum,
			int anoLancamento, long idArtista) {
		super(musicas, fotoDaCapaUrl, tempoStreaming, nome);
		this.idAlbum = idAlbum;
		this.anoLancamento = anoLancamento;
		this.idArtista = idArtista;
	}
	
    //empty constructor
	public Album() {
		super();
	}
	
    //getters
	public long getIdAlbum() {
		
		return idAlbum;
	}
	public int getAnoLancamento() {
		return anoLancamento;
	}
	public long getIdArtista() {
		return idArtista;
	}
	
	
    //setters
	public void setIdAlbum(long idAlbum) {
		this.idAlbum = idAlbum;
	}
	public void setAnoLancamento(int anoLancamento) {
		this.anoLancamento = anoLancamento;
	}
	public void setidArtista(long idArtista) {
		this.idArtista = idArtista;
	}  

    //methodss
@Override //override the super method
public String printarInfos() {
    String parentInfo = super.printarInfos();
    return " • " + anoLancamento + parentInfo;
}
}
