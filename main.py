def validar_alistamento(sexo,idade):
    if sexo.upper() == 'M' and idade >= 18:
        return True , "ALISTAMENTO OBRIGATÓRIO"
    elif sexo.upper() == 'M' and idade < 18:
        return False, "AINDA NÃO TEM A IDADE MÍNIMA"
    else :
        return False ," AISTAMENTO NÃO OBRIGATÓRIO PARA ESSE PERFIL"

def exibir_menu():
        print ('-=-' * 30)
        print('    TRIAGEM MILITAR    ')
        print ('-=-'* 30)

        nome = (input('Qual é o seu nome?'))
        sexo = (input('Qual é o seu sexo? (M/F)'))
        idade = int(input('Quantos anos você tem?'))

        resultado = validar_alistamento (sexo,idade)

        print(f'Olá {nome}')
        print(f'O resultado foi{resultado}')

exibir_menu()
