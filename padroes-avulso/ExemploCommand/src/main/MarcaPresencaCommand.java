package main;

/** O Command marcar presença - ConcreteCommand #1 */
public class MarcaPresencaCommand implements Command{
	private PresencaReceiver presenca; 
	
	public MarcaPresencaCommand(PresencaReceiver presenca) {
		this.presenca = presenca;
	}
	@Override
	public void execute() {
		presenca.marcar();
	}	
}
