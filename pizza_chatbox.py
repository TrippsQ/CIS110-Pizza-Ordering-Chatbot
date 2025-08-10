print("Welcome to the Pizza Ordering Chatbot! What would you like to order?")
print("I am going to ask you a few questions. After typing an answer press enter")
userName = input("\nEnter your name:  ")
if userName.lower() == "lord isszac":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else: 
    print(f"\nHello, {userName}. Nice to meet you.")

size = input("What size do you want? Enter small, nediun, or large: ")
FLavor = input("\nEnter the Flavor of the Pizza:   ")
crustType = input("\nwhat type of crust do you want:  ")
quantity = input("\nHow many of these do vou want to order? Please use a interger.")
quantity = int(quantity)
method = input("\nIs this carry out or delivery")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

salesTax= 1.1

if size.lower() == "small":
    pizzaCost = 8.99 
elif size.lower() == "medium":
    pizzaCost = 14.99 
elif size.lower() == "large":
    pizzaCost = 17.99

total = (pizzaCost * quantity) * salesTax + deliveryFee

print("-" * 10)
print(f"Thank you, {userName}, for your order")
print(f"Your {quantity} {size} {FLavor} pizzas with {crustType} costs ${total: ,.2f}.")
if total >= 50: 
    print("\nCongrats, You earned 10$ off your next order")
else:
    print("Orders over 50$ receive 10$ off.")


print("-" * 10)


