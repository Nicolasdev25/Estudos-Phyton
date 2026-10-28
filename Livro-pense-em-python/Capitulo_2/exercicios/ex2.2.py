raio = 5
pi = 3.141592653589793

volume = (4 / 3) * pi * (raio ** 3)

print(volume)

# Dados do problema
preco_capa = 24.95
desconto = 0.40
total_copias = 60

# Cálculo do preço de um livro com o desconto
preco_com_desconto = preco_capa * (1 - desconto)

# Custo total dos livros
custo_livros = preco_com_desconto * total_copias

# Custo do transporte: R$ 3,00 pelo primeiro + R$ 0,75 por cada um dos 59 adicionais
custo_transporte = 3.00 + (total_copias - 1) * 0.75

# Custo total de atacado
custo_total = custo_livros + custo_transporte

print(f"O custo total de atacado para {total_copias} cópias é: R$ {custo_total:.2f}")
