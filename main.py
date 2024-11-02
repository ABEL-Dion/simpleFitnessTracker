class User:
    def __init__(self, user_id, name, age, weight, height):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.workouts = []
        self.meals = []

    def log_workout(self, workout):
        if workout in self.workouts:
            print(f"This {workout.workout_id} workout already exists.\n")
        else:
            self.workouts.append(workout)
            return f"Workout {workout.workout_id} logged successfully."

    def log_meal(self, meal):
        if meal in self.meals:
            print(f"This {meal.food_item} meal already exists.\n")
        else:
            self.meals.append(meal)  # Correct this line to append to self.meals
            return f"Meal {meal.meal_id} logged successfully."

    def total_calories(self):
        total_burned = sum(workout.calculate_calories_burned() for workout in self.workouts)
        total_consumed = sum(meal.calories for meal in self.meals)
        return total_burned, total_consumed


class Workout:
    def __init__(self, workout_id, duration):
        self.workout_id = workout_id
        self.duration = duration
        self.calories_burned = self.calculate_calories_burned()  # Calculate immediately upon creation

    def calculate_calories_burned(self):
        calories_per_min = 4
        return self.duration * calories_per_min


class Meal:
    def __init__(self, meal_id, food_item, calories):
        self.meal_id = meal_id
        self.food_item = food_item
        self.calories = calories


class FitnessTracker:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            print(f"{user.name} already exists.")

    def get_user_summary(self):
        summaries = []
        for user in self.users:
            total_calories_burned = sum(workout.calories_burned for workout in user.workouts)
            total_calories_consumed = sum(meal.calories for meal in user.meals)
            summaries.append({
                "user_id": user.user_id,
                "name": user.name,
                "calories_burned": total_calories_burned,
                "calories_consumed": total_calories_consumed,
            })
        return summaries


def main():
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add User")
        print("2. Log Workout")
        print("3. Log Meal")
        print("4. Get User Summary")
        print("5. Exit")

        choice = input("Select an option: ").lower()

        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            weight = input("Enter weight: ")
            height = input("Enter height: ")
            user = User(user_id, name, age, weight, height)
            tracker.add_user(user)
            print(f"User {name} added successfully.")

        elif choice == '2':
            user_id = input("Enter user ID to log workout for: ")
            user = next((u for u in tracker.users if u.user_id == user_id), None)
            if user:
                workout_id = input("Enter workout ID: ")
                duration = int(input("Enter workout duration (in minutes): "))
                workout = Workout(workout_id, duration)  # calories_burned will be calculated
                user.log_workout(workout)
                print(f"Logged workout for {user.name}.")
            else:
                print("User not found.")

        elif choice == '3':
            user_id = input("Enter user ID to log meal for: ")
            user = next((u for u in tracker.users if u.user_id == user_id), None)
            if user:
                meal_id = input("Enter meal ID: ")
                food_item = input("Enter food item: ")
                calories = int(input("Enter calories for this meal: "))
                meal = Meal(meal_id, food_item, calories)
                user.log_meal(meal)
                print(f"Logged meal for {user.name}.")
            else:
                print("User not found.")

        elif choice == '4':
            user_id = input("Enter user ID to get summary for: ")
            user = next((u for u in tracker.users if u.user_id == user_id), None)
            if user:
                burned, consumed = user.total_calories()
                print(f"User Summary for {user.name}:")
                print(f"Total Calories Burned: {burned}")
                print(f"Total Calories Consumed: {consumed}")
            else:
                print("User not found.")

        elif choice == '5' or "exit":
            print("Exiting the Fitness Tracker.")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
