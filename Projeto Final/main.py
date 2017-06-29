"""
Trabalho Final: Mecanismos de Criptografia!
"""

#Inculi a biblioteca para buscar valores randomicamente em determinado
#formato (ex.: p = random.getrandbits(n) buscara um valor de n bits para p).
import random

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
    arquivo_fonte = str(raw_input())
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

    if (modus == 1):
        #Adequar para que key receba o valor em hexadecimal
        print("Insira o valor de 'n'.")
        key = input()
        #O valor de entrada eh hexadecimal, para transforma-lo em decimal, use:
        # i = (key, 16)
    else:
        print("Insira o nome do arquivo para leitura da chave.")
        nome_arq_ChavePublica = raw_input()

        with open(nome_arq_ChavePublica, 'r') as arq_ChavePublica:
            arq_ChavePublica.read()


        #Fazer codigo capaz de ler valores de arquivos.
        # file_ = open("filename", "r") #mesma coisa de C aqui
                # r para read
                # w para write
                # a para append
                # r+ para ler e escrever
        # para fechar o arquivo, usa-se:
        # file_.close() #so use quando tiver acabado de usar o arquivo completamente
        # uma vez fechado, nao eh possivel abrir de novo durante o programa

        # TUDO QUE VOCE PRECISA SABER PARA MEXER COM ARQUIVO EM PYTHON #
            # utilizando o mesmo file_ como la de cima, use:
            # reading = file_.read() para colocar todo o conteudo do arquivo na string reading
            # reading = file_.read(n) para ler n caracteres do arquivo e armazenar em reading
            # reading = file_.readline(n) para ler o que ta escrito na linha n do arquivo e armazena em reading

            # writing = file_.write("o que vc quiser escrever") para escrever no arquivo - uma unica linha

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
#-----------------------------------------------------------------------------------------------------------------
#

#Missing
def chaves_assinatura():
    '''.'''

    pass

#Missing (hexadecimal converting method)
def chaves_RSA():
    '''Gera tres chaves "n", "e" (publica) e "d" (privada). A cahave "n" e igual ao produto entre
    dois primos de 128 bits "p" e "q".'''

    p,q = 6,6
    #Define dois numeros que certamente sao compostos para que
    #eles caiam no caso de randomizacao para numeros de 128 bits

    while (miller_rabin(p,2) is True):
        p = random.getrandbits(128) #Obtem um valor de 128 bits inteiro
    while (miller_rabin(q,2) is True):
        q = random.getrandbits(128) #Obtem um valor de 128 bits inteiro

    # Nestes casos foi utilizado o algoritmo de
    #Miller-Rabbin ou inves do algoritmo de Lucas
    #devido a sua velocidade de execucao, uma vez que
    #este nao depende de uma fatoracao.

    n = (p * q)
    #Efetua o calculo da chave parcial "n" (publica).
    phi_n = (p-1) * (q-1)
    #Considerando que a ordem de um grupo U(n) sera a ordem de um grupo
    #U(p*q) , o valor phi de n sera o produto das ordens (phi_p e phi_q)
    #dos respectivos primos. Portanto, phi_n = phi_p * phi_q = (p-1)*(q-1).

    e = 2
    while (e < phi_n) and (euclidiano(e, phi_n) is False):
        e += 1
    #Calcula a chave publica "e" de acordo com as devidas restricoes.

    d = euclidiano_estendido(e, phi_n)
    if (d < 0):
        d = modulo(e, phi_n)
    else:
        d = d % phi_n
    #Calcula a chava privada "d" de acordo com o metodo aprendido em sala

    n = converte_para_hexadecimal(n)
    e = converte_para_hexadecimal(e)
    d = converte_para_hexadecimal(d)

    #-------------Fim do algoritmo para a criacao de chaves RSA ----------------

    print(" ")
    print("1) Imprimir os valores gerados no terminal.")
    print("2) Armazenar os valores gerados em dois arquivos (um para cada par de chaves).")
    print(" ")

    #Recebendo o comando do usuario.
    modus = input()

    #Verificando a escolha do usuario:
    if (modus == 1):
        print("Chave Publica: n = " + str(n) + "; e = " + str(e))
        print("Chave Privada: n = " + str(n) + "; d = " + str(d))
        print(" ")

    elif (modus == 2):

        print("Informe o nome do arquivo que ira conter as chaves publicas.")
        nome_arq_ChavePublica = raw_input()
        print(" ")

        print("Informe o nome do arquivo que ira conter as chaves privadas.")
        nome_arq_ChavePrivada = raw_input()
        print(" ")

        with open(nome_arq_ChavePublica, 'w') as arq_ChavePublica:
            arq_ChavePublica.write("n = " + str(n) + '\n')
            arq_ChavePublica.write("e = " + str(e) + '\n')
        arq_ChavePublica.closed

        with open(nome_arq_ChavePrivada, 'w') as arq_ChavePrivada:
            arq_ChavePrivada.write("n = " + str(n) + '\n')
            arq_ChavePrivada.write("d = " + str(d) + '\n')
        arq_ChavePrivada.closed

        print("Arquivos produzidos com sucesso!")
        print("Redirecionando para o menu principal...")

    #-----------------------Fim das opcoes interativas--------------------------

    return menu_principal()

