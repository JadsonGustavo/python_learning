# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um termo e retornar sua respectiva descrição.		
def descrever_termo(termo):
  if termo == "Governança":
    return "Membros de uma DAO votam em propostas para tomar decisões"

  # TODO: Preencha corretamente a descrição de cada termo, considerando as condições abaixo e Saídas possíveis:		
  elif termo == "Liquidity Pool":
    return "Fundo coletivo bloqueado em um contrato inteligente"

  elif termo == "Yield Farming":
    return "Estratégia para aumentar o retorno de investimentos em DeFi"

  elif termo == "Token Governance":
    return "Tokens que representam o poder de voto dos membros em uma DAO"

print(descrever_termo(entrada))