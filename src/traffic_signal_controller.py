import time

def control_signal(north, south, east, west):

    ns_density = north + south
    ew_density = east + west

    print("\n===== AI SMART SIGNAL CONTROL =====\n")

    print(f"North : {north}")
    print(f"South : {south}")
    print(f"East  : {east}")
    print(f"West  : {west}")

    # Decide which direction gets green
    if ns_density > ew_density:

        direction = "North-South"

        if ns_density < 20:
            green_time = 15

        elif ns_density < 50:
            green_time = 30

        else:
            green_time = 45

        print("\n🚦 SIGNAL STATUS")
        print("North-South : GREEN")
        print("East-West   : RED")

    else:

        direction = "East-West"

        if ew_density < 20:
            green_time = 15

        elif ew_density < 50:
            green_time = 30

        else:
            green_time = 45

        print("\n🚦 SIGNAL STATUS")
        print("North-South : RED")
        print("East-West   : GREEN")

    print(f"\nDecision : {direction}")
    print(f"Green Time : {green_time} seconds")

    # Countdown timer
    for i in range(green_time, 0, -1):

        print(
            f"🚦 Remaining Time: {i} sec",
            end="\r"
        )

        time.sleep(1)

    print("\n\n⚠️ YELLOW SIGNAL")

    for i in range(5, 0, -1):

        print(
            f"🟡 Yellow Time: {i} sec",
            end="\r"
        )

        time.sleep(1)

    print("\n\n🔄 Switching Signal...\n")


if __name__ == "__main__":

    # Sample values
    control_signal(
        north=52,
        south=47,
        east=18,
        west=15
    )