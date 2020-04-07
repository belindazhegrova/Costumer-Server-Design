import socket
from datetime import *
import random
from _thread import *

print('-------------------------------------KY ESHTE PROGRAMI FIEK-TCP SERVER-------------------------------------------------')
print('-----------------------------------------------------------------------------------------------------------------------')


def IpAddress():
    return "Ip adresa juaj eshte %s" % address[0]



def porti():
    return "Klienti eshte duke perdorur portin %s" % address[1]



def count(request):
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    ccount = 0
    vcount=0
    message = str(request).upper()
    for i in range (0, len(message)):
        if(message[i] in consonants):
            ccount += 1
        else:
            vcount +=1
    return  "Teksti i pranuar permban  " + str(vcount) + " zanore dhe  " + str(ccount) + " bashketingllore"



def reverse(request):
  #return request[::-1]
  return ''.join(reversed(request))

   

def is_palindrome(request):
   if(request == request[::-1]):
       return "Teksti i dhene eshte palindrome"
   else:
       return "Teksi i dhene nuk eshte palindrome"
                                      

def time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def game():
    listaNumrave = []
    for i in range(5):
        listaNumrave.append(random.randint(1,35))
    listaNumrave.sort()
    return str(listaNumrave) + " 5 numra te rastesishem nga 35"


def gcf(num1,num2):
    num1=int(num1)
    num2=int(num2)
    while(num2):
        num1, num2=num2, num1 % num2

    return "Faktori me i madh i perbashket i dy numrave eshte: " + str(num1)



def convert(type,nr):
    nr = float(nr)
    if(type == "CmToFeet"):
        return  '{:.2f}'.format(nr /30.48) 
    elif (type == "FeetToCm"):
            return  '{:.2f}'.format(nr * 30.48)
    elif (type == "KmToMile"):
            return  '{:.2f}'.format(nr / 1.609344)
    elif (type == "MileToKm"):
            return  '{:.2f}'.format(nr * 1.609344)
    else:
       return "Ky Konvertim nuk gjendet ketu"



def check(n):
    n = float(n)
    if n>0:
        return "Positive number"
    elif n==0:
        return "Zero"
    else:
        return "Negative number"



def grade(mark1,mark2,mark3,mark4,mark5):
    mark1=float(mark1)
    mark2=float(mark2)
    mark3=float(mark3)
    mark4=float(mark4)
    mark5=float(mark5)

    total= mark1 + mark2 + mark3 + mark4 + mark5
    perc=(total /500)*100

    return "total marks = %.2f " %total + " mark percetange = %.2f" % perc




def kerkesat(data, clientS):
    try:
        request = data.split()
        response = ""
        if request[0] == "IPADDRESS":
            response = IpAddress()
        elif request[0] == "PORT":
            response = porti()
        elif request[0] == "COUNT":
            response = count(request[1])
        elif request[0] == "TIME":
            response = time()
        elif request[0] == "REVERSE":
            response = reverse(request[1])
        elif request[0] == "GAME":
            response = game()
        elif request[0] == "PALINDROME":
            response = is_palindrome(request[1])
        elif request[0] == "GCF":
            response = gcf(request[1],request[2])
        elif request[0] == "CONVERT":
            response = str(convert(request[1],request[2]))
        elif request[0] == "CHECK":
            response = str(check(request[1]))
        elif request[0] == "GRADE":
            response = str(grade(request[1],request[2],request[3],request[4],request[5]))
        
        else:
            response = "Kerkese invalide"
        clientS.sendall(str.encode(response))
        
    except:
        response = "Ka ndodhur nje gabim, ju lutem provoni perseri "
        clientS.sendall(str.encode(response))

    
def client_thread(clientS):
    while True:

        data = clientS.recv(128).decode()
       
        kerkesat(data, clientS)
    clientS.close()

serverName = 'localhost'
serverPort = 13000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.bind((serverName, serverPort))
s.listen(5)
print("Serveri eshte duke pritur per ndonje kerkese ")



while True:
    clientS, address = s.accept()
    print("Klienti i lidhur ne portin  " +   str(address[1]) )
    start_new_thread(client_thread, (clientS,))


s.close()
