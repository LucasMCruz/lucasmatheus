package Desafioveiculo;

public class carrao {
	public static void main(String[] args) {
		Veiculo c1;
		c1 = new Veiculo();
		c1.setMarca("Renault");
		c1.setCor("Branco");
		c1.setModelo("Duster");
		c1.setKm((float) 1000.00);
		c1.setLigado(false);
		c1.setPlaca("ABC1234");
		c1.setPreço(70000.00);
		c1.setVelocidade(0);
		c1.setLitrosCombustivel(0);
		
		
		
		c1.status();
		
		c1.abastecer(950);
		c1.acelerar();
		c1.ligar();
		c1.freiar();
		c1.pintar("verde");
		
	}
}
