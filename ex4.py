# number cars
cars = 100
# space in a car
space_in_a_car = 4.0
#drivers
drivers = 30
#passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avalilable"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# extra credit

x = 10
y = 20
z = 10 + 20
print "x = 10, y = 20"
print "x + y = ", z