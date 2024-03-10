class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.prices = []
        self.quantities = []
        self.discount = discount
        self.last_transaction_amount = 0
        self.total = 0

    def add_item(self, item, price, quantity=1):
        self.items.append(item)
        self.prices.append(price)
        self.quantities.append(quantity)
        self.total += price * quantity 

    def calculate_total(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i] * self.quantities[i]
        return total

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.calculate_total()
            self.total -= discount_amount  # Update the total with the discount applied
            return int(self.total)
        else:
            return self.total

    def void_last_transaction(self):
        if self.items and self.prices and self.quantities:
            self.last_transaction_amount = self.prices.pop() * self.quantities.pop()
            self.items.pop()
            self.total -= self.last_transaction_amount
        else:
            print("No transaction to void.")


            
# Test
register = CashRegister(discount=10)  
register.add_item("Apple", 1.50, 2)
register.add_item("Banana", 0.75)
print("Total before discount:", register.calculate_total())  # Output: 4.75
print("Total after discount:", register.apply_discount())     # Output: 4.275 (10% discount applied)
register.void_last_transaction()
print("Total after voiding last transaction:", register.calculate_total())  # Output: 1.50 (Only apples left)
