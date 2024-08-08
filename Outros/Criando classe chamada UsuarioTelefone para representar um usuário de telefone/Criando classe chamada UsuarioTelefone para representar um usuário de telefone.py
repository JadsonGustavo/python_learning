import re

class UsuarioTelefone:
    def __init__(self, nome, telefone, plano):
        self._nome = nome
        self._telefone = None  # Atributo protegido
        self._plano = plano
        self.set_telefone(telefone)

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self.set_telefone(valor)

    @property
    def plano(self):
        return self._plano

    def set_telefone(self, telefone):
        if self.validar_telefone(telefone):
            self._telefone = telefone
        else:
            raise ValueError("Número de telefone inválido. Formato esperado: (XX) 9XXXX-XXXX")

    @staticmethod
    def validar_telefone(telefone):
        padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
        return bool(re.match(padrao, telefone))

    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."

# Loop para criar usuários até que um usuário seja criado com sucesso
while True:
    nome = input("Por favor, insira o nome do usuário: ").strip()
    numero = input("Por favor, insira o número de telefone: ").strip()
    plano = input("Por favor, insira o plano do usuário: ").strip()

    try:
        usuario = UsuarioTelefone(nome, numero, plano)
        print(usuario)
        break  # Sai do loop após criar o usuário com sucesso
    except ValueError as e:
        print(e)
        ----------------------------------------------------
        # TODO: Crie uma classe UsuarioTelefone.  
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.


        
    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
      

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

print(usuario)