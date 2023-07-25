def valor_input(operation):
    deposito = float(input(f'\n\ndigite o valor para {operation}: '))
    if deposito <= 0:
        print('\n\nvalor inválido!\n\n')
        return 0.00
    return deposito


def painel():
    extrato = 0.00
    option = '4'
    number_saque = 0
    dep_list = []
    saq_list = []
    max_saque = 500.00
    while option != '0':
        option = input('''
digite os valor para as opções:
[1] depósito;
[2] saque;
[3] saldo;
[0] sair.

Opção: ''')
        if option == '1':
            value = valor_input('depósito')
            dep_list.append(value)
            extrato += value
        elif option == '2':
            value = valor_input('saque')
            if number_saque >= 3 or value > max_saque:
                print('Pode-se sacar 3 vezes por dia um valor máximo de R$500,00')
            elif value > extrato:
                print('não será possível sacar dinheiro por falta de saldo.')
            else:
                saq_list.append(value)
                extrato -= value
                number_saque += 1
        elif option == '3':
            print(f'Extrato é de: R${extrato:.2f}'.replace('.', ','))
            for saq in saq_list:
                print(f'- {saq}'.replace('.', ','))
            for dep in dep_list:
                print(f'+ {dep}'.replace('.', ','))
        elif option == '0':
            print('\n\ntchau!\n\n')
        else:
            print('\n\ndigite uma alternativa válida!\n\n')


if __name__ == '__main__':
    painel()
