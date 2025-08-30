def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height (in meters or cm): "))

        # Handle height input (if user enters cm instead of meters)
        if height > 3:  # assume cm
            height = height / 100

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\n Your BMI is {bmi:.2f}")
        print(f" Category: {category}")

    except ValueError as e:
        print("Error:", e)

    # Ask user if they want another calculation
    again = input("\nDo you want to calculate again? (y/n): ").lower()
    if again != "y":
        print("Goodbye! Stay healthy 💪")
        break
