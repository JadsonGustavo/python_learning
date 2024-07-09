# Software Bancário
# O Software permite três operações: depósito, saque e extrato.
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
# Deve listar todos os depósitos e saques na conta.
# Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações".
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

menu = """
==========================================

    Bem vindo ao Banco JG. Digital

==========================================
Escolha uma das opções abaixo de 1 à 4
[1] Extrato
[2] Depositar
[3] Sacar
[4] Sair

==========================================
=>"""

#print(menu)

saldo = 0.00
limite = 500
numero_saques = 0
extrato = ""
limite_saques = 3

while True:
    #Recebe o valor
    opcao = input(menu)
    #Analisa se o valor digitado é númerico
    if opcao.isdigit() == True:
        #transforma o valor digitado apenas no primeiro digito
        opcao = int(opcao[0])
    else:
        #Procura por virgula ou ponto
        if opcao.find(",") > 0 or opcao.find(".") > 0:
            opcao = int(opcao[0])
        else:
            print("\nDigite apenas valores númericos")
            opcao = 100
    if int(opcao) == 1:
        print("\n==========================================")
        print(                "Extrato"                 )
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        while True:
            voltar = input("\nPara voltar ao menu principal digite '0', se deseja encerrar digite '1': ")
            if voltar.isdigit() == True:
                voltar = int(voltar[0])
            else:
                if voltar.find(",") > 0 or voltar.find(".") > 0:
                    voltar = int(voltar[0])
                else:
                    print("\nDigite apenas valores númericos")
                    voltar = 100
            if voltar == 0:
                break
            elif voltar == 1:
                print("\nObrigado por usar o banco JG.")
                exit()
            else:
                continue
    elif opcao == 2:
        while1 = 0
        while while1 == 0:
            valor = input("\nInforme o valor do depósito: ")
            if valor.isdigit() == True:
                valor = float(valor)
            else:
                if valor.find(",") > 0:
                    valor = float(valor.raplace(",","."))
                else:
                    print("\nDigite apenas valores númericos")
                    continue
            if valor > 0:
                saldo += float(valor)
                extrato += f"Depósito: R$ {valor:.2f}"
                print("\nDepósito:", f"R$ {valor:.2f}.", " Seu novo saldo agora é:", f"R$ {saldo:.2f}.")
                while2 = 0
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("\nObrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
            else:
                print("\nOperação falhou! O valor informado é inválido.")
                while2 = 0
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("\nObrigado por usar o banco JG.")
                        exit()
                    else:
                        continue

    elif opcao == 3:
        while1 = 0
        while while1 == 0:
            valor = input("\nInforme o valor do saque: ")
            if valor.isdigit() == True:
                valor = float(valor)
            else:
                if valor.find(",") > 0:
                    valor = float(valor.raplace(",","."))
                else:
                    print("\nDigite apenas valores númericos")
                    continue
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= limite_saques
            
            if saldo == 0:
                while2 = 0
                print("\nOperação falhou! Você não tem saldo." f" Saldo: R$ {saldo:.2f}")
                while while2 == 0:
                    print("\nMenu principal digite '0', encerrar digite '1': ")
                    voltar = input()
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 1:
                        print("\nObrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
            elif excedeu_limite:
                while2 = 0
                print("Operação falhou! Você só pode realizar o saque de até R$500,00.")
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("\nObrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
                    
            elif saldo < valor:
                while2 = 0
                print("\nOperação falhou! Você não tem saldo suficiente para o valor escolhido." f" Saldo: R$ {saldo:.2f}")
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("Obrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
            elif excedeu_saques:
                while2 = 0
                print("\nOperação falhou! Você já realizou o limite de 3 saques diários.")
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100                    
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("Obrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
            elif valor > 0 and valor <= limite:
                while2 = 0
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}.\n"
                valores = f"R$ {valor:.2f}."
                numero_saques += 1
                saquesrestantes = limite_saques - numero_saques
                print("\nVocê sacou",valores, " Seu novo saldo agora é:", f"R$ {saldo:.2f}.")
                if saquesrestantes == 1:
                    print("Você ainda possui", saquesrestantes,"saque.")
                else:
                    print("Você ainda possui",saquesrestantes,"saques.")                       
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("\nObrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
            else:
                while2 = 0
                print("\nOperação falhou! O valor informado é inválido.")
                while while2 == 0:
                    voltar = input("\nPara realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        while2 = 1
                        pass
                    elif voltar == 1:
                        while1 = 1
                        while2 = 1
                        pass
                    elif voltar == 2:
                        print("\nObrigado por usar o banco JG.")
                        exit()
                    else:
                        continue
    elif opcao == 4:
        print("\nObrigado por usar o banco JG.")
        exit()

    else:
        print("\nOperação inválida, por favor selicione uma opção válida.")
        continue