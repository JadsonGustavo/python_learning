print("Bem vindo a FibraNet")
# TODO_: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
# TODO_: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
def recomendar_plano(cosumo):
        
    if consumo<=10:
        return "Plano Essencial Fibra - 50Mbps "
    elif consumo<=20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"
# TODO_: Retorne o plano de internet adequado:
print("\n- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB. \n- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.\n- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.")
# Solicita ao usuário que insira o consumo médio mensal de dados:
print("Ajude-nos a lhe recomendar o melhor plano digitando seu consumo médio:")  
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
consumo = float(input())
print(recomendar_plano(consumo))

   
    

 



   

  
 