#Missing
def chaves_ElGamal():
    '''.'''
    p,q = 6,6   #Para evitar um processo demorado usa-se o fato de que p = 2q +1
    c,a = 0,0
    g = 2

    while ((p.bit_length() != 256 or q.bit_length() != 255) or (miller_rabin(q,2) is False or miller_rabin(p,2) is False)):
        q = random.getrandbits(255)
        p = 2*q + 1
    while (potenciamodular(g, a , p) == 1):
        g += 1

    a = random.randint(2, p-2)
    c = potenciamodular(g, a, p)

    c = converte_para_hexadecimal(c)
    a = converte_para_hexadecimal(a)
    p = converte_para_hexadecimal(p)
    g = converte_para_hexadecimal(g)

    #----------------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------------------
#Funcoes para resultados intermediarios e adequacao ao formato desejado.
#Nao consituem funcoes chamadas diretamente por uma escolha do usuario,
#entretanto, aparecem dentro de outras funcoes.(NAO PERTENCEM AS FUNCOES PREVIAS)

#Missing
def converte_para_hexadecimal(x):
    '''Recebe um valor inteiro "x" e converte para a base 16 (hexadecimal).'''

    return hexa_x

#Missing
def converte_para_decimal(x):
    '''Recebe um valor na base 16 (hexadecimal) e converte para a base 10 (decimal).'''

    return dec_x


#------------------------------------------------------------------------------------------------------------

#Funcoes previamente utilizadas nos trabalhos semanais:

def miller_rabin(n, b):
    '''.'''

    r,k = 1,0
    q = (m - 1)

    while (q % 2 == 0):
        q = q/2
        k += 1
    l = k
    e = q

    while (q >= 0):
        i = q%2
        if (q == 0): break
        if (i == 1):
            r = (r*a) % m
            q = (q-1) / 2
        else:
            q = q/2
        a = (a*a) % m

    while (k > 0):
        k -= 1

        if (r == m-1) or (k == (l-1) and r == 1):
            return False
        if (k == 0):
            return True

        e = (e*2) % m
        r = (r*r) % m

    pass

def euclidiano(a, b):
    '''Implementa o algoritmo euclidiano para dois valores a e b. Retorna 1 se ha coprimalidade.'''
    while b > 0:
        aux = b
        b = a % b
        a = aux
        if (b == 1):
            return True

    return False

def euclidiano_estendido(a, b):
    '''Implementa o algoritmo euclidiano estendido para dois valores a e b.'''
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1

    while b > 0:
        quociente = a // b

        x = x2 - (x1 * quociente)
        x2 = x1
        x1 = x

        y = y2 - (y1 * quociente)
        y2 = y1
        y1 = y

        aux = b
        b = a % b
        a = aux

        if b != 0:
            true_x = x

    return true_x

#Missing description
def modulo(n,m):
    '''.'''
	resultado = 0
	num = n
	mod = m
	if(num < 0):
		num *= -1
		if(num < mod):
			resultado = mod - num
		else:
			resultado = num % mod
	else:
		result = num % mod
	return result

#Missing description
def inversomodular(a, mod):
    modfixo = mod
    x1, y = 1
    x, y1 = 0
    while a%mod > 0:
        r = a%mod
        q = a/mod
        if r != 0:
            a = mod
            mod = r
            xr = x1
            x1 = x
            x = xr-q*x
            yr = y1
            y1 = y
            y = yr-q*y
    if r == 1:
        while x < 0:
            i = 1
            x = x + modfixo*i
            i = i + 1
        if x > modfixo:
            x = x%modfixo
    return x

#Missing description
def potenciamodular(a, e, mod):
    r = 1
    while e > 0:
        if e%2 == 1:
            r = (r*a)%mod
            e = (e-1)/2
        else:
            e = e/2
        a = (a*a)%mod
    return r

#Missing description
def decriptaElGamal(p, a, s, t): # sendo p o primo parametro publico do El Gamal, a eh o valor calculo nos steps, s e t sao os valores dados para decriptacao do bloco
    slinha = potenciamodular(s, p-1-a, p)
    return (slinha*t)%p

#Missing description
def stepsElGamal(g, h, p):
    m = int((p-1)**0.5) + 1
    j = 0
    gj = [] # lista com os valores de j
    # INICIO DO BABY STEP #
    while j < m:
        print j, (g**j)%p
        gj.append((g**j)%p)
        j = j + 1
    # FIM DO BABY STEP #
    # INICIO DO GIANT STEP #
    glinha = inversomodular(g, p) # calculo o inverso de g
    t = potenciamodular(glinha, m, p) # calculo t usando o RAE IMPAR (pego o ultimo valor)
    i = 0
    while (h*(t**i))%p not in gj: #faco o loop ate achar um valor de h*t^i (mod p) que esteja na lista dos valores de j
        print i, (h*(t**i))%p
        i = i+1
    #print i, (h*(t**i))%p # como o loop acaba quando eu acho o valor, eu printo o valor de i que encontrou o valor e o tal valor
    #print i, gj.index((h*(t**i))%p) # aqui printo i novamente e o valor em que h*t^i (mod p) se encontra na lista
    a = i*m + gj.index((h*(t**i))%p) # que eh o valor que satisfaz a equacao g^a = h (mod p)
    return a
