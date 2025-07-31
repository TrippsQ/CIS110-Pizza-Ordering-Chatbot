print("Welcome to the Pizza Ordering Chatbot! What would you like to order?")
print("I am going to ask you a few questions. After typing an answer press enter")
userName = input("\nEnter your name:")
print(f"\nHello, {userName}. Nice to meet you!")

size = input("What size do you want? Enter small, nediun, or large: ")
FLavor = input("\nEnter the Flavor of the Pizza:   ")
crustType = input("\nwhat type of crust do you want:  ")
quantity = input("\nHow many of these do vou want to order? Please use a interger.")
quantity = int(quantity)
method = input("\nIs this carry out or delivery")

salesTax= 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax

print("-" * 10)
print(f"Thank you, {userName}, for your order")
print(f"Your {quantity} {size} {FLavor} pizzas with {crustType} costs ${total: ,.2f}.")