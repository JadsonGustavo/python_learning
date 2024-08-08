import re

class PlanoTelefone:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self):
        return self._saldo

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, valor):
        self._saldo -= valor

    def verificar_saldo(self):
        if self._saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

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

    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        if self._plano.saldo >= custo:
            self._plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario.telefone} realizada com sucesso. Saldo: ${self._plano.saldo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."

# Entrada do usuário
nome = input("Por favor, insira o nome do usuário: ").strip()
numero = input("Por favor, insira o número de telefone: ").strip()
saldo = float(input("Por favor, insira o saldo do plano: ").strip())

# Criação do objeto usuário e plano
plano = PlanoTelefone(nome, saldo)
usuario = UsuarioTelefone(nome, numero, plano)

# Dados da chamada
destinatario_numero = input("Por favor, insira o número de telefone do destinatário: ").strip()
duracao = float(input("Por favor, insira a duração da chamada em minutos: ").strip())

# Criação do objeto destinatário (simulando)
destinatario = UsuarioTelefone("Destinatário", destinatario_numero, plano)

# Realização da chamada e saída da mensagem
mensagem = usuario.fazer_chamada(destinatario, duracao)
print(mensagem)
