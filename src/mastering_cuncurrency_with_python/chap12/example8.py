import threading
import time

class Spouse(threading.Thread):
    def __init__(self, name: str, partner):
        threading.Thread.__init__(self)
        self.name = name
        self.partner = partner
        self.hungry = True

    def run(self):
        while self.hungry:
            print(f"{self.name} is hungry and wants to eat")

            if self.partner.hungry:
                print(f"{self.name} is waiting for {self.partner.name} to eat first")
            else:
                with fork:
                    print(f"{self.name} is eating")
                    time.sleep(2)
                    print(f"{self.name} has eaten and is now full")
                    self.hungry = False

partner1 = Spouse("wife", None)
partner2 = Spouse("husband", partner1)
partner1.partner = partner2

fork = threading.Lock()

partner1.start()
partner2.start()

partner1.join()
partner2.join()

print("Done")

