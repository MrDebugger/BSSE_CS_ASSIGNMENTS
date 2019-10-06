#Task 1
class Clicker:
    def __init__(self):
        self.counter = 0
    def push(self):
        self.counter+=1
    def reset(self):
        self.counter=1
    def notFound(self):
        print("[-] Button not Found")
    def __str__(self):
        return f'{self.counter}'

clicker = Clicker()
while True:    
    print("[+] Current Value of Counter is:",clicker)
    print("[?] Press the following Buttons to perform given Functions")
    print("[*] (P)ush > Increment the Clicker counter.")
    print("[*] (R)eset > Reset the Clicker counter.")
    print("[*] (E)xit > Exit from Program")
    option = input("[>] Button: ").lower()
    {
    'p' : clicker.push,
    'r' : clicker.reset,
    'e' : exit
    }.get(option, clicker.notFound)()
    print()
