# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar uma mensagem abaixo:

nome_heroi = 'Spider-Man'
experiencia = int(input('Qual o nivel atual da experiencia do heroi? '))

if experiencia < 1000:
    experiencia = 'Ferro'
elif experiencia > 1001 and experiencia < 2000:
    experiencia = 'Bronze'
elif experiencia > 2001 and experiencia < 5000:
    experiencia = 'Prata'
elif experiencia > 5001 and experiencia < 7000:
    experiencia = 'Ouro'
elif experiencia > 7001 and experiencia < 8000:
    experiencia = 'Platina'
elif experiencia > 8001 and experiencia < 9000:
    experiencia = 'Ascendente'
elif experiencia > 9001 and experiencia < 10000:
    experiencia = 'Imortal'
else:
    experiencia = 'Radiante'

print(f'O heroi de nome {nome_heroi} está no nível de {experiencia}')