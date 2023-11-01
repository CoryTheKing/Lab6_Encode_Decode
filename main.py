def encode(password):
    result = []
    for char in password:
        if char.isdigit():
            new_digit = (int(char) + 3) % 10
            result.append(str(new_digit))
        else:
            raise ValueError("input string contains non-digit characters!")
    return ''.join(result)

def decode(password):
    result = []
    for char in password:
        if char.isdigit():
            new_digit = (int(char) - 3) % 10
            result.append(str(new_digit))
        else:
            raise ValueError("input string contains non-digit characters!")
    return ''.join(result)

def main():
    while True:
        print("Menu \n-------------")
        print("1. Encode \n2. Decode \n3. Quit")
        user_input = input("Please enter an option: ")

        if user_input == "1":
            global password
            password = input("Please enter your password to encode: ")
            global output
            output = encode(password)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            print(f"The encoded password is {output}, and the original password is {decode(output)}")
        elif user_input == "3":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
