#Em uma instrução print, o que acontece se voce ommitir um dos parentes ou ambos?
print("Olá, mundo!")  # Correto, imprime a mensagem
print("Olá, mundo!"  # Erro de sintaxe, falta o parêntese de fechamento

#Se estiver tentanto imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
print("Olá, mundo!")  # Correto, imprime a mensagem
print("Olá, mundo!)  # Erro de sintaxe, falta a aspa de fechamento 
print(Olá, mundo!")  # Erro de sintaxe, falta a aspa de abertura
print(Olá, mundo!)  # Erro de sintaxe, falta ambas as aspas
      
#Você pode usar um sinal de menos para fazer um numero negativo como -2. o que acontece se puser um sinal de mais antes de um numero?
#e se escrever assim: 2++2?
print(2 + 2)  # Correto, imprime a soma
print(-2+2)  # Correto, imprime a soma
print(2++2)  # Erro de sintaxe, não é permitido usar dois sinais de mais consecutivos

#Na notação matematica, zeros à esquerda são aceitaveis, como em 02. O que acontece se voce tentar usar isso em python?
print(02)  # Erro de sintaxe, zeros à esquerda não são permitidos em números inteiros

#o que acontece se voce tiver dois valores sem nem um operador entre eles, como em 2 2?
print(2 2)  # Erro de sintaxe, não é permitido ter dois