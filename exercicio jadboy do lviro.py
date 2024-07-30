#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
#desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
#para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
capa_de_livro = 24.95
transp_1 = 3.
transpadd = 0.75
n_copias = 60
desconto = 0.4

c_t_por_copia1 = capa_de_livro*n_copias
perc_desconto2 = c_t_por_copia1*desconto
valor_final = c_t_por_copia1-perc_desconto2
c_t_por_exemplar = (transp_1)+(transpadd*(n_copias-1))
resultado = valor_final + c_t_por_exemplar
a = resultado
print(f"O custo total de atacado para 60 cópias é: R$ {a:,.2f}")

#O custo total de atacado para 60 cópias é: 1,119.45 ou em BRL R$ 1.119,45