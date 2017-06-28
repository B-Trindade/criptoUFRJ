"""
Trabalho Final: Mecanismos de Criptografia!
"""

#Inclui a biblioteca com o algoritmo de hashing utilizado
#no modo de assinatura por El Gamal:
from hashlib import sha224

#Tendo a string que desejamos calcular o hash armazenada na variavel
#texto, por exemplo, podemos calcular o seu hash com a seguinte linha:
#h = sha224(texto).hexdigest()


def menu_principal():
    '''Funcao apresenta a possibilidade de escolher entre
       as funcoes de:
       1) Modo de geracao de chaves;
       2) Modo de encriptacao(pura);
       3) Modo de decriptacao(pura);
       4) Modo de assinatura digital(pura);
       5) Modo de verificacao de assinatura(pura);
       6) Modo de assinatura digital e encriptacao (combinados);
       7) Modo de decriptacao e verificacao de assinatura (combinados).'''

    #Apresentando as opcoes ao usuario:
    print("Programa de criptografia inspirado em PGP e GnuPG. Escolha o modo de funcionamento.")
    print(" ")

    print("1) Modo de geracao de chaves")
    print("2) Modo de encriptacao(pura)")
    print("3) Modo de decriptacao(pura)")
    print("4) Modo de assinatura digital(pura)")
    print("5) Modo de verificacao de assinatura(pura)")
    print("6) Modo de assinatura digital e encriptacao (combinados)")
    print("7) Modo de decriptacao e verificacao de assinatura (combinados).")

    print(" ")
    print("Para selecionar uma opcao insira apenas o numero correspondente ao modo desejado!")

    #Recebendo o comando do usuario:
    modus = input()

    #Verificando a escolha do usuario:
    if (modus == 1):
        geracao_chaves_menu()
    elif (modus == 2):
        encriptacao_pura_menu()
    elif (modus == 3):
        decriptacao_pura_menu()
    elif (modus == 4):
        assinatura_digital_pura_menu()
    elif (modus == 5):
        verificacao_assinatura_pura_menu()
    elif (modus == 6):
        comb_assinatura_encriptacao_menu()
    elif (modus == 7):
        comb_decriptacao_verificacao_menu()

    pass

def geracao_chaves_menu():
    '''A funcao oferece a escolha para geracao de chaves de assinatura ou criptografia.'''

    print(" ")
    print("Selecione o tipo de chave desejada:")
    print(" 1) Gerar chaves de assinatura digital")
    print(" 2) Gerar chaves de criptografia")
    print(" ")

    #Recebendo o comando do usuario:
    modus = input()

    #Verificando a escolha do usuario
    if (modus == 1):
        chaves_assinatura()
    else:
        print("Gerar chaves para sistemas El Gamal ou RSA?")
        print(" ")
        print("1) Gerar chaves para criptografia RSA")
        print("2) Gerar chaves para criptografia El Gamal")
        print(" ")

        #Recebendo o comando do usuario:
        modus = input()

        #Novamente, Verificando a escolha do usuario:
        if (modus == 1):
            chaves_RSA()
        else:
            chaves_ElGamal()

    pass

def encriptacao_pura_menu():
    '''A funcao oferece a escolha para encriptacao por RSA ou El Gamal. Obtem o nome
    do arquivo a ser encriptado, alem de receber a chave publica de encriptacao (lida
    de um arquivo ou digitada em hexadecimal manualmente).'''

    print(" ")
    print("Selecione o tipo de encriptacao desejada:")
    print("1) Encriptacao RSA")
    print("2) Encriptacao El Gamal")
    print(" ")

    #Recebendo o comando do usuario:
    modus = input()

    #Obtendo o nome do arquivo a ser encriptado:
    print("Insira, agora, o nome do arquivo a ser encriptado: ")
    arquivo_fonte = input()
    print(" ")

    #Verificando a escolha do usuario:
    if (modus == 1):
        encriptacao_RSA(arquivo_fonte)
    else:
        encriptacao_ElGamal(arquivo_fonte)

    pass

