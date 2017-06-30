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
       3) Modo de decriptamento(pura);
       4) Modo de assinatura digital(pura);
       5) Modo de verificacao de assinatura(pura);
       6) Modo de assinatura digital e encriptacao (combinados);
       7) Modo de decriptamento e verificacao de assinatura (combinados).'''

    #Apresentando as opcoes ao usuario:
    print("Programa de criptografia inspirado em PGP e GnuPG. Escolha o modo de funcionamento.")
    print(" ")

    print("1) Modo de geracao de chaves")
    print("2) Modo de encriptacao(pura)")
    print("3) Modo de decriptamento(pura)")
    print("4) Modo de assinatura digital(pura)")
    print("5) Modo de verificacao de assinatura(pura)")
    print("6) Modo de assinatura digital e encriptacao (combinados)")
    print("7) Modo de decriptamento e verificacao de assinatura (combinados).")

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
        decriptamento_puro_menu()
    elif (modus == 4):
        assinatura_digital_pura_menu()
    elif (modus == 5):
        verificacao_assinatura_pura_menu()
    elif (modus == 6):
        comb_assinatura_encriptacao_menu()
    elif (modus == 7):
        comb_decriptamento_verificacao_menu()

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
        chaves_ElGamal()
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

def decriptamento_puro_menu():
    '''A funcao oferece a escolha para decriptamento por RSA ou El Gamal. Obtem o nome
    do arquivo a ser decriptado, alem de receber a chave privada de encriptacao (lida
    de um arquivo ou digitada em hexadecimal manualmente). '''

    print(" ")
    print("Selecione o tipo de decriptamento desejada:")
    print("1) Decriptamento RSA")
    print("2) Decriptamento El Gamal")
    print(" ")

    #Recebendo o comando do usuario:
    modus = input()

    #Obtendo o nome do arquivo a ser encriptado:
    print("Insira, agora, o nome do arquivo a ser decriptado: ")
    arquivo_fonte = raw_input()
    print(" ")

    #Verificando a escolha do usuario:
    if (modus == 1):
        decriptamento_RSA(arquivo_fonte)
    else:
        decriptamento_ElGamal(arquivo_fonte)

    pass

def assinatura_digital_pura_menu():
    '''Essa funcao inicia assinatura digital por El Gamal. Recebe os valores do nome
    do arquivo cujo conteudo sera assinado, alem de uma chave privada de assinatura.
    Retorna o valor da chave de assinatura.'''

    print(" ")
    print("Insira o nome do arquivo cujo conteudo sera assinado.")
    arquivo_fonte = raw_input()
    print(" ")

    #Evoca a funcao que de fato executa o algoritmo de assinatura digital
    assinatura_digital_pura(arquivo_fonte)

    pass

def verificacao_assinatura_pura_menu():
    '''Recebe inicialmente o nome de dois arquivos contendo, respectivamente, o conteudo
    que foi assinado digitalmente e a assinatura propriamente dita. Alem disso, recebe
    a chave publica de verificacao de assinatura (recebida do terminal ou de um arquivo).'''

    print(" ")
    print("Insira o nome do arquivo assinado.")
    arquivo_assinado = raw_input()
    print("Insira o nome do arquivo com a assinatura.")
    arquivo_com_assinatura = raw_input()
    print(" ")

    #Evoca a funcao que, de fato, executa a verificaco:
    verificacao_assinatura_pura(arquivo_assinado, arquivo_com_assinatura)

    pass

#Missing
def comb_assinatura_encriptacao_menu():
    '''. '''

    print("Opcao indisponivel. Trabalho incompleto")
    return menu_principal()

#Missing
def comb_decriptamento_verificacao_menu():
    '''.'''

    print("Opcao indisponivel. Trabalho incompleto")
    return menu_principal()

#
#--------------------------------------------------------------------------------------------
#Funcoes chamadas diretamente pelos menus. Servem para realizar os algoritmos para cada uma
# das opcoes de menu.

#Concluded
def chaves_RSA():
    '''Gera tres chaves "n", "e" (publica) e "d" (privada). A cahave "n" e igual ao produto entre
    dois primos de 128 bits "p" e "q".'''

    p,q = 10,10
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
    
    #Calcula a chava privada "d" de acordo com o metodo aprendido em sala

    n = converte_para_hexadecimal(n)
    while (len(n) < 64):
        n = '0' + str(n)

    e = converte_para_hexadecimal(e)
    while (len(e) < 64):
        e = '0' + str(e)

    d = converte_para_hexadecimal(d)
    while (len(d) < 64):
        d = '0' + str(d)

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
            arq_ChavePublica.write(str(n) + '\n')
            arq_ChavePublica.write(str(e) + '\n')
        arq_ChavePublica.closed

        with open(nome_arq_ChavePrivada, 'w') as arq_ChavePrivada:
            arq_ChavePrivada.write(str(n) + '\n')
            arq_ChavePrivada.write(str(d) + '\n')
        arq_ChavePrivada.closed

        print("Arquivos produzidos com sucesso!")
        print("Redirecionando para o menu principal...")

    #-----------------------Fim das opcoes interativas--------------------------

    return menu_principal()

#Concluded
def chaves_ElGamal():
    '''.'''
    p,q = 6,6   #Para evitar um processo demorado usa-se o fato de que p = 2q +1
    c,a = 0,0
    g = 2

    print("Calculando...")
    while ((p.bit_length() != 256 or q.bit_length() != 255) or (miller_rabin(q,2) is True) or (miller_rabin(p,2) is True)):
        q = random.getrandbits(255)
        p = 2*q + 1

    #Calculamos "c" de forma que "g" elevado a "a" seja congruente a "c" mod p e c != 1
    #Assim, temos um "g" gerador de U(p) e um "p" primo de forma que U(p) e ciclico.
    
    while (potenciamodular(g, q , p) == 1):
        g += 1

    a = random.randint(2, p-2)
    c = potenciamodular(g, a, p)

    c = converte_para_hexadecimal(c)
    while(len(c) < 64):
        c = '0' + str(c)

    a = converte_para_hexadecimal(a)
    while(len(a) < 64):
        a = '0' + str(a)

    p = converte_para_hexadecimal(p)
    while(len(p) < 64):
        p = '0' + str(p)

    g = converte_para_hexadecimal(g)
    while(len(g) < 64):
        g = '0' + str(g)

    #----------- Fim do algoritmo para a criacao de chaves El Gamal ------------

    print(" ")
    print("1) Imprimir os valores gerados no terminal.")
    print("2) Armazenar os valores gerados em dois arquivos (um para cada par de chaves).")
    print(" ")

    #Recebendo o comando do usuario.
    modus = input()

    #Verificando a escolha do usuario:
    if (modus == 1):
        print("Chave Publica: p = " + str(p))
        print("               g = " + str(g))
        print("               c = " + str(c))
        print(" ")
        print("Chave Privada: a = " + str(a))
        print(" ")

    elif (modus == 2):

        print("Informe o nome do arquivo que ira conter as chaves publicas.")
        nome_arq_ChavePublica = raw_input()
        print(" ")

        print("Informe o nome do arquivo que ira conter as chaves privadas.")
        nome_arq_ChavePrivada = raw_input()
        print(" ")

        print("""Os valores serao armazenados na seguinte ordem: 'p', 'g' e 'c'.
             Seguidos de 'p', 'g' e 'a' no proximo arquivo.""")

        with open(nome_arq_ChavePublica, 'w') as arq_ChavePublica:
            arq_ChavePublica.write(str(p) + '\n')
            arq_ChavePublica.write(str(g) + '\n')
            arq_ChavePublica.write(str(c) + '\n')
        arq_ChavePublica.closed

        with open(nome_arq_ChavePrivada, 'w') as arq_ChavePrivada:
            arq_ChavePrivada.write(str(p) + '\n')
            arq_ChavePrivada.write(str(g) + '\n')
            arq_ChavePrivada.write(str(a) + '\n')
        arq_ChavePrivada.closed

        print(" ")
        print("Arquivos produzidos com sucesso!")
        print("Redirecionando para o menu principal...")

    #-----------------------Fim das opcoes interativas--------------------------
    return menu_principal()

#Concluded
def encriptacao_RSA(arquivo):
    '''.'''
    n_key,e_key = get_keyRSA()

    print("Insira o nome do novo arquivo encriptado.")
    novo_arquivo = raw_input()
    print(" ")
    
    arquivo_fonte = open(arquivo, 'r')
    encript_arq = open(novo_arquivo, 'w')

    mensagem = arquivo_fonte.readline()  
    while (mensagem != ''):
        
        i = 0
        while (i < len(mensagem)):
            bloco = ord(mensagem[i]) + 10
            bloco = potenciamodular(bloco, e_key, n_key)
            encript_arq.write(str(bloco) + '\n')
            
            i += 1
            
        mensagem = arquivo_fonte.readline()
 
    encript_arq.close()
    arquivo_fonte.close()

    print("Sucesso! Arquivos encriptados.")
    return menu_principal()

#Concluded
def encriptacao_ElGamal(arquivo):
    '''.'''
    p_key,g_key,c_key = get_keyEG()

    print("Insira o nome do novo arquivo encriptado.")
    novo_arquivo = raw_input()
    print(" ")

    arquivo_fonte = open(arquivo, 'r')
    encript_arq = open(novo_arquivo, 'w')

    mensagem = arquivo_fonte.readline()
    while(mensagem != ''):
        i = 0
        while (i < len(mensagem)):

            bloco = ord(mensagem[i]) + 10
            m = random.randint(2, p_key -2)
            o = (bloco * potenciamodular(c_key, m, p_key)) % p_key
            n = potenciamodular(g_key, m, p_key)
            
            encript_arq.write(str(n) + '\n')
            encript_arq.write(str(o) + '\n')
            
            i += 1
        mensagem = arquivo_fonte.readline()
            
    encript_arq.close()
    arquivo_fonte.close()

    print("Sucesso! Arquivos encriptados.")
    return menu_principal()

#Cocluded
def decriptamento_RSA(arquivo):
    '''Recebe um arquivo com conteudo encriptado por RSA'''
    n_key,d_key = get_pkeyRSA()

    print("Insira o nome do novo arquivo decriptado.")
    novo_arquivo = raw_input()
    print(" ")

    arquivo_fonte = open(arquivo, 'r')
    arq_drecriptado = open(novo_arquivo, 'w')

    linha = arquivo_fonte.readline()
    while(linha != ''):
        bloco = linha   
        bloco = potenciamodular(int(bloco), d_key, n_key)
        bloco_decriptado = chr(int(bloco) - 10)

        arq_drecriptado.write(bloco_decriptado)
        linha = arquivo_fonte.readline()

    arquivo_fonte.close()
    arq_drecriptado.close()
    
    return menu_principal()

#Concluded
def decriptamento_ElGamal(arquivo):
    '''.'''
    p_key,g_key,a_key = get_pkeyEG()

    print("Insira o nome do arquivo decriptado.")
    novo_arquivo = raw_input()
    print(" ")

    arquivo_fonte = open(arquivo, 'r')
    arq_drecriptado = open(novo_arquivo, 'w')

    linha_n = arquivo_fonte.readline()
    linha_o = arquivo_fonte.readline()

    while ((linha_n and linha_o) != ''):

        linha_n = potenciamodular((int(linha_n)), p_key-1-a_key, p_key)
        bloco = (linha_n * int(linha_o)) % p_key
        bloco = chr(int(bloco) - 10)

        arq_drecriptado.write(bloco)

        linha_n = arquivo_fonte.readline()
        linha_o = arquivo_fonte.readline()

    arq_drecriptado.close()
    arquivo_fonte.close()

    return menu_principal()

#Missing
def assinatura_digital_pura(arquivo):
    '''.'''
    p_key,g_key,a_key = get_pkeyEG()


    print("Insira o nome para o novo arquivo assinado.")
    novo_arquivo = raw_input()
    print(" ")


    ################################################################################################
    arquivo_fonte = open(arquivo, 'r')

    texto = ''
    linha_texto = arquivo_fonte.readline()
    while (linha_texto != ''):
        i = 0

        while(i < len(linha_texto)):
            bloco = ord(linha_texto[i])
            ConvertToBin = lambda x: format(x, 'b')
            bloco = ConvertToBin(bloco)
            texto += str(bloco)
            i += 1

        linha_texto = arquivo_fonte.readline()
    arquivo_fonte.close()
    ################################################################################################


    k = random.randint(1, p_key - 2)
    while (euclidiano(k, p_key -1) is False):
        k = random.randint(1, p_key - 2)
    
    r = potenciamodular(g_key, k, p_key)
    inverso_k = euclidiano_estendido(k, p_key-1)

    ConvertToBin = lambda x: format(x, 'b')
    h_text = sha224(texto).hexdigest()
    h = int(h_text, 16)
    #Embaralha o texto (composicao de blocos) segundo o metodo sha224, retornando um valor em hexadecimal

    #Obtem o primeiro par da assinatura dada por (r,s).
     
    s = (inverso_k * int(h - a_key * r)) % (p_key -1)

    r = converte_para_hexadecimal(int(r))
    while(len(r) < 64):
        r = '0' + str(r)

    s = converte_para_hexadecimal(int(s))
    while(len(s) < 64):
        s = '0' + str(s)
    
    ############################### Fim do calculo do par assinatura #################################

    with open(novo_arquivo, 'w') as arquivo_assinado:
        arquivo_assinado.write(str(r) + '\n')
        arquivo_assinado.write(str(s) + '\n')
    arquivo_assinado.closed

    print("Sucesso na assinatura do arquivo!")
    print("Retornando ao menu principal...")

    return menu_principal()

#Missing
def verificacao_assinatura_pura(arq_assinado, arq_assinatura):
    '''.'''
    p_key,g_key,c_key = get_keyEG()

    with open(arq_assinatura, 'r') as arquivo_assinatura:
        r = arquivo_assinatura.readline()
        r = r[0:-1]
        r = int(r, 16)

        s = arquivo_assinatura.readline()
        s = s[0:-1]
        s = int(s, 16)
    arquivo_assinatura.closed

    if  (r < 1) or ( r > (p_key - 1) ):
        print(" ")
        print("Essa assinatura e invalida. Assinatura rejeitada.")  
    else:
        #Verificacao 1:
        v1 = (potenciamodular(c_key, int(r), int(p_key)) * potenciamodular(int(r), int(s) , p_key)) % p_key
        #Verificacao 2:
        with open(arq_assinado, 'r') as arquivo_assinado:
            texto = ''
            linha_texto = arquivo_assinado.readline()
            
            while (linha_texto != ''):
                i = 0

                while(i < len(linha_texto)):
                    bloco = ord(linha_texto[i])
                    ConvertToBin = lambda x: format(x, 'b')
                    bloco = ConvertToBin(bloco)
                    texto += str(bloco)
                    i += 1

                linha_texto = arquivo_assinado.readline()
        arquivo_assinado.closed

        ConvertToBin = lambda x: format(x, 'b')
        h_text = sha224(texto).hexdigest()
        h_text = int(h_text, 16)
        h_text = ConvertToBin(h_text)
        
        v2 = potenciamodular(g_key, h_text, p_key)

        if (v1 == v2):
            print("Essa e uma assinatura valida. Assinatura aprovada.")
        else:
            print("Essa assinatura e invalida. Assinatura rejeitada.")

    return menu_principal()

#------------------------------------------------------------------------------------------------------------
#Funcoes para resultados intermediarios e adequacao ao formato desejado.
#Nao consituem funcoes chamadas diretamente por uma escolha do usuario,
#entretanto, aparecem dentro de outras funcoes.(NAO PERTENCEM AS FUNCOES PREVIAS)

def get_pkeyEG():
    '''Recebe pelo terminal (em haxadecimal), ou por um arquivo, a chave privada a ser usada.'''

    print("""Deseja informar a chave privada no formato hexadecimal pelo terminal
    ou ler de um arquivo que a contenha?""")

    print("1) Digitar no terminal")
    print("2) Ler de um arquivo")
    print(" ")

    #Obtendo a resposta do usuario:
    modus = input()

    if (modus == 1):
        print("Insira o valor de 'p'.")
        p_Hkey = raw_input()
        p_key = int(p_Hkey, 16)

        print("Insira o valor de 'g'.")
        g_Hkey = raw_input()
        g_key = int(g_Hkey, 16)

        print("Insira o valor de 'a'.")
        a_Hkey = raw_input()
        a_key = int(a_Hkey, 16)

    else:
        print("Insira o nome do arquivo para a leitura da chave")
        nome_arq_ChavePrivada = raw_input()

        with open(nome_arq_ChavePrivada, 'r') as arq_ChavePrivada:
            p_Hkey = arq_ChavePrivada.readline()
            p_Hkey = p_Hkey[0:-1]
            p_key = int(p_Hkey, 16)

            g_Hkey = arq_ChavePrivada.readline()
            g_Hkey = g_Hkey[0:-1]
            g_key = int(g_Hkey, 16)

            a_Hkey = arq_ChavePrivada.readline()
            a_Hkey = a_Hkey[0:-1]
            a_key = int(a_Hkey, 16)

        arq_ChavePrivada.closed

    return p_key,g_key,a_key

def get_pkeyRSA():
    '''Recebe pelo terminal (em haxadecimal), ou por um arquivo, a chave privada a ser usada.'''

    print("""Deseja informar a chave privada no formato hexadecimal pelo terminal
    ou ler de um arquivo que a contenha?""")

    print("1) Digitar no terminal")
    print("2) Ler de um arquivo")
    print(" ")

    #Obtendo a resposta do usuario:
    modus = input()

    if (modus == 1):
        print("Insira o valor de 'n'.")
        n_Hkey = raw_input()
        n_key = int(n_Hkey, 16)

        print("Insira o valor de 'd'.")
        d_Hkey = raw_input()
        d_key = int(d_Hkey, 16)

    else:
        print("Insira o nome do arquivo para a leitura da chave")
        nome_arq_ChavePrivada = raw_input()

        with open(nome_arq_ChavePrivada, 'r') as arq_ChavePrivada:
            n_Hkey = arq_ChavePrivada.readline()
            n_Hkey = n_Hkey[0:-1]
            n_key = int(n_Hkey, 16)

            d_Hkey = arq_ChavePrivada.readline()
            d_Hkey = d_Hkey[0:-1]
            d_key = int(d_Hkey, 16)

        arq_ChavePrivada.closed

    return n_key,d_key

#Missing
def get_keyRSA():
    '''Recebe, pelo terminal ou por um arquivo, a chave publica que sera usada.'''

    print("""Deseja informar a chave publica no formato hexadecimal pelo terminal
    ou ler de um arquivo que a contenha?""")

    print("1) Digitar no terminal")
    print("2) Ler de um arquivo")
    print(" ")

    #Obtendo a resposta do usuario:
    modus = input()

    if (modus == 1):
        #Adequa para que key receba o valor em hexadecimal
        print("Insira o valor de 'n'.")
        n_Hkey = raw_input()
        n_key = int(n_Hkey, 16)

        print("Insira o valor de 'e'.")
        e_Hkey = raw_input()
        e_key = int(e_Hkey, 16)

    else:
        print("Insira o nome do arquivo para leitura da chave.")
        nome_arq_ChavePublica = raw_input()

        with open(nome_arq_ChavePublica, 'r') as arq_ChavePublica:
            n_Hkey = arq_ChavePublica.readline()
            n_Hkey = n_Hkey[0:-1]
            n_key = int(n_Hkey, 16)


            e_Hkey = arq_ChavePublica.readline()
            e_Hkey = e_Hkey[0:-1]
            e_key = int(e_Hkey, 16)

        arq_ChavePublica.closed

    return n_key,e_key

def get_keyEG():
    '''Recebe, pelo terminal ou por um arquivo, a chave publica que sera usada.'''

    print("""Deseja informar a chave publica no formato hexadecimal pelo terminal
    ou ler de um arquivo que a contenha?""")

    print("1) Digitar no terminal")
    print("2) Ler de um arquivo")
    print(" ")

    #Obtendo a resposta do usuario:
    modus = input()

    if (modus == 1):
        #Adequa para que key receba o valor em hexadecimal
        print("Insira o valor de 'p'.")
        p_Hkey = raw_input()
        p_key = int(p_Hkey, 16)

        print("Insira o valor de 'g'.")
        g_Hkey = raw_input()
        g_key = int(g_Hkey, 16)

        print("Insira o valor de 'c'.")
        c_Hkey = raw_input()
        c_key = int(c_Hkey, 16)

    else:
        print("Insira o nome do arquivo para leitura da chave.")
        nome_arq_ChavePublica = raw_input()

        with open(nome_arq_ChavePublica, 'r') as arq_ChavePublica:
            p_Hkey = arq_ChavePublica.readline()
            p_Hkey = p_Hkey[0:-1]
            p_key = int(p_Hkey, 16)

            g_Hkey = arq_ChavePublica.readline()
            g_Hkey = g_Hkey[0:-1]
            g_key = int(g_Hkey, 16)

            c_Hkey = arq_ChavePublica.readline()
            c_Hkey = c_Hkey[0:-1]
            c_key = int(c_Hkey, 16)

        arq_ChavePublica.closed

    return p_key,g_key,c_key

#Missing
def converte_para_hexadecimal(x):   
    '''Recebe um valor inteiro "x" e converte para a base 16 (hexadecimal).'''

    n = (x % 16)
    aux = ""
    if (n < 10):
        aux = n
    if (n == 10):
        aux = "A"
    if (n == 11):
        aux = "B"
    if (n == 12):
        aux = "C"
    if (n == 13):
        aux = "D"
    if (n == 14):
        aux = "E"
    if (n == 15):
        aux = "F"
    if (x - n != 0):
        return converte_para_hexadecimal(x / 16) + str(aux)
    else:
        return str(aux)


#------------------------------------------------------------------------------------------------------------
#Funcoes previamente utilizadas nos trabalhos semanais:

def miller_rabin(n, b):
    '''.'''

    if(n % 2 == 0 and n != 2):
	    return True
    elif(n == 1 or n == 2 or n == 3):
	    return False
    else:
	    k = 0
	    q = n - 1
	    while(q % 2 == 0):
	    	k += 1
	    	q /= 2
	    t = potenciamodular(b,q,n)
	    if(t == 1 or t == n-1):
	    	return False
	    else:
	    	i = 1
	    	while (i < k):
	    		t = potenciamodular(t,2,n)
	    		if(t == n-1):
	    			return False
	    		else:
	    			i += 1
	    	return True

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

#Missing description
def modulo(n, m):
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

def euclidiano_estendido(a, mod):
    '''Implementa o algoritmo euclidiano estendido para dois valores a e b.'''
    modfixo = mod
    x1,y = 1,1
    x,y1 = 0,0
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

menu_principal()