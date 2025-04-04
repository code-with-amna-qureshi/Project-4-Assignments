

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
   
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    print(f"Temperature: {fahrenheit:.1f}F = {celsius:.6f}C")
    
    
    print("🙏 Thank you for using this program! Created by Amna Qureshi! 🌟")

# This provided line is required to call the main() function.
if __name__ == '__main__':
    main()
