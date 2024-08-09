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
    global nome_completo
    global senha
    global email
    global cpf
    global senha
    global repetirsenha

    opcao = 0
    saldo = 0.00
    extrato = ""
    limite = 500.00
    numero_saques = 0
    limite_saques = 3
    cliente = []
    conta = []
    cod = 0
    cpf = 0
    cod_usuario = ""
    nome_de_usuario = ""
    senha = ""
    email = ""
    senha = ""
    repetirsenha = ""

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
    print("\nSaldo: R$ "+ fsaldo+".")
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
    global fvalor
    global fsaldo
    global z
    z = ""

    while1 = 0
    while while1 == 0:
        valor = input("\nInforme o valor do depósito: ")
        if valor.isdigit() == True:
            valor = float(valor)
        else:
            if valor.find(",") > 0:
                #No VSCode não estava funcionando a função replace()
                fvalor = valor
                x = len(valor)
                y = valor.find(",")
                z = valor[0:y] + "."+ valor[y+1:x]
                valor = float(z)

            elif valor.find(".") > 0:
                valor = float(valor)

            else:
                print("\nDigite apenas valores númericos")
                continue
        if valor > 0:
            saldo += float(valor)
            fsaldo = str(saldo)
            print(fsaldo)
            if fsaldo.find(","):
                x = len(fsaldo)
                y = fsaldo.find(".")
                z = fsaldo[0:y] + ","+ fsaldo[y+1:x]
                fsaldo = z
            extrato += "Depósito: R$ "+fvalor+"."
            print("\nDepósito: R$ "+fvalor+", seu novo saldo agora é: R$ "+fsaldo+".")
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
    global conta
    global cliente
    global excedeu_saldo
    global extrato
    global fsaldo
    global fvalor
    global limite
    global limite_saques
    global numero_saques
    global saldo

    fsaldo = ""
    fvalor = ""

    while1 = 0
    while while1 == 0:
        valor = input("\nInforme o valor do saque: ")
        if valor.isdigit() == True:
            valor = float(valor)
        else:
            if valor.find(",") > 0:
                #No VSCode não estava funcionando a função replace() para alterar letra
                fvalor = valor
                x = len(valor)
                y = valor.find(",")
                z = valor[0:y] + "."+ valor[y+1:x]
                valor = float(z)
            else:
                print("\nDigite apenas valores númericos")
                continue
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if saldo == 0:
            while2 = 0
            if saldo.find(","):
                x = len(saldo)
                y = saldo.find(".")
                z = saldo[0:y] + ","+ saldo[y+1:x]
                fsaldo = z
            print("Operação falhou! Você não tem saldo.  Saldo: R$ " + fsaldo)
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
            print("\nOperação falhou! Você só pode realizar o saque de até R$500,00 por vez.")
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
                #Sair dos 2 loops
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
            if valor.find("."):
                x = len(valor)
                y = valor.find(".")
                z = valor[0:y] + ","+ valor[y+1:x]
                fvalor = z
            extrato += "\nSaque: R$ " +fvalor+"."
            valores = "R$ "+fvalor +"."
            #valores = f"R$ {valor:.2f}."
            numero_saques += 1
            saquesrestantes = limite_saques - numero_saques
            print("\nVocê sacou "+valores+" Seu novo saldo agora é: R$"+fsaldo+".")
            #print("\nVocê sacou",valores, " Seu novo saldo agora é:", f"R$ {saldo:.2f}.")
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

def recuperar_senha(usuarios):
    print(f"\nCPF: {cpf}")
    nome_completo = input('Nome Completo: ')
    email = input('E-mail: ')
    usuario = filtrar_nome_completo_e_email(nome_completo, email, senha, usuarios)
    if usuario:
        print(f'\nSenha: {usuario["Senha"]}')
        print("Isso é considerado uma falha de segurança e é considerado uma prática ruim, está aqui apenas para fins didáticos")
        
        while2 = 0
        while while2 == 0:
            print("\nO que você deseja fazer agora?")
            voltar = input("Fazer Login digite '0', Tela de Boas-Vindas digite '1' Encerrar digite '2': ")
            if voltar.isdigit() == True:
                voltar = int(voltar[0])
            else:
                if voltar.find(",") > 0 or voltar.find(".") > 0:
                    voltar = int(voltar[0])
                else:
                    print("\nDigite apenas valores númericos")
                    voltar = 100
            if voltar == 0:
                Logar(usuarios)
            elif voltar == 1:
                return
            else:
                exit()

