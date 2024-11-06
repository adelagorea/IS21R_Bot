class BankAccount:
    def __init__(self, balance=0):
        """
        Inițializează un obiect BankAccount cu soldul dat.

        :param balance: Soldul inițial al contului
        """
        self.__balance = balance

    def deposit(self, amount):
        """
        Depune o sumă în cont.

        :param amount: Suma de depus
        """
        if amount > 0:
            self.__balance += amount
            print(f"Depus: {amount}. Sold actual: {self.__balance}")
        else:
            print("Suma de depus trebuie să fie pozitivă.")

    def withdraw(self, amount):
        """
        Retrage o sumă din cont.

        :param amount: Suma de retras
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Retras: {amount}. Sold actual: {self.__balance}")
        else:
            print("Fonduri insuficiente sau sumă invalidă.")

    def get_balance(self):
        """
        Returnează soldul actual al contului.

        :return: Soldul contului
        """
        return self.__balance

# Testează clasa
account = BankAccount(100)
account.deposit(50)    # Output: Depus: 50. 
