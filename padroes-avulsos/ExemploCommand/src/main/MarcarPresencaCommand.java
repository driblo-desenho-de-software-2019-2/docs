package main;

/** O Command marcar presença - ConcreteCommand #1 */
public class MarcarPresencaCommand implements Command{
	private PresencaReceiver presenca; 
	
	public MarcarPresencaCommand(PresencaReceiver presenca) {
		this.presenca = presenca;
	}
	@Override
	public void execute() {
		presenca.marcar();
	}	
}
