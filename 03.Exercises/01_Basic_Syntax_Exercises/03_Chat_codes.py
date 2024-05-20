chat_lines = int(input())

for i in range(chat_lines):
    code_number = int(input())

    if code_number == 88:
        print("Hello")
    elif code_number == 86:
        print("How are you?")
    elif code_number != 86 and code_number < 88:
        print("GREAT!")
    else:
        print("Bye.")
