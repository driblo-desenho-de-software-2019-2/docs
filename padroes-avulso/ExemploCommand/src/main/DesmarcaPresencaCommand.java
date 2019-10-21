package main;

/** O Command marcar presença - ConcreteCommand #2 */
public class DesmarcaPresencaCommand implements Command{
	private PresencaReceiver presenca; 
	
	public DesmarcaPresencaCommand(PresencaReceiver presenca) {
		this.presenca = presenca;
	}
	@Override
	public void execute() {
		presenca.desmarcar();
	}	
}
