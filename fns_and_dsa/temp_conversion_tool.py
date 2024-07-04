# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    while True:
        try:
            temperature_str = input("Enter temperature (e.g., 32F or 0C): ").strip().upper()
            
            if temperature_str.endswith('F'):
                temperature = float(temperature_str[:-1])
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}F is {converted_temp:.2f}C")
                break
            elif temperature_str.endswith('C'):
                temperature = float(temperature_str[:-1])
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}C is {converted_temp:.2f}F")
                break
            else:
                raise ValueError("Invalid temperature format. Please enter a numeric value followed by 'F' or 'C'.")
        
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")

# Entry point of the script
if __name__ == "__main__"
main()