#Missing
def get_key():
    '''Recebe, pelo terminal ou por um arquivo, a chave publica que sera usada.'''

    print("""Deseja informar a chave publica no formato hexadecimal pelo terminal
             ou ler de um arquivo que a contenha?""")

    print("1) Digitar no terminal")
    print("2) Ler de um arquivo")
    print(" ")

    #Obtendo a resposta do usuario:
    modus = input()

    #Verificando a escolha do usuario:
    if (modus == 1):
        #Adequar para que key receba o valor em hexadecimal
        key = input()
    else:
        print("Insira o nome do arquivo para leitura da chave.")
        #Fazer codigo capaz de ler valores de arquivos.

    return key

def decriptacao_pura_menu():
    '''A funcao oferece a escolha para decriptacao por RSA ou El Gamal. Obtem o nome
    do arquivo a ser decriptado, alem de receber a chave privada de encriptacao (lida
    de um arquivo ou digitada em hexadecimal manualmente). '''

    print(" ")
    print("Selecione o tipo de decriptacao desejada:")
    print("1) Decriptacao RSA")
    print("2) Decriptacao El Gamal")
    print(" ")

    #Recebendo o comando do usuario:
    modus = input()

    #Obtendo o nome do arquivo a ser encriptado:
    print("Insira, agora, o nome do arquivo a ser decriptado: ")
    arquivo_fonte = input()
    print(" ")

    #Verificando a escolha do usuario:
    if (modus == 1):
        decriptacao_RSA(arquivo_fonte)
    else:
        decriptacao_ElGamal(arquivo_fonte)

    pass

def assinatura_digital_pura_menu():
    '''Essa funcao inicia assinatura digital por El Gamal. Recebe os valores do nome
    do arquivo cujo conteudo sera assinado, alem de uma chave privada de assinatura.
    Retorna o valor da chave de assinatura.'''

    print(" ")
    print("Insira o nome do arquivo cujo conteudo sera assinado.")
    arquivo_fonte = input()
    print(" ")
    chave_privada_assinatura = get_key()

    #Evoca a funcao que de fato executa o algoritmo de assinatura digital
    assinatura_digital_pura(chave_privada_assinatura)

    pass

def verificacao_assinatura_pura_menu():
    '''Recebe inicialmente o nome de dois arquivos contendo, respectivamente, o conteudo
    que foi assinado digitalmente e a assinatura propriamente dita. Alem disso, recebe
    a chave publica de verificacao de assinatura (recebida do terminal ou de um arquivo).'''

    print(" ")
    print("Insira o nome do primeiro arquivo.")
    arquivo_assinado = input()
    print("Insira o nome do segundo arquivo")
    arquivo_com_assinatura = input()
    print(" ")
    chave_publica_verificacao = get_key()

    #Evoca a funcao que, de fato, executa a verificaco:
    verificacao_assinatura_pura(chave_publica_verificacao)

    pass

#Missing
def comb_assinatura_encriptacao_menu():
    '''. '''

    pass

#Missing
def comb_decriptacao_verificacao_menu():
    '''.'''

    pass

#
#
#

#Missing
def chaves_assinatura():
    '''.'''

    pass

#Missing
def chaves_RSA():
    '''.'''

    pass

#Missing
def chaves_ElGamal():
    '''.'''

    pass

#Missing
def encriptacao_RSA(arquivo):
    '''.'''
    public_key = get_key()

    pass

#Missing
def encriptacao_ElGamal(arquivo):
    '''.'''
    public_key = get_key()

    pass

#Missing
def decriptacao_RSA(arquivo):
    '''.'''
    private_key = get_key()

    pass

#Missing
def decriptacao_ElGamal(arquivo):
    '''.'''
    private_key = get_key()

    pass

#Missing
def assinatura_digital_pura(chave_privada_assinatura):
    '''.'''

    pass

#Missing
def verificacao_assinatura_pura(chave_publica_verificacao):
    '''.'''

    pass




#Funcoes previamente utilizadas nos trabalhos semanais:
