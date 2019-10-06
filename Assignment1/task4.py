#Task 4
from datetime import datetime
class DateTime:
    def __init__(self):
        self.presentTime = datetime.now()
    def displayTime(self):
        return '[+] Current Time: '+self.presentTime.time().strftime("%I:%H %p")
    def displayDate(self):
        return '[+] Current Date: '+self.presentTime.date().strftime("%d / %m / %Y")
    def notFound(self):
        return '[-] Invalid Choice'
    def displayFormat(self):
        print("[?] Formats can be found here: http://strftime.org/")
        form = input("[>] Enter Format: ")
        try:
            return '[+] Your Formated Date Time: '+self.presentTime.strftime(form)
        except:
            return '[-] Invalid Format'
    def __str__(self):
        return f'{self.presentTime.strftime("%d/%m/%Y %I:%H %p")}'
while True:
    print("[?] Please Follow below Instructions.")
    print("[*] Enter (T)ime to display Time")
    print("[*] Enter (D)ate to display Date")
    print("[*] Enter (F)ormat to display Date Time in specific Format")
    print("[*] Enter (E)xit to Quit")
    option = input("[>] Enter Choice: ").lower()
    date = DateTime()
    print(
    {
    't' : date.displayTime,
    'd' : date.displayDate,
    'f' : date.displayFormat,
    'e' : exit
    }.get(option,date.notFound)()
    )
    print()
