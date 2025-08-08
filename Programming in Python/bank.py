from abc import ABC, abstractmethod

# Abstract base class
class Bank(ABC):
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self, amount):
        pass


# Subclass Swiss implementing Bank
class Swiss(Bank):
    def __init__(self):
        self.bal = 1000  # Correctly assign instance variable

    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal = self.bal - amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining balance: {self.bal}")
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal


# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())  # Should work now
    s.withdraw(30)        # Should work
    s.withdraw(1000)      # Should print "Insufficient funds"

if __name__ == "__main__":
    main()
