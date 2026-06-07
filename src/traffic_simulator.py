import random

# Generate traffic at intersection
north = random.randint(5, 50)
south = random.randint(5, 50)
east = random.randint(5, 50)
west = random.randint(5, 50)

print("Current Traffic")
print("----------------")
print("North:", north)
print("South:", south)
print("East :", east)
print("West :", west)

# Action 0
waiting_ns = east + west

# Action 1
waiting_ew = north + south

print("\nIf North-South gets Green:")
print("Waiting Time =", waiting_ns)

print("\nIf East-West gets Green:")
print("Waiting Time =", waiting_ew)

if waiting_ns < waiting_ew:
    print("\nBest Action: Green for North-South")
else:
    print("\nBest Action: Green for East-West")