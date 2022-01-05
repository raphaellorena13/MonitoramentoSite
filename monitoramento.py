import time, os 
from datetime import datetime

def checar_conexao(hostname):
    response = os.system('ping -c 1 -w2 ' + hostname + ">/dev/null 2>&1")
    return response     


if __name__ == '__main__':
    teste = False
    executa = True
    while executa :
        now = datetime.now()
        agora = now.strftime("%m/%d/%Y, %H:%M:%S")
        if checar_conexao('uol.com.br') == 0:
            if (teste == False):
                print('up   ' + agora )
                teste = True
                time.sleep(60)
        else:
            if (teste):
                print('down ' + agora )
                teste = False
                #reset_vpn_globo()
                time.sleep(60)