def Logar(usuarios):
    global cliente
    global conta
    global cod_cliente
    global cod_conta
    global nome_de_usuario
    global senha
    global email
    global login
    global inicio
    global cpf
    global teste
    teste = ""

    login = """

    \n\n==========================================
    Banco JG Digital

                      LOGIN

    ==========================================
    Usuário:[                    ]
      Senha:[                    ]
    ==========================================
    Email ou cpf: """

    while True:
        cpf = input(login)
        email = cpf
        usuario = filtrar_email_ou_cpf(cpf, email, usuarios)
        while True:
            if usuario:
                senha = input("    Senha: ")
                usuario = filtrar_email_ou_cpf_e_senha(cpf, email, senha, usuarios)
                if usuario:
                    Main()
                else:
                    print("\nSenha incorreta.")
                    while2 = 0
                    while while2 == 0:
                        voltar = input("Tentar Novamente digite '0', Recuperar a senha digite '1'. Encerrar digite '2': ")
                        if voltar.isdigit() == True:
                            voltar = int(voltar[0])
                        else:
                            if voltar.find(",") > 0 or voltar.find(".") > 0:
                                voltar = int(voltar[0])
                            else:
                                print("\nDigite apenas valores númericos")
                                voltar = 100
                        if voltar == 0:
                            Logar(usuarios)
                        elif voltar == 1:
                            recuperar_senha(usuarios)
                        elif voltar == 2:
                            Sair()
                        else:
                            continue
            else:
                print("Usuário não cadastrado.")
                while2 = 0
                while while2 == 0:
                    print("\nO que você deseja fazer?")
                    voltar = input("Tentar Novamente digite '0', Cadastrar-se digite '1'. Encerrar digite '2': ")
                    if voltar.isdigit() == True:
                        voltar = int(voltar[0])
                    else:
                        if voltar.find(",") > 0 or voltar.find(".") > 0:
                            voltar = int(voltar[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            voltar = 100
                    if voltar == 0:
                        Logar(usuarios)
                    elif voltar == 1:
                        Cadastrar(usuarios)
                    else:
                        exit()

def Cadastrar(usuarios):
    global cadastro
    global cod
    global caracteres_permitidos_no_email
    global caracteres_permitidos_no_nome
    global nome_completo_resultante
    global emailresultante
    global caracteres_nao_permitidos_no_nome
    global string_1

    caracteres_permitidos_no_email = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caracteres_permitidos_no_nome = ['\'', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    caracteres_nao_permitidos_no_nome = ""
    nome_completo_resultante = ""
    string_1 = ""
    cod = 0
    cadastro = """
    

    ==========================================
    Banco JG Digital

                    CADASTRO

    ==========================================
              CPF:[                    ]
    Nome Completo:[                    ]
            Email:[                    ]
            Senha:[                    ]
    ==========================================
CPF: """

    while True:
        cpf = input(cadastro)
        usuario = filtrar_cpf(cpf, usuarios)

        while len(usuario) < 11:
            usuario = input("O número do CPF deve conter pelo menos 11 numeros. Tente novamente:\nSenha:")            
        while usuario.isalpha():
            usuario = input("O número do CPF não deve conter outros caracteres além de número. Tente novamente:\nSenha:")
        while usuario.isalnum():
            usuario = input("A senha deve conter pelo menos um caracter especial. Tente novamente:\nSenha:")    
        
        if usuario:
            while2 = 0
            while while2 == 0:
                print("\nCPF já cadastrado. O que você deseja fazer?")
                voltar = input("Fazer Login digite '0', Recuperar a Senha digite '1'. Encerrar digite '2': ")
                if voltar.isdigit() == True:
                    voltar = int(voltar[0])
                else:
                    if voltar.find(",") > 0 or voltar.find(".") > 0:
                        voltar = int(voltar[0])
                    else:
                        print("\nDigite apenas valores númericos")
                        voltar = 100
                if voltar == 0:
                    Logar(usuarios)
                elif voltar == 1:
                    recuperar_senha(usuarios)
                elif voltar == 2:
                    Sair()
                else:
                    continue
        

        while True:
            nome_completo = input('Nome Completo: ')
            converter_string_em_lista(nome_completo)

            lista1 = []
            lista1 = lista

            caracteres_nao_permitidos_no_nome = [x for x in lista1 if x not in caracteres_permitidos_no_nome]

            if len(caracteres_nao_permitidos_no_nome) == 0:
                converter_lista_em_string(lista1)
                nome_completo_resultante = string

                global buscar_espaco
                global buscar_espaco_1
                global buscar_depois_do_espaco
                global buscar_depois_do_espaco_1
                
                buscar_espaco = nome_completo_resultante.find(" ")
                try: buscar_espaco_1 = nome_completo_resultante[buscar_espaco]
                except: buscar_espaco = 0

                buscar_depois_do_espaco = buscar_espaco+1
                try: buscar_depois_do_espaco_1 = nome_completo_resultante[buscar_depois_do_espaco]
                except: buscar_depois_do_espaco = 0

                if buscar_espaco > 0 and buscar_depois_do_espaco > 0:
                    break
                else:
                    print("\nVocê não digitou seu nome completo, digite seu nome completo.")
            else:
                print("\nVocê digitou caracteres inválidos.")
                continue

        while True:
            email = input('E-mail: ')
            converter_string_em_lista(email)

            lista1 = []
            lista1 = lista

            emailresultante = [x for x in lista1 if x not in caracteres_permitidos_no_email]

            if email.find("@") > 0 and email.find(".com") > 0 and email[email.find(".com")-1] != "@":
                break
            elif email.find("@") > 0 and email.find(".com.br") > 0 and email[email.find(".com")-1] != "@":
                break  
            else:
                print("\nO domínio do e-mail não foi informado ou não é aceito. Exemplo: @dominio.com ou @dominio.com.br")
                continue

        while True:
            senha = str(input("""Digite uma senha com os seguintes critérios:"
- Ao menos 8 digitos
- Ao menos uma letra MAIÚSCULA(A à Z)
- Ao menos um número de (0 à 9)
- Ao menos um caractere especial(! @ # $ % ¨ & *)\n
Senha:"""))

            while len(senha) <= 7:
                senha = input("A senha deve conter pelo menos 8 caracteres. Tente novamente:\nSenha:")            
            while senha.islower():
                senha = input("A senha deve conter pelo menos uma letra MAIUSCULA. Tente novamente:\nSenha:")
            while senha.isupper():
                senha = input("A senha deve conter pelo menos uma letra MINUSCULA. Tente novamente:\nSenha:")
            while senha.isalpha():
                senha = input("A senha deve conter pelo menos um número. Tente novamente:\nSenha:")
            while senha.isalnum():
                senha = input("A senha deve conter pelo menos um caracter especial. Tente novamente:\nSenha:")    
            repetirsenha = input("Repita a senha para confirmar: ")
            if senha == repetirsenha:
                cod = cod + 1
                print(f'\nCPF: {cpf}, Nome Completo:{nome_completo}, E-mail: {email}, Senha: {senha}\n')
                
                while2 = 0
                
                while while2 == 0:
                    print("Os dados estão corretos?")  
                    opcao = input("Confirmar Dados digite '0', Editar Dados digite '1'. Encerrar digite '2': ")
                    if opcao.isdigit() == True:
                        if int(opcao) <= int(2):
                            opcao = int(opcao[0])
                        else:
                            print("\nOpção inválida. Digite uma opção válida!")
                            continue
                    else:
                        if opcao.find(",") > 0 or opcao.find(".") > 0:
                            opcao = int(opcao[0])
                        else:
                            print("\nDigite apenas valores númericos")
                            opcao = 100
                            continue

                    if opcao == 0:
                        usuarios.append({"CPF": cpf, "Nome Completo":nome_completo, "E-mail":email, "Senha":senha})
                        print("\nUsuário cadastrado com sucesso!")      
                        while2 = 0
                        while while2 == 0:
                            opcao = input("Fazer Login digite '0', Realizar Novo Cadastro digite '1', Encerrar digite '2': ")
                            if opcao.isdigit() == True:
                                if int(opcao) <= int(2):
                                    opcao = int(opcao[0])
                                else:
                                    print("\nOpção inválida. Digite uma opção válida!")
                                    continue
                            else:
                                if opcao.find(",") > 0 or opcao.find(".") > 0:
                                    opcao = int(opcao[0])
                                else:
                                    print("\nDigite apenas valores númericos")
                                    opcao = 100
                            if opcao == 0:
                                Logar(usuarios)
                            elif opcao == 1:
                                Cadastrar(usuarios)
                            else:
                                continue
                    elif opcao == 1:
                        Cadastrar(usuarios)
                    else:
                        exit()
                    continue
            else:
                print("\nSenhas não conferem")
                continue 

def filtrar_cpf(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def filtrar_nome_completo_e_email(nome_completo, email, senha, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["Nome Completo"] == nome_completo and usuario["E-mail"] == email]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def converter_string_em_lista(string):
    global lista
    lista = []
    for elemento in string:
       lista.append(str(elemento))
    return lista

def converter_lista_em_string(lista):
    global string
    string = ""
    x = 0
    while x < len(lista):
        string = string + lista[x]
        x += 1
    return string

def filtrar_email_ou_cpf(cpf, email, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf or usuario["E-mail"] == email]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def filtrar_email_ou_cpf_e_senha(cpf, email, senha, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if (usuario["CPF"] == cpf or usuario["E-mail"] == email) and usuario["Senha"] == senha]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def Iniciar():

    usuarios = []

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
            Logar(usuarios)
        elif opcao == 2:
            Cadastrar(usuarios)
        else:
            print("\nOperação inválida, por favor selicione uma opção válida.")
            continue
Iniciar()