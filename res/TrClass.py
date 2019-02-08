from threading import Thread

class TrClass(Thread):
    colors = {
        'INFO': '\033[94m',
        'OK': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[1;31m',
        'END_C': '\033[0m'
    }

    def __init__(self, thrNun, nameList, ipRange, userWin):
        Thread.__init__(self)
        self.thrNun     = thrNun
        self.nameList   = nameList
        self.ipRange    = ipRange
        self.userWin    = userWin

    def run(self):
        print "thrNun: " + self.thrNun
        print "nameList: " + self.nameList
        print "ipRange: " + self.ipRange
        print "userWin: " + self.userWin

        self.meExec()

    def meExec(self):
        print "EXEC"

