import csv
import datetime as dt
import time

def msgerroArquivo():
    print(':(  não consegui encontrar o arquivo ...')
    print(f'Possiveis soluções.')
    print(f'1 Conferir se todas colunas do arquvio estão preenchidas: Nome, Email, Cpf, Celular, idade, Data de nascimento, Data de cadastro')
    print(f'2 Verificar o local e nome do arquivo.')
    print(f'3 O local e nome do arquivo devem ser informados juntos: EX C:carlos\pastaarquivo\meuarquivo.csv')
    print ('Não se esqueça de colocar o \ junto ao nome do arquirvo.')

def carregandoArq():
    carregando ='carregando arquivo .'
    pont = '.'
    print(f'{carregando}',end='')
    time.sleep(0.4)
    print(f'{pont}',end='')
    time.sleep(0.4)
    print(f'{pont}',end='')
    time.sleep(0.6)
    print(f'{pont}')

def conferirNom ():
    if len(nome) == 'nome':
        return True
    if len(nome) <= 25:
        return True
    if len(nome) > 25:
        return False

def conferirEmail ():
    if email == 'email':
        return True
    if len(email)< 4:
        return False
    if email[-4] == '.' and email[-3] == 'c' and email[-2] == 'o' and email[-1] == 'm':
        for i in email:
            if i == '@':
                return True
    else:
        return False

def conferircpf ():
    if cpf == 'cpf':
        return True
    if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        cpf_val = cpf.replace('.','').replace('-','')
        if len(cpf_val) == 11:
            return True
        else:
            return False
    else:
        return False

def conferirCel ():
    if celular == 'celular':
        return True
    if celular[0] =='(' and celular[3] == ')':
        celularV = celular.replace(' ', '').replace('-','')
        if len(celularV) == 13:
            return True
        else:
            return False
    else:
        return False

def conferirDt_nasc():
    if dt_nascimento == 'data_nascimento':
        return True
    if dt_nascimento[2] == '/' and dt_nascimento[5] == '/' and len(dt_nascimento) == 10:
        return True
    else:
        return False

def conferirDt_cad ():
    if dt_cadastro == 'data_cadastro':
        return True
    if dt_cadastro[2] == '/' and dt_cadastro[5] == '/' and len(dt_cadastro) == 10:
        return True
    else:
        return False


def msgerroNome():
    print(f"{20 * '-/'} PROGRAMA INTERROMPIDO{20*'/-'}")
    print(f"FALHA AO LER AS SEGUINTES INFORMAÇÕES: {nome} - {email} - {cpf} - {celular} - {idade} - {dt_nascimento} - {dt_cadastro}:")
    print(f"MOTIVO : NOME MAIOR QUE 25 CARACTERES '{nome}'")
    print(f"quantidade de caracteres encontrados {len(nome)}")
    print(f"favor corrigir a quantidade de caracteres no arquivo.")

def msgerroEmail():
    print(f"{20 * '-/'} PROGRAMA INTERROMPIDO{20 * '/-'}")
    print(f'FALHA AO LER AS SEGUINTES INFORMAÇÕES: {nome} - {email} - {cpf} - {celular} - {idade} - {dt_nascimento} - {dt_cadastro}:')
    print(f'MOTIVO : EMAIL INVALIDO "{email}":')
    print(f'Solução: feche o programa e corrija o email. Ex email valido: levi.cunha@gmail.com')

def msgerroCpf():
    print(f"{20 * '-/'} PROGRAMA INTERROMPIDO{20 * '/-'}")
    print(f'FALHA AO LER AS SEGUINTES INFORMAÇÕES: {nome} - {email} - {cpf} - {celular} - {idade} - {dt_nascimento} - {dt_cadastro}:')
    print(f'MOTIVO : CPF INCORRETO "{cpf}":')
    print(f'Solução: feche o programa e corrija o numero de cpf no arquivo.EX CPF valido: 863.052.791-95')

def msgerrtoCel():
    print(f"{20 * '-/'} PROGRAMA INTERROMPIDO{20 * '/-'}")
    print(f'FALHA AO LER AS SEGUINTES INFORMAÇÕES: {nome}-{email}-{cpf}-{celular}-{idade}-{dt_nascimento}-{dt_cadastro}:')
    print(f'MOTIVO : NUMERO DE CELULAR INCORRETO "{celular}":')
    print(f'Solução: feche o programa e corrija o numero do celular no arquivo.EX celular valido:(31) 9164-05374')

def msgerroNasc():
    print(f"{20 * '-/'} PROGRAMA INTERROMPIDO{20 * '/-'}")
    print(f'FALHA AO LER AS SEGUINTES INFORMAÇÕES: {nome}-{email}-{cpf}-{celular}-{idade}-{dt_nascimento}-{dt_cadastro}:')
    print(f'MOTIVO : DATA DE NASCIMENTO INVALIDA "{dt_nascimento}":')
    print(f'Solução: feche o programa e corrija a data de nascimento. Ex data valida: 10/05/1935')

def msgerroCad():
    print(f"{20 * '-/'} PROGRAMA INTERROMPIDO{20*'/-'}")
    print(f'FALHA AO LER AS SEGUINTES INFORMAÇÕES: {nome}-{email}-{cpf}-{celular}-{idade}-{dt_nascimento}-{dt_cadastro}:')
    print(f'MOTIVO : DATA DE CADASTRO INVALIDA "{dt_cadastro}"')
    print(f'Solução: feche o programa e corrija a data de cadastro. Ex data valida: 10/05/1935')



print (f"{20 * '=='} BEM-VINDO {20 * '=='}")
print(f'leitor de arquivos .csv versão 1.0')
while True:
    try:
        arq = str(input("informe o local e nome do arquivo:")).strip(' ')
        carregandoArq()
        with open(arq, "r") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=',')
            for [nome, email, cpf, celular, idade, dt_nascimento, dt_cadastro] in arquivo_csv:
                if conferirNom() == True and conferirEmail() == True and conferircpf() == True and conferirCel() == True and conferirDt_nasc() == True and conferirDt_cad() == True:
                    print(f'{nome} -- {email} -- {cpf} -- {celular} -- {idade} -- {dt_nascimento} -- {dt_cadastro}')
                    idade = int()
                    dt_nascimento = dt.time()
                    dt_cadastro = dt.time()
                elif conferirNom() == False:
                    msgerroNome()
                    break
                elif conferirEmail() == False:
                    msgerroEmail()
                    break
                elif conferircpf() == False:
                    msgerroCpf()
                    break
                elif conferirCel() == False:
                    msgerrtoCel()
                    break
                elif conferirDt_nasc() == False:
                    msgerroNasc()
                    break
                elif conferirDt_cad() == False:
                    msgerroCad()
                    break
    except:
        msgerroArquivo()

    continuar = input("Deseja abrir outro aquirvo? se sim aperte S, caso queira fechar o programa digite F:").upper().strip()
    if continuar != "F" and continuar != "S":
        continuar = input(f'{continuar} não é uma resposta valida digite S para abrir outro arquivo ou F para finalizar o programa')
    if continuar == "F":
        break
