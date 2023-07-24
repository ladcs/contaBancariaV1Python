def painel():
    option = '4'
    while option != '0':
        option = input('''digite os valor para as opções:
1) depósito;
2) saque;
3) saldo;
0) sair.
''')
        if option == '1':
            print(f'ta lento option {option}')
        elif option == '2':
            print(f'ta lento option {option}')
        elif option == '3':
            print(f'ta lento option {option}')
        elif option == '0':
            print('tchau!')
        else:
            print('digite uma alternativa válida!')


if __name__ == '__main__':
    painel()
