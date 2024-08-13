# _TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
#item=["Edge","Routers","Patch Cord","UPSServidor","Cabinet Rack","Access Point","Antena","Roteador","Switch"]
item=[]
# _TODO: Crie um loop para solicita os itens ao usuário:

while len(item)<3:
# _TODO: Solicite o item e armazena na variável "item":
# _TODO: Adicione o item à lista "itens":
    a=input("Insira até 3 equipamentos:")
    if a in item:
        print("Item já declarado")
    else:
        item.append(a)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in item:
# Loop que percorre cada item na lista "itens"
    print(f"- {item}")