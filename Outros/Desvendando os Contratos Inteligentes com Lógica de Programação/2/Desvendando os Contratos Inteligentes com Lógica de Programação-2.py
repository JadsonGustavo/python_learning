# Recebe a Entrada do usuário e armazena na variável "entrada"
print("Digite as opções:\n - Automação de Acordos\n - Interoperabilidade\n - Imutabilidade\n - Execução Autônoma")
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição.
def descrever_termo(termo):
  if termo == "Automação de Acordos":
    return "Permite a execução de contratos baseado em eventos pré-definidos"
			
	# TODO: Preencha corretamente a descrição de cada termo, considerando as condições abaixo e Saídas possíveis:						  
  elif termo == "Interoperabilidade":
    return "Capacidade de interagir e operar com diferentes blockchains"
	    
  elif termo == "Imutabilidade":
    return "Não pode ser alterado ou modificado após sua criação"
	    	    	
  elif termo == "Execução Autônoma":
    return "Executa automaticamente as condições do código do contrato"

print(descrever_termo(entrada))
a=input("Tecle qualuer tecla para finalizar")