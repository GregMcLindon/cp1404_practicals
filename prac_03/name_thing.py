"""Greg McLindon"""
def main():
    """Program to print every second letter of a string"""


def get_name():
    global string_name
    name_valid = False
    while not name_valid:
        string_name = input("What is your name?")
        if len(string_name) == 0:
            print("Enter a valid name")
        else:
            name_valid = True
    return string_name

def print_name_thing(string_text,int_step):
    print(string_text[::int_step])

string_name = get_name()
int_step = int(input("How many characters to print?"))
print_name_thing(string_name,int_step)

main()
