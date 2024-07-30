"""Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por
quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e
1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa
para o café da manhã?"""
#Função pra transformar horário decimal no formato de relógio
def transformar_em_horario(horario):
    global relogio
    
    relogio = str(horario/3600)
    ponto = relogio.find(".")
    hora = int(relogio[0:ponto])
    minuto_bruto = float(relogio) - hora
    minuto = round(round(minuto_bruto,2)*60)
    segundo = round((round((minuto_bruto*60),15) - minuto)*60)

    if len(str(hora)) == 1: hora = f"0{hora}"
    else: pass
    if len(str(minuto)) == 1: minuto = f"0{minuto}"
    else: pass
    if len(str(segundo)) == 1: segundo = f"0{segundo}"
    else: pass

    relogio = f"{hora}:{minuto}:{segundo}"
    return relogio

#Saída de casa
#horario_de_saida = (6*3600)+(52*60)
horario_de_saida = input("Informe o horário de saída(formato 00:00): ")
hora_de_saida = horario_de_saida[0:horario_de_saida.find(":")]
minuto_de_saida = horario_de_saida[horario_de_saida.find(":")+1:horario_de_saida.find(":")+3]

if horario_de_saida.find(":",horario_de_saida.find(":")+1)+1 > 0:
    segundo_de_saida = horario_de_saida[horario_de_saida.find(":",horario_de_saida.find(":")+1)+1:horario_de_saida.find(":",horario_de_saida.find(":")+1)+3]
    horario_de_saida = (int(hora_de_saida)*3600)+(int(minuto_de_saida)*60)+(int(segundo_de_saida))
else:
    horario_de_saida = (int(hora_de_saida)*3600)+(int(minuto_de_saida)*60)

#Tempo no trajeto
km1 = (8*60)+15
km2 = ((7*60)+12)*3
km3 = (8*60)+15

#Chegada em casa
tempo_total = horario_de_saida + km1 + km2 + km3
print(f"Você chegará em casa às {transformar_em_horario(tempo_total)}")