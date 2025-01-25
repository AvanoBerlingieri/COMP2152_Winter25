# Author: Avano Berlingieri
# Assignment 1

gym_member = "Alex Alliton" # Data type: String
preferred_weight_kg = 20.5 # Data type: Double
highest_reps = 25 # Data type: Int
membership_active = True # Data type: Boolean

# Data types: String & tuple
workout_stats = {
    "Nima": (0, 10, 90),
    "Lhek": (15, 100, 60),
    "Avano": (30, 60, 120),
    "Nima_Total":(),
    "Lhek_Total":(),
    "Avano_Total":(),
}

for i in workout_stats.keys():
    workout_stats[f"{workout_stats.keys()} + _Total"] = (workout_stats[f"{workout_stats.keys()}"][0] + workout_stats[f"{workout_stats.keys()}"][1] + workout_stats[f"{workout_stats.keys()}"][2])

workout_List = ([],
                [],
                [])


if workout_stats[f"{workout_stats.keys()}_Total"] >= 120:
    print(f"Great job staying active {workout_stats.keys()}!")

def find_friend():
    for member in workout_stats.keys():
        print(f"Member: {member} " + "yoga: " + workout_stats[member][0] + "running: " + workout_stats[member][1] + "Weightlifting: " + workout_stats[member][2] + "Total: " + workout_stats[member][3])