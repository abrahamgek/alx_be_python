# weather_advice.py

# Prompt the user for weather input
What_is_the_weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations based on user input
if What_is_the_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif What_is_the_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif What_is_the_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")