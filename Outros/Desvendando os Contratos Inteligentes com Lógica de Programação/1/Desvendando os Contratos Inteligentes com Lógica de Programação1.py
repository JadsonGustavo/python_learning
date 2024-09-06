# Recebe a Entrada do usuário e armazena na variável "entrada"
print("Digite as opções:\n - Cadeia de Blocos\n - Mineração\n - Ethereum\n - NFT")
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição.	
def descrever_termo(termo):
	if termo == "NFT":
			return "Token digital na blockchain que representa um ativo único"
			
	# TODO: Preencha corretamente a descrição de cada termo, considerando as condições abaixo e Saídas possíveis: 	    	
	elif termo == "Cadeia de Blocos":
	    return "Sequência de blocos com informações registradas na blockchain"
	    
	elif termo == "Mineração":
	    return "Processo de validar e registrar transações na blockchain"
    
	elif termo == "Ethereum":
	    return "Plataforma que executa contratos inteligentes e DApps"
	    
print(descrever_termo(entrada))
a=input("Tecle qualuer tecla para finalizar")