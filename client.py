import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
guest = 0
host = 0
IP = '0.tcp.in.ngrok.io'
PORT = 18872
s.connect((IP,PORT))
temp_file = []
print("[+] connection established")
for x in range(0,3):
    msg = s.recv(1000) 
    ask_input = input("Enter a for rock b for paper c for scissors :")
    temp_file.append((f"{ask_input}",f"{msg.decode('utf-8')}"))
    s.send(bytes(ask_input,'utf-8'))
to_win = [('b','a'),('c','b'),('a','c')]
to_draw = [('a','a'),('b','b'),('c','c')]
to_lose = [('a','b'),('b','c'),('c','a')]
for item in temp_file:
	if item in to_win:
		guest += 1
		print(f"you chose :{item[0]},he chose :{item[1]} ")
	elif item in to_draw:
		print(f"you chose :{item[0]},he chose :{item[1]} ")
	elif item in to_lose:
		guest -= 1
		print(f"you chose :{item[0]},he chose :{item[1]} ")
	else:
		print("[-] something went wrong here")
if guest>host:
	print(" you  won")
elif host>guest:
	print(" Host won")
else:
	print('Draw ')
