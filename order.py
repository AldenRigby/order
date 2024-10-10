courses = {"raw potato": 50, "instant ramen": 200, "chicken tender": 1, "nothing": 0}
drinks = {"water": 0, "coffee": 200000, "soda": 1, "orange juice": 5, "nothing": 0}
appetizers = {"french fries": 5, "american fries": 500000000, "popsicle": 1, "nothing": 0}
sides = {"salad": -5, "croutons": 1, "cooked potato": 5000, "nothing": 0}
desserts = {"ice cream": 10, "popsicle": 5, "blue cheese": 300, "nothing": 0}
class Order:
    def __init__(self, drink="nothing", appetizer="nothing", course="nothing", sides=["nothing", "nothing"], dessert="nothing"):
        self.drink = drink
        self.appetizer = appetizer
        self.course = course
        self.sides = sides
        self.dessert = dessert
    def __str__(self):
        return f"""Course: {self.course}. ${str(courses[self.course])}
Drink: {self.drink}. ${str(drinks[self.drink])}
Appetizer: {self.appetizer}. ${str(appetizers[self.appetizer])}
Sides: {self.sides[0]} and {self.sides[1]}. ${str(sides[self.sides[0]] + sides[self.sides[1]])}
Dessert: {self.dessert}. ${str(desserts[self.dessert])}
Total: ${str(courses[self.course] + drinks[self.drink] + appetizers[self.appetizer] + sides[self.sides[0]] + sides[self.sides[1]] + desserts[self.dessert])}
"""
    def setCourse(self):
        self.course = Order.askUser("What would you like for your main course?\n" + str(list(courses.keys())), list(courses.keys()))
    
    def setDrink(self):
        self.drink = Order.askUser("What would you like for your drink?\n" + str(list(drinks.keys())), list(drinks.keys()))
    
    def setAppetizer(self):
        self.course = Order.askUser("What would you like for your appetizer?\n" + str(list(appetizers.keys())), list(appetizers.keys()))
    
    def setSides(self):
        self.sides = [0, 0]
        self.sides[0] = Order.askUser("What would you like for your first side?\n" + str(list(sides.keys())), list(sides.keys()))
        self.sides[1] = Order.askUser("What would you like for your second side?\n" + str(list(sides.keys())), list(sides.keys()))
    
    def setDessert(self):
        self.dessert = Order.askUser("What would you like for your dessert?\n" + str(list(desserts.keys())), list(desserts.keys()))
    
    @classmethod
    def askUser(self, ask, valid):
        userInput = input(ask + "\nInput: ")
        print("")
        while userInput not in valid:
            userInput = input("That isn't on the menu buddy. Pick something else. " + ask)
        return userInput

order = Order()

while True:
    userInput = input("""Hello. How may we help you today?
(M) Order main course
(D) Order a drink
(A) Order appetizer
(S) Order sides
(DS) Order dessert
(V) View order
(P) Place order
Input: """).upper()
    print("")
    if userInput in ["M","D","A","S","DS","V","P"]:
        if userInput == "M":
            order.setCourse()
        elif userInput == "D":
            order.setDrink()
        elif userInput == "A":
            order.setAppetizer()
        elif userInput == "S":
            order.setSides()
        elif userInput == "DS":
            order.setDessert()
        elif userInput == "V":
            print(str(order))
        elif userInput == "P":
            if order.course != "nothing" or order.appetizer != "nothing" or order.drink != "nothing" or "nothing" not in order.sides or order.dessert != "nothing":
                print("Thank you for coming. Have a good day.")
                quit()
            else:
                print("You need to order something first bro.")