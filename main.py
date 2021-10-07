# https://prnt.sc/sdchkm
import time
from threading import Thread
from new.Conf import Conf
from new.ThreadTesseract import tT
from new.linkManager import lM
from new.log import *

config = Conf.config

threads = config.get("threads")
max_digits = config.get("code_digit_num")
url_prefix = config.get("url_form")
thread_arr = []
instance_arr = []
auto = 0  # para n bloquear açao de threads
status = 0
init_link = config.get("init_link")


lm = lM(init_link=init_link)

# TODO://
#  + Testar se todos os modulos funcionam
#  + Guardar dados temporariamente num json de array [ [url, keywords], [u,k],... ] porque os prints não funcionam sem auto
#  ou usar o webwook do discord para mandar os pares [url, keywords] como tambem o resto dos loggings de teste dos modulos.
#  + Adicionar opção de aumentar/diminuir o no. de threads a meio da execução
#  + Guardar dados numa DB [PERMANENTE]


def startThreads():
    global status

    print("lm Main Hash: " + str(hex(id(lm))))

    for i in range(0, threads):
        print("Aqui 2")
        tt = tT()
        t = Thread(target=tt.startIfShould, args=(lm,), name="Thread#" + str(i))
        t.start()
        thread_arr.append(t)
        instance_arr.append(tt)
    status = 1


def stopThreads():
    global status
    for ti in instance_arr:
        ti.askToStop()

    for t in thread_arr:
        t.join()

    status = 0


def askThreadsStatus():
    for t in instance_arr:
        print("Running: " + str(t._running))
        print("ActualUrl: " + str(t.actual_url))


def defineNewUrlToContinue(url):
    lm.overWriteBase(url)


def main():

    global auto
    while True:
        time.sleep(1)
        if auto is 0:

            cmd = input("CMD> ")
            if len(cmd) == 0:
                cmd = "     "
            if cmd[0] == "/":

                if cmd[1:len(cmd)] == "start":

                    if status == 0:
                        print("Iniciando Threads")
                        startThreads()
                    elif status == 1:
                        print("Threads ja iniciadas")

                elif cmd[1:len(cmd)] == "stop":

                    if status == 1:
                        print("Parando Threads")
                        stopThreads()

                    elif status == 0:
                        print("Threads ja estao paradas")


                elif cmd[1:len(cmd)] == "set":

                    arg = cmd.split(" ")[1]
                    if arg is not None:

                        if len(arg) > max_digits or len(arg) < max_digits:
                            print("Tamanho de codigo errado")
                        else:
                            defineNewUrlToContinue(str(url_prefix)+str(arg))


                            #addNewUrlToLast("https://prtn.sc/" + args)
                    else:
                        print("Digite um codigo valido")

                elif cmd[1:len(cmd)] == "status":

                    if status == 1:
                        askThreadsStatus()
                        print("Threads ativas.")
                    else:
                        print("Threads inativas.")


                elif cmd[1:len(cmd)] == "auto":
                    auto = 1
                    print("Ativando modo automatico")
                else:
                    print("Comando desconhecido.")
            else:
                print("Nenhum comando utilizado")
        else:
            time.sleep(1)
        


main()


