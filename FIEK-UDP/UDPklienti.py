import socket

print('-------------------------------------KY ESHTE PROGRAMI FIEK-UDP --------------------------------------------------')
print('------------------------------------------------------------------------------------------------------------------')


serverName= 'localhost' 
serverPort= 13000
var = input('Emri i serverit eshte ' + serverName + '  dhe porti eshte ' + str(serverPort) + ' , A doni ti ndryshoni  PO/JO  ')
if var.upper() == 'PO':
    serverName=input('Shkruani emrin e serverit: ')
    serverPort=input('Shkruani numrin e portit: ')

address = (serverName, serverPort)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        try:
           request = input("Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT,CHECK,FIND)? ")
           if request == "exit":
                break
           s.sendto(str.encode(request), address)
           response = s.recvfrom(128)
           response = response[0].decode()
           print('Pergjigja: ', repr(response))
        except:
            print("Ka ndodhur nje gabim, ju lutem provoni perseri")
