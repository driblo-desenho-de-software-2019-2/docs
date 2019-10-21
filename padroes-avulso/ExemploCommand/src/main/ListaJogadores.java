package main;

import java.util.Scanner;

public class ListaJogadores {
	public static void main(String[] args){
		int opcao = 2;
	    Scanner ler = new Scanner(System.in);
        
	    PresencaReceiver presenca = new PresencaReceiver();
	    Command marcaPresenca = new MarcaPresencaCommand(presenca);
	    Command desmarcaPresenca = new DesmarcaPresencaCommand(presenca);
	    ControlePresencaInvoker presencaJogador = new ControlePresencaInvoker();
	    
	    menu(opcao);
  
	    do {
	    	opcao = ler.nextInt();
	    	switch(opcao) {
	    		case 1:
	    			presencaJogador.setCommand(marcaPresenca);
	    			break;
	    		case 2:
	    			presencaJogador.setCommand(desmarcaPresenca);
	    			break;
	    		default:
	                System.out.println("ATÉ A PRÓXIMA.");	
	    	}
	    	
	    	menu(opcao);
	    	
	    }while(opcao != 0);
	    
	    ler.close();
	}
	
	private static void menu(int opcao) {
		if(opcao == 2) {
    		System.out.println("Você ainda não marcou presença na pelada\n");	
    		System.out.println("Digite 1 para marcar presença");
    		System.out.print("Digite 0 para sair\n");
    	}
    	else if(opcao == 1){
    		System.out.println("Você marcou presença na pelada\n");	
    		System.out.println("Digite 2 para desmarcar presença");
    		System.out.print("Digite 0 para sair\n");
    	}		
	}
	
}