#import os
# Software Bancário
# O Software permite três operações: depósito, saque e extrato.
# O sistema deve permitir realizar 3 saques diários com limite máximo
# de R$ 500,00 por saque. Deve listar todos os depósitos e saques na conta.
# Se o estrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações".
# Os valoeres devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45= R$ 1500.45

menu="""
==========================================

    Bem vindo ao Banco JG Digital

==========================================
Escolha uma das opções abaixo de 1 à 4
[1] Extrato
[2] Depositar
[3] Sacar
[4] Sair

==========================================
=>"""

#print(menu)

saldo=0
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3

while True:
    opcao=input(menu)
    if opcao=='1':
        print("\n==========================================")
        print(                "Extrato"                 )
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        while True:
            voltar=int(input("se você deseja retornar para o menu digite 0\n"))
            if voltar == 0:
                break
            else:
                continue
    elif opcao=='2':
        valor=float(input("Informe o valor do depósito: "))
        if valor>0:
            saldo+=valor
            extrato+=f"Depósito: R$ {valor:.2f}\n"
            print(extrato)
            while True:
                voltar=int(input("se você deseja retornar para o menu digite 0\n"))
                if voltar == 0:
                        break
                else:
                    continue
        else:
              print("Operação falhou! O valor informado é inválido.")
              while True:
                voltar=int(input("se você deseja retornar para o menu digite 0\n"))
                if voltar == 0:
                    break
                else:
                    continue

    elif opcao=='3':
            valor= float(input("Informe o valor do saque: "))
            excedeu_saldo=valor>saldo
            excedeu_limite=valor>limite  
            excedeu_saques=numero_saques>= LIMITE_SAQUES
            if saldo==0:
               print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
               print("Operação falhou! O valor do saque excedeu o limite.")
            elif excedeu_saques:
               print("Operação falhou! Número máximo de saques excedido.")
            elif valor>0:
               saldo-=valor
               extrato+= f"Saque: R$ {valor:.2f}\n"
               numero_saques+=1
               print("você realizou mais um saque")
            while True:
               voltar=int(input("se você deseja retornar para o menu digite 0\n"))
               if voltar == 0:
                    break
               else:
                    continue
              
               while True:
                    voltar=int(input("se você deseja retornar para o menu digite 0\n"))
               if voltar == 0:
                    break
               else:
                    continue
            else:
                 print("Operação falhou! O valor informado é inválido.")
                 while True:
                    voltar=int(input("se você deseja retornar para o menu digite 0\n"))
                    if voltar == 0:
                        break
                    else:
                        continue
    elif opcao=='4':
        print("Obrigado por usar o banco JG")
        break

    else:
        print("Operação inválida, por favor selicione uma opção válida")