package main;

/** O Command marcar presença - ConcreteCommand #2 */
public class DesmarcarPresencaCommand implements Command{
	private PresencaReceiver presenca; 
	
	public DesmarcarPresencaCommand(PresencaReceiver presenca) {
		this.presenca = presenca;
	}
	@Override
	public void execute() {
		presenca.desmarcar();
	}	
}
