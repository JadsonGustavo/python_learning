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
-----------------------------------------------------------------------------------------
# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:

# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':

# TODO: Verifique se o saldo do plano é suficiente para a chamada.

# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.

# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:

# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:


# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))