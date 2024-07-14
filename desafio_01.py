def Variaveis():
    global opcao
    global extrato
    global saldo
    global limite
    global numero_saques
    global limite_saques
    global cliente
    global conta
    global cod_cliente
    global cod_conta
    global nome_de_usuario
    global Nome_completo
    global senha
    global email

    opcao = 0
    saldo = 0.00
    extrato = ""
    limite = 500.00
    numero_saques = 0
    limite_saques = 3
    cliente = []
    conta = []
    cod_usuario = ""
    nome_de_usuario = ""
    senha = ""
    email = ""
    
def Menu():
    menu = """
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
    opcao = input(menu)
    return opcao

def Extrato():
    global extrato
    global saldo
    global limite
    global numero_saques
    global limite_saques
    global cliente
    global conta

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
            Sair()
        else:
            continue

def Deposito():

    global extrato
    global saldo
    global limite
    global numero_saques
    global limite_saques
    global cliente
    global conta

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
                    Sair()
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

def Saque():
    global extrato
    global saldo
    global limite
    global numero_saques
    global limite_saques
    global cliente
    global conta

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
            print("Operação falhou! Você não tem saldo." f" Saldo: R$ {saldo:.2f}")
            while while2 == 0:
                print("Menu principal digite '0', encerrar digite '1': ")
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
                    Sair()
                else:
                    continue
        elif excedeu_limite:
            while2 = 0
            print("\nOperação falhou! Você só pode realizar o saque de até R$500,00.")
            while while2 == 0:
                voltar = input("Para realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
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
                    Sair()
                else:
                    continue
        elif saldo < valor:
            while2 = 0
            print("\nOperação falhou! Você não tem saldo suficiente para o valor escolhido." f" Saldo: R$ {saldo:.2f}")
            while while2 == 0:
                voltar = input("Para realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
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
                    Sair()
                else:
                    continue
        elif excedeu_saques:
            while2 = 0
            print("\nOperação falhou! Você já realizou o limite de 3 saques diários.")
            while while2 == 0:
                voltar = input("Para realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
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
                    Sair()
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
                voltar = input("Para realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
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
                    Sair()
                else:
                    continue
        else:
            while2 = 0
            print("\nOperação falhou! O valor informado é inválido.")
            while while2 == 0:
                voltar = input("Para realizar a operação novamente digite '0', menu principal digite '1', encerrar digite '2': ")
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
                    Sair()
                else:
                    continue

def Sair():
    print("\nObrigado por usar o banco JG.")
    exit()

def Inicio():
    global cliente
    global conta
    global cod_cliente
    global cod_conta
    global nome_de_usuario
    global senha
    global email
    global login
    global inicio

    inicio = """
    ==========================================

        Bem vindo ao Banco JG Digital

    ==========================================
    [1] Fazer Login
    [2] Cadastrar
    ==========================================
    =>"""
    opcao = input(inicio)
    return opcao

def Login():
    global cliente
    global conta
    global cod_cliente
    global cod_conta
    global nome_de_usuario
    global senha
    global email
    global login
    global inicio

    login = """

    ==========================================
    Banco JG Digital

                      LOGIN

    ==========================================
    Usuário:[                    ]
      Senha:[                    ]
    ==========================================
    Email ou CPF: """
    
    nome_de_usuario = input(login)
    return nome_de_usuario

def Cadastro():
    global cliente
    global conta
    global cod_cliente
    global cod_conta
    global nome_de_usuario
    global senha
    global email
    global login
    global inicio
    global cadastro
    global Nome_completo
    cadastro = """

    ==========================================
    Banco JG Digital

                    CADASTRO

    ==========================================
    Nome Completo:[                    ]
              CPF:[                    ]
            Email:[                    ]
            Senha:[                    ]
    ==========================================
    Nome Completo: """
    
    Nome_completo = input(cadastro)
    return Nome_completo

def Cadastrar():

    Variaveis()

    while True:
        #Recebe o valor
        Nome_completo = Login()
        #Analisa se o valor digitado é númerico
        
        if Nome_completo.isdigit() == True:
            opcao = int(opcao)

        elif Nome_completo.find("@") > 0:
            if Nome_completo.find(".com") <= 0 or Nome_completo.find(".com.br") <= 0:
                print("Email inválido")
            else:
                print("\nDigite apenas valores númericos")
                Nome_completo = 100
        if Nome_completo == 1:
            Main()
        elif Nome_completo == 2:
            Cadastrar()
        else:
            print("\nOperação inválida, por favor selicione uma opção válida.")
            continue
    
def Acessar():

    Variaveis()

    while True:
        #Recebe o valor
        nome_de_usuario = Login()
        #Analisa se o valor digitado é númerico
        
        if nome_de_usuario.isdigit() == True:
            opcao = int(opcao)

        elif nome_de_usuario.find("@") > 0:
            if nome_de_usuario.find(".com") <= 0 or nome_de_usuario.find(".com.br") <= 0:
                print("Email inválido")
            else:
                print("\nDigite apenas valores númericos")
                nome_de_usuario = 100
        if nome_de_usuario == 1:
            Main()
        elif nome_de_usuario == 2:
            Cadastrar()
        else:
            print("\nOperação inválida, por favor selicione uma opção válida.")
            continue

def Iniciar():

    Variaveis()

    while True:
        #Recebe o valor
        opcao = Inicio()
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
            Acessar()
        elif opcao == 2:
            Cadastrar()
        else:
            print("\nOperação inválida, por favor selicione uma opção válida.")
            continue

Iniciar()    

def Cadastro():
    print("")

def Usuarios():
    print("")

def ContaBancaria():
    print("")

def Main():

    Variaveis()

    while True:
        #Recebe o valor
        opcao = Menu()
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
            Extrato()
        elif opcao == 2:
            Deposito()
        elif opcao == 3:
            Saque()
        elif opcao == 4:
            Sair()
        else:
            print("\nOperação inválida, por favor selicione uma opção válida.")
            continue

Main()