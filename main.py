#Autor: Rafael Paranhos
#Projeto: Sistema Eleitoral
#Descrição: Identificar se o cidadão pode votar e se poder armazenar o voto
#Regra de negócio: O cidadão apenas poderá votar em ano par, para poder votar precisa ter pelo menos 16 anos
#e poderá votar até os 70 anos.

candidatos = [['Jasom Momoa', 17], ['The Rock', 22], ['Gisele Bundchen', 13]]
print('Bem-vindo ao sistema eleitoral')
anoVigente = int(input('Qual ano você está? '))
anoNascimento = int(input('Em que ano você nasceu? '))
idade = anoVigente - anoNascimento

if anoNascimento > anoVigente:
    print('Você é do futuro, não pode participar dessa eleição')
if idade >= 110:
    print('Você é um fóssil! Onde fica a fonte da imortalidade?')
elif idade < 15:
    faltaAnos = 16 - idade
    anoVotacao = anoVigente + faltaAnos
    if (anoVotacao % 2) != 0:
        anoVotacao += 1
    print('Você ainda não pode votar, você tem ' + str(idade) + ' anos, você poderá votar em '+ str(anoVotacao))
elif idade >= 70 and idade < 110 :
    print('Você já votou bastante, é um patriota')
elif anoVigente % 2 != 0:
    print('Ano que vem você irá votar')
else:
    print('\nSegue a lista dos candidatos do ano\n')
    for candidato in candidatos:
        print('O nome do candidato é ' + candidato[0] + ' e seu código é ' + str(candidato[1]))
    opcao = int(input('\nDigite o código do candidato que você quer votar: '))

    if opcao == 17:
        print('\nVocê votou no Jason Momoa')
    elif opcao == 22:
        print('\nVocê votou no The Rock')
    elif opcao == 13:
        print('\nVocê votou na Gisele Bundchen')
    else:
        print('Não existe um candidato com esse código, você perdeu seu voto!')


