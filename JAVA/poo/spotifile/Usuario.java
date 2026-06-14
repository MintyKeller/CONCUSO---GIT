package poo.spotifile;

/*
this is a abstract class. 

The abstract keyword is a non-access modifier, used for classes and methods:

Abstract class: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).

Abstract method: can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from).

*/

/*

Why And When To Use Abstract Classes and Methods?
To achieve security - hide certain details and only show the important details of an object.
*/

public abstract class Usuario {
    //atributes: they are private because of Encapsulation 
    /*
    The meaning of Encapsulation, is to make sure that "sensitive" data is hidden from users. To achieve this, you must:

declare class variables/attributes as private
provide public get and set methods to access and update the value of a private variable
    
    */
 	private String nome; 
	private String email;
	private String senha;
	private String fotoPerfil;;

    //constructor 
    /*
    as the abstract class, to be used, it must be inherited, 
    the constructor exists because in the subclass that inherits the superclass
    its constructor it's going to call the super() constructor!
    /////////////////////////////////////////////////////////////////////////
    Needed for subclasses to call super() and initialize inherited attributes.
    Abstract classes cannot be instantiated, but their constructors are 
    essential for initializing shared state in subclasses.
    */
	Usuario(String nome, String email, String senha, String fotoPerfil) {
		this.nome = nome;
		this.email = email;
		this.senha = senha;
		this.fotoPerfil = fotoPerfil;
	}

    //empty constructor 
	public Usuario() {
		
	}
	//getter 

	public String getNome() {
		return nome;
	}

	public String getEmail() {
		return email;
	}

	public String getSenha() {
		return senha;
	}
	
	public String getFotoPerfil() {
		return fotoPerfil;
	}


	//setters
	public void setNome(String nome) {
		this.nome = nome;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public void setSenha(String senha) {
		this.senha = senha;
	}
	
	public void setFotoPerfil(String fotoPerfil) {
		this.fotoPerfil = fotoPerfil;
	}
    
}

/*
this projetct of mine has no interfaces, so I'll explain here: 

An interface is a completely "abstract class" 
that is used to group related methods with empty bodies:

    // interface
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void run(); // interface method (does not have a body)
}

ABSTRACT CLASSES ARE INHERITED WITH THE extends KEYWORD, INTERFACES USES: implements KEYWORD
To access the interface methods, the interface must be "implemented" 
(kinda like inherited) by another class with the implements keyword
 (instead of extends). 
 The body of the interface method is provided by the "implement" class

Notes on Interfaces:
    Like abstract classes, interfaces cannot be used to create objects (in the example above, it is not possible to create an "Animal" object in the MyMainClass)
    Interface methods do not have a body - the body is provided by the "implement" class
    On implementation of an interface, you must override all of its methods
    Interface methods are by default abstract and public
    Interface attributes are by default public, static and final
    An interface cannot contain a constructor (as it cannot be used to create objects)


*/

/*
In general, abstract classes can and should have constructors because:

Initialization of shared state: Abstract classes often have fields that need to be initialized for all subclasses
Enforcing initialization logic: The constructor ensures that any subclass must call it (via super() or super(...)) and go through required setup
Defining contracts: It's part of the class contract—subclasses inherit the constructor behavior


*/
