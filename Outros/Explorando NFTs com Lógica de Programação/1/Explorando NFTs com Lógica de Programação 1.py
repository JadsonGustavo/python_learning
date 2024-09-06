# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição.		
def descrever_termo(termo):
	if termo == "Tokenization":
			return "Converte ativos em tokens digitais"
			
	# TODO: Preencha corretamente a descrição de cada termo, considerando as condições abaixo e Saídas possíveis:		
	elif termo == "Blockchain":
	    return "Habilita transações seguras e à prova de adulterações"
	    
	elif termo == "Smart Contracts":
	    return "Programas autoexecutáveis que operam em blockchains"
	    	    	
	elif termo == "Decentralization":
	    return "Remove autoridades centrais e devolve o controle aos usuários"
	    
print(descrever_termo(entrada))