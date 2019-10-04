# this is an octothorpe -- it makes a comment (line ignored by the computer)
# print("hello world!")
# testing out print
print("hello there!")
print("Howdy, y'all!")
print("I like typing this.")
print("This is fun.")

# math skills demo

# counting the chickens
print("I will not count my chickens", 2.0)
# adding hens
print("Hens: ", 25.0 + 30.0 / 6.0)
# adding roosters
print("Roosters: ", 100.0 - 25.0 * 3.0 % 4.0)
# counting the eggs
print("Now I will count the eggs", 7.0)
# adding the eggs
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)
# true or false math problem
print(3.0 + 2.0 < 5.0 - 7.0)
# counting the pigs
print("Now I will count the pigs")
# adding the pigs
print(3.0 + 6.0 + 4.0 % 11.0 - 2.0)

# variables and some of their powers
cars = 80
SpaceInACar = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = SpaceInACar + cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available,")
print("There are only",  drivers, "drivers available today,")
print("There will be", cars_not_driven, "empty cars today")
print("We have", passengers, "to carpool today,")
print("approximately",average_passengers_per_car, "in each car,")

# variables with food
burgers = 150
Customers = 125
BurgersPerCustomer = 1
BurgersBought = BurgersPerCustomer * Customers
BurgersNotBought = burgers - BurgersBought

print("There are", burgers, "burgers for sale")
print("There are", Customers, "customers today")
print("We sold", BurgersBought, "burgers today")
print("We didn't sell", BurgersNotBought, "burgers today")

# More variables and playing with output
myName = "Izzie"
myAge = 307
myHeight = 61 # inches
MyEyes = "Brown"
myHair = "Brown"
print("Let's talk about %s, "% myName)
print("She's %d inches tall."% myHeight)
print("she's got %s eyes and %s hair,"% MyEyes, myHair)
print("when I add %d and %d, I get %d,"% myAge, myHeight)

my_String = 'hello'
print(my_String)

count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

