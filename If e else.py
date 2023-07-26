nota1 = int(input('Digite suas notas: '))
nota2 = int(input())
nota3 = int(input())
nota4 = int(input())

media = float((nota1 + nota2 + nota3 + nota4) / 4)

if media >= 70:
    print(f'Você passou com uma media de {media:.1f}')
elif media < 70 and media >= 50:
    print(f'Você foi para a final com uma média de {media:.1f}')
else:
    print(f'Você ficou de recuperação com uma media de {media:.1f}')
