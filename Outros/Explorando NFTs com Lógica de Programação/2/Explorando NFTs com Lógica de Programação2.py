# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma característica e retornar o padrão respectivo.
def identificar_padrao_nft(caracteristica):
	if caracteristica == "Permite identificadores únicos para cada token":
			return "ERC-721"
			
	# TODO: Preencha corretamente o padrão referente a cada característica, considerando as condições abaixo e Saídas possíveis:		
	elif caracteristica == "Suporta a transferência em massa de diferentes tipos de tokens":
	    return "ERC-1155"
	    
	elif caracteristica == "Permite a criação de tokens fungíveis e não fungíveis":
	    return "ERC-1155"
	    	    	
	elif caracteristica == "Exige que cada token seja único e não divisível":
	    return "ERC-721"
	    
print(identificar_padrao_nft(entrada))

