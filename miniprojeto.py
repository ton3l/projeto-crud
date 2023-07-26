"""Mini Projeto: CRUD de funcionários"""
nomes = []
cpf = []
sal = []

while True:
    opção = input('--------- Oxente Sistemas --------\n1 .................Cadastrar Funcionário\n2 ................ Exibir dados do Funcionário\n3 ................ Remover Funcionário\n4 ................ Exibir todos os funcionários cadastrados\n0 ............... Sair\n')

    if opção == '0':#Fechar o sistema
        break

    if opção == '1':#Cadastro de funcionários
        nomes.append(input('Digite seu nome: '))
        cpf.append(input('Digite seu cpf: '))
        sal.append(float(input('Digite seu salário: ')))

    if opção == '2':#Verificação de dados de um funcionário
        fun = int(input('Digite o número do funcionário: '))
        if fun > 0 and fun <= len(nomes):
            print(nomes[fun - 1], cpf[fun - 1], sal[fun - 1])
        else:
            print('Esse funcionário não consta no sistema.')
        

    if opção == '3':#Apagar dados de um funcionário do sistema
        fun = int(input('Digite um funcionário a ser removido: '))
        del(nomes[fun - 1])
        del(cpf[fun - 1])
        del(sal[fun - 1])
    
    if opção == '4':#Verificação de dados de todos os funcionários
        for funcionario in nomes:
            print(f'Nome: {nomes[funcionario]}\nCPF: {cpf[funcionario]}\nSalário: {sal[funcionario]}\n')
