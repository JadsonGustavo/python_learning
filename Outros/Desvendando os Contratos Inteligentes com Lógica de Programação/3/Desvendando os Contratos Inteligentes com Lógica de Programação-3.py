# Recebe a Entrada do usuário e armazena na variável "entrada"
print("Digite as opções:\n - DAOs\n - Gas Fees\n - Oráculos\n - Solidity\n - DApps")
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição.
def descrever_termo(termo):
  if termo == "DAOs":
    return "Organizações autônomas descentralizadas"

  # TODO: Preencha corretamente a descrição de cada termo, considerando as condições abaixo e Saídas possíveis:
  elif termo == "Gas Fees":
    return "Taxas pagas para realizar transações e executar contratos"
			
  elif termo == "Oráculos":
    return "Entidades que fornecem dados externos aos contratos inteligentes"

  elif termo == "Solidity":
    return "Linguagem de programação utilizada nos contratos inteligentes"  	    

  elif termo == "DApps":
    return "Aplicações descentralizadas que operam em uma rede blockchain"

print(descrever_termo(entrada))
a=input("Tecle qualuer tecla para finalizar")