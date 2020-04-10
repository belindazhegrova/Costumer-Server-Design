import socket
from datetime import *
import random
from _thread import *

print('-------------------------------------KY ESHTE PROGRAMI FIEK-TCP SERVER-------------------------------------------------')
print('-----------------------------------------------------------------------------------------------------------------------')

def IPADDRESS():
    return "Ip adresa juaj eshte %s" % address[0]




def PORT():
    return "Klienti eshte duke perdorur portin %s" % address[1]




def COUNT(request):
    vowels = ['A','E','I','O','U']
    vcount = 0
    ccount=0
    text = ''.join([str(word) for word in request])
    for i in range (0, len(text)):
        if(text[i] in vowels):
            vcount += 1
        else:
            ccount +=1
    return  "Teksti i pranuar permban  " + str(vcount) + " zanore dhe  " + str(ccount) + " bashketingllore"
    




def REVERSE(word):
  text = ''.join([str(item) for item in word])
  reverseTEXT= text[::-1]
  return reverseTEXT



   
def PALINDROME(request):
   if(request == request[::-1]):
       return "Teksti i dhene eshte palindrome"
   else:
       return "Teksi i dhene nuk eshte palindrome"
                                      



def TIME():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")




def GAME():
    listaNumrave = []
    for i in range(5):
        listaNumrave.append(random.randint(1,35))
    listaNumrave.sort()
    return str(listaNumrave) + " 5 numra te rastesishem nga 35"




def GCF(num1,num2):
    num1=int(num1)
    num2=int(num2)
    while(num2):
        num1, num2=num2, num1 % num2

    return "Faktori me i madh i perbashket i dy numrave eshte: " + str(num1)





def CONVERT(type,nr):
    nr = float(nr)
    if(type == "CmToFeet"):
        return  '{:.2f}'.format(nr /30.48)+'ft'
    elif (type == "FeetToCm"):
            return  '{:.2f}'.format(nr * 30.48)+'cm'
    elif (type == "KmToMile"):
            return  '{:.2f}'.format(nr / 1.609344)+'mile'
    elif (type == "MileToKm"):
            return  '{:.2f}'.format(nr * 1.609344)+'km'
    else:
       return "Keni bere gabim gjate shenimit"




def CHECK(n):
    n = float(n)
    if n>0:
        return "Numri eshte pozitiv"
    elif n==0:
        return "Zero"
    else:
        return "Numri eshte negativ"




def FIND(mark1,mark2,mark3,mark4,mark5):
    mark1=float(mark1)
    mark2=float(mark2)
    mark3=float(mark3)
    mark4=float(mark4)
    mark5=float(mark5)

    total= mark1 + mark2 + mark3 + mark4 + mark5
    perc=(total /500)*100

    return "totali i notav eshte  %.2f " %total + " dhe  nota mesatare eshte  %.2f" % perc





def kerkesat(data, clientS):
    try:
        request = data.split()
        response = ""
        if request[0] == "IPADDRESS":
            response = IPADDRESS()
        elif request[0] == "PORT":
            response = PORT()
        elif request[0] == "COUNT":
            response = COUNT(request[1:])
        elif request[0] == "TIME":
            response = TIME()
        elif request[0] == "REVERSE":
            response = REVERSE(request[1:])
        elif request[0] == "GAME":
            response = GAME()
        elif request[0] == "PALINDROME":
            response = PALINDROME(request[1])
        elif request[0] == "GCF":
            response = GCF(request[1],request[2])
        elif request[0] == "CONVERT":
            response = str(CONVERT(request[1],request[2]))
        elif request[0] == "CHECK":
            response = str(CHECK(request[1]))
        elif request[0] == "FIND":
            response = str(FIND(request[1],request[2],request[3],request[4],request[5]))
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
print('Serveri eshte startuar ne localhost ne portin: ' + str(serverPort))
s.listen(5)
print("Serveri eshte duke pritur per ndonje kerkese ")


while True:
    clientS, address = s.accept()
    print("Klienti i lidhur ne portin  " +   str(address[1]))
    start_new_thread(client_thread, (clientS,))

s.close()


