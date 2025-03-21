def decimal_to_binary(n):
    result = ""
    for i in range(7, -1, -1):
        bit = (n >> i) & 1
        result += str(bit)
    return result

def decimal_to_hexadecimal(n):
    symbols = "0123456789ABCDEF"
    high = n // 16
    low = n % 16
    return symbols[high] + symbols[low]

def main():
    user_input = input("Enter a decimal number (0-255): ").strip()

    if not user_input.isdigit():
        print("Error: Please enter a valid integer.")
        return

    number = int(user_input)

    if not (0 <= number <= 255):
        print("Error: Number must be between 0 and 255.")
        return

    binary_output = decimal_to_binary(number)
    hex_output = decimal_to_hexadecimal(number)

    print(f"Decimal: {number}")
    print(f"Binary: {binary_output}")
    print(f"Hexadecimal: {hex_output}")

if __name__ == "__main__":
    main()