def convert_integer_part(value, base):
    symbols = "0123456789ABCDEF"
    if value == 0:
        return "0"
    output = ""
    negative = value < 0
    value = abs(value)
    while value > 0:
        remainder = value % base
        output = symbols[remainder] + output
        value //= base
    return '-' + output if negative else output

def convert_fractional_part(value, base, max_places=8):
    symbols = "0123456789ABCDEF"
    result = ""
    count = 0
    while value > 0 and count < max_places:
        value *= base
        digit = int(value)
        result += symbols[digit]
        value -= digit
        count += 1
    return result or "0"

def base_converter(input_str, bases):
    try:
        if '.' in input_str:
            number = float(input_str)
            int_part = int(number)
            frac_part = abs(number - int_part)

            print(f"Input (decimal): {number}")

            for b in bases:
                int_result = convert_integer_part(int_part, b)
                frac_result = convert_fractional_part(frac_part, b)
                print(f"Base {b}: {int_result}.{frac_result}")

        else:
            number = int(input_str)
            print(f"Input (decimal): {number}")

            for b in bases:
                int_result = convert_integer_part(number, b)
                print(f"Base {b}: {int_result}")

    except ValueError:
        print("Error: Invalid decimal input.")


if __name__ == "__main__":
    num_input = input("Enter a decimal integer or float: ").strip()
    
    if not num_input:
        print("Error: No input provided for number.")
        exit()

    base_input = input("Enter bases to convert to (e.g., 2,8,16 or custom like 3,5,12): ").strip()
    
    if not base_input:
        print("Error: No input provided for bases.")
        exit()

    base_list = [int(x.strip()) for x in base_input.split(',') if x.strip().isdigit() and 2 <= int(x.strip()) <= 16]

    base_converter(num_input, base_list)