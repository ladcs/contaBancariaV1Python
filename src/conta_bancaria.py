def valor_to_change_saldo(operation):
    deposito = float(input(f'\n\ndigite o valor para {operation}: '))
    if deposito <= 0:
        print('\n\nvalor inválido!\n\n')
        return 0.00
    return deposito


def painel():
    extrato = 0.00
    option = '4'
    while option != '0':
        option = input('''
                       
digite os valor para as opções:
[1] depósito;
[2] saque;
[3] saldo;
[0] sair.

Opção: ''')
        if option == '1':
            extrato += valor_to_change_saldo('depósito')
        elif option == '2':
            extrato -= valor_to_change_saldo('saque')
        elif option == '3':
            print(f'Extrato é de: R${extrato:.2f}'.replace('.', ','))
        elif option == '0':
            print('\n\ntchau!\n\n')
        else:
            print('\n\ndigite uma alternativa válida!\n\n')


if __name__ == '__main__':
    painel()
