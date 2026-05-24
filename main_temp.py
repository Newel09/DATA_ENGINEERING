from API_Project_2.get_city_temperature import get_city_temperature

def main():
    city_name = input("Enter the city name: ").strip()

    try:
        # Call the combined function
        temperature = get_city_temperature(city_name)
        print(f"Current temperature in {city_name}: {temperature}")

    except KeyError:
        print(f"City '{city_name}' not found in API results.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()