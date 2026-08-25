import random
import string

def make_serial(count):

    all_char = string.ascii_letters + string.digits

    char_count = len(all_char)

    serial_list = []

    while count > 0:

        random_number = random.randint(0, char_count - 1)

        random_char = all_char[random_number]

        serial_list.append(random_char)

        count -= 1
        
    print("".join(serial_list))

make_serial(10)