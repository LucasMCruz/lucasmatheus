package Desafioveiculo;

public class Veiculo {
	private String marca;
	private String modelo;
	private float km;
	private String placa;
	private String cor;
	private boolean ligado;
	private int litrosCombustivel;
	private int velocidade;
	private double preço;
	
	public String getMarca() {
		return marca;
	}
	
	public void setMarca(String marca) {
		this.marca = marca;
	}
	
	public String getModelo() {
		return modelo;
	}
	
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	
	public float getKm() {
		return km;
	}
	
	public void setKm(float km) {
		this.km = km;
	}
	
	public String getPlaca() {
		return placa;
	}
	
	public void setPlaca(String placa) {
		this.placa = placa;
	}
	
	public String getCor() {
		return cor;
	}
	
	public void setCor(String cor) {
		this.cor = cor;
	}
	
	public boolean isLigado() {
		return ligado;
	}
	
	public void setLigado(boolean ligado) {
		this.ligado = ligado;
	}
	
	public int getLitrosCombustivel() {
		return litrosCombustivel;
	}
	
	public void setLitrosCombustivel(int litrosCombustivel) {
		this.litrosCombustivel = litrosCombustivel;
	}
	
	public int getVelocidade() {
		return velocidade;
	}
	
	public void setVelocidade(int velocidade) {
		this.velocidade = velocidade;
	}
	
	public double getPreço() {
		return preço;
	}
	
	public void setPreço(double preço) {
		this.preço = preço;
	}
	
	void status() {
		System.out.println("Marca: " + this.marca + " Modelo: " + this.modelo + " Placa: " + this.placa + " Cor: " + this.cor + "Ligado" + ligado);
	}
	
	
	void acelerar() {
		if (ligado == true && litrosCombustivel > 0) {
			
			velocidade += 20;
			litrosCombustivel -= 1;	
			System.out.println("Sua velocidade atual é " + velocidade +"km/h" + "\n Seu combustivel atual é " +litrosCombustivel + "L");
			
		}
		else {
			System.out.println("O carro esta desligado ou  sem gasolina, ligue-o para acelerar ou coloque gasolina.");
			
		}  
	}
	
	void freiar() {
		if (velocidade > 0) {
			velocidade -= 20;
			System.out.println("Freando... Você esta 20km/h mais lerdo");
		}
		else {
			System.out.println("O carro esta parado");
		}
		
	}
	
	void ligar() {
		ligado = true;
		System.out.println("carro ligado");
		
	}
	
	void desligar() {
		ligado = false;
		System.out.println("carro desligado");
		
		
	}
	
	void abastecer(int qtdLitros) {
		if(litrosCombustivel == 100) {
			System.out.println("Você nao pode colcoar mais do que 100" + " portanto seu tanque esta com " + litrosCombustivel + "L");
		}
		if(litrosCombustivel <= 100) {
			litrosCombustivel += qtdLitros;
			if (litrosCombustivel > 100) { 
				litrosCombustivel = 100;
				System.out.println("Você nao pode colcoar mais do que 100L" + " portanto seu tanque esta com " + litrosCombustivel + "L");
				}
			else {
				System.out.println("Você abasteceu" + qtdLitros + "L" + "seu tanque esta com " + litrosCombustivel);
			}
		}
		
	}
	
	void pintar(String corp) { 
		cor = corp;
		System.out.println("Voce pintou seu carro de " + corp);
		
	}
	
	
	
	
	
	
	
	
	
	
	
}
