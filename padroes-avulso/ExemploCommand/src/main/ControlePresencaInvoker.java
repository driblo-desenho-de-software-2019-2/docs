package main;

/** Classe invocadora */
public class ControlePresencaInvoker {
	public void setCommand(Command cmd) {
		cmd.execute();
	}
}
