import socket

print('------------------------------------------KY ESHTE PROGRAMI FIEK-TCP CLIENT--------------------------------------------')
print('-----------------------------------------------------------------------------------------------------------------------')



serverName= 'localhost' 
serverPort= 13000
var = input('Emri i serverit eshte:  ' + serverName + '  dhe porti eshte  ' + str(serverPort) + ' , A doni ti ndryshoni  PO/JO  ')
if var.upper() == 'PO':
    serverName=input('Shkruani emrin e serverit: ')
    serverPort=input('Shkruani numrin e portit: ')



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverName, serverPort))
    while True:
        try:
            request = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT,CHECK,FIND)? ")
            s.sendall(str.encode(request))
            response = s.recv(128).decode()
            print('Pergjigja: ', repr(response))
        except:
            print("Ka ndodhur nje gabim, ju lutem provoni perseri")





        

  





  
    


