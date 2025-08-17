print("Welcome to the Pizza Ordering Chatbot! What would you like to order?")
print("I am going to ask you a few questions. After typing an answer press enter")
userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
if userName.lower() == "lord isszac":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else: 
    print(f"\nHello, {userName}. Nice to meet you.")

size = input("What size do you want? Enter small, medium, or large: ")
while size.lower() not in ["small", "meduim", "large"]:
    size = input("Invalid! Enter correct Size")
FLavor = input("\nEnter the Flavor of the Pizza:   ")
while len(FLavor) == 0:
    FLavor = input("Invalid! Enter correct Flavor")
crustType = input("\nwhat type of crust do you want:  ")
while len(crustType) == 0:
    crustType = input("Invalid! Enter correct crust type")
quantity = input("\nHow many of these do vou want to order? Please use a interger.")
while not quantity.isdigit():
    quantity = input("Value not recongized. Please enter a numeric Value:  ")
quantity = int(quantity)
def canon_method(s: str) -> str:
    # lowercase, strip, collapse spaces, remove dashes/underscores
    s = " ".join(s.lower().split()).replace("-", "").replace("_", "")
    # accept common variants
    if s in ("carryout", "carry out", "pickup", "pick up", "takeout", "take out"):
        return "carry out"
    if s in ("delivery",):
        return "delivery"
    return ""  # not recognized

method = canon_method(input("Is this carry out or delivery? "))
while method == "":
    method = canon_method(input("Invalid. Please type 'carry out' or 'delivery': "))

deliveryFee = 5 if method == "delivery" else 0

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


