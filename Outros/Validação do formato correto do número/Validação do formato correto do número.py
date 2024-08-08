import re

def validar_telefone(numero):
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    return "Número de telefone válido." if re.match(padrao, numero) else "Número de telefone inválido."

while True:
    entrada = input("Por favor, insira o número de telefone (ou digite 'sair' para encerrar): ").strip()
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    if entrada:
        print(validar_telefone(entrada))
    else:
        print("Entrada vazia. Por favor, insira um número de telefone.")
  -------------------------------------------------------------------------------------------------------------------------      
        # Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
   
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
   
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
       
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.

# Imprime o resultado:
print(result)

--------------------------------------------------------------------------------------------------
import re

def validar_telefone(numero):
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    return "Número de telefone válido." if re.match(padrao, numero) else "Número de telefone inválido."


entrada = input()
    

print(validar_telefone(entrada))
