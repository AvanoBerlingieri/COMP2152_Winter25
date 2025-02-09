# Author: Avano Berlingieri
# Assignment 1

gym_member = "Alex Alliton" # Data type: String
preferred_weight_kg = 20.5 # Data type: Float
highest_reps = 25 # Data type: Int
membership_active = True # Data type: Boolean

# Data type: dict
workout_stats = {
    "Nima": (0, 10, 90),
    "Lhek": (10, 60, 35),
    "Avano": (30, 45, 75),
}

totals = {}
for name, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    totals[f"{name}_total"] = total_minutes

workout_stats.update(totals)
print("Workout stats from dictionary:")
print(workout_stats)

# Data type: List
workout_list = [[workout_stats["Nima"][0], workout_stats["Nima"][1], workout_stats["Nima"][2]],
                [workout_stats["Lhek"][0], workout_stats["Lhek"][1], workout_stats["Lhek"][2]],
                [workout_stats["Avano"][0], workout_stats["Avano"][1], workout_stats["Avano"][2]]]

print("Workout stats from nested lists:")
print(workout_list)

yoga_running = [row[:2] for row in workout_list]
print("Time for yoga & running:")
print(yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Time weightlifting for Last Two Friends:")
print(weightlifting_last_two)

for name in workout_stats:
    if "_total" in name and workout_stats[name] >= 120:
        friend_name = name.replace("_total","")
        print(f"Great job staying active {friend_name}!")

friend = input("Enter a friend's name to check workout stats: ")

if friend in workout_stats:
    workout_data = workout_stats[friend]
    print(f"{friend}'s Workout Stats - Yoga: {workout_data[0]}, Running: {workout_data[1]},"
          f" Weightlifting: {workout_data[2]}, Total: {workout_stats[f'{friend}_total']}")
else:
    print(f"{friend} was not found in the records.")

highest_friend = max(totals, key = totals.get)
lowest_friend = min(totals, key = totals.get)

print(f"{highest_friend.replace('_total', '')} spent the most time time working out: {totals[highest_friend]} minutes")
print(f"{lowest_friend.replace('_total', '')} spent the least time working out: {totals[lowest_friend]} minutes")