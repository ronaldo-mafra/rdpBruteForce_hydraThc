from res.TrClass import TrClass

print '''
\033[92m
          .--. .--. .--. 
          |   )|   :|   )
          |--' |   ||--' 
          |  \ |   ;|    
          '   `'--' '    
\033[93m.             \033[1;31m          .-.              
\033[93m|            _|_      \033[1;31m  |                
\033[93m|.-. .--..  . |  .-.  \033[1;31m -|-.-. .--..-..-. 
\033[93m|   )|   |  | | (.-'  \033[1;31m  |(   )|  (  (.-' 
\033[93m'`-' '   `--`-`-'`--' \033[1;31m  ' `-' '   `-'`--'\033[0m
-------------------------------------------------------------------
[+] Desenvolvido por: Ronaldo Mafra
[+] Versao:           0.1
[+] Python:           2.7
-------------------------------------------------------------------'''

help1 = '''[+] Uso do programa:
[!] Carregar uma word-list
[!] Inserir numero de Thread (de 1 a 20)
[!] Inserir ip (para finalizar digite END)
[!] Setar usuario para teste de login
-------------------------------------------------------------------'''

confScript  = {"threads":None,"wordList":None,"ip":None,"userWin":None}
menufuction = {"SET_USER":"setUser", "SET_THREADS":"setTr", "SET_IP":"setIp", "SET_WORD_LIST":"setNameList", "SHOW":"showConf", "RUN":"run"}

def help(opt):
    if opt == 0:
        print help1

def setUser():
    pass

def setTr():
    pass

def setIp():
    pass

def setNameList():
    pass

def showConf():
    pass

def run():
    pass

def menuAndStsShow():
    msg1 = ""
    msg2 = "[+] Escolha uma opcao:\n        "
    for key,val in confScript.items():
        if val == None:
            msg1 += "[!] %s, vazia - " % (key)
        else:
            msg1 += "[+] %s, OK (%s)" % (key, val)

    for key in menufuction.keys():
        msg2 += "   " + key

    print msg1
    print msg2


def main():
    help(0)
    while True:
        menuAndStsShow()
        inp = raw_input("[>] Selecione a Opcao: ").lower()
        a = getattr(None,menufuction[inp])("")


if __name__ == '__main__':
    main()


#ex = TrClass("thrNun","nameList","ipRange","userWin")
#ex.run()


