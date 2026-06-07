import random

north = random.randint(10, 60)
south = random.randint(10, 60)
east = random.randint(10, 60)
west = random.randint(10, 60)

print("\n===== SMART TRAFFIC CONTROL =====\n")

print("North:", north)
print("South:", south)
print("East :", east)
print("West :", west)

traffic = {
    "North": north,
    "South": south,
    "East": east,
    "West": west
}

best_direction = max(traffic, key=traffic.get)

print("\nGreen Signal:", best_direction)

print("Vehicles Cleared:", traffic[best_direction])