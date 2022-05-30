from database_interface import *
from statistical_calculations import *
from key_logging import *

def study():
    print("studying...")
    # get name
    name = input("Enter your name >> ")
    # measure times
    print("Enter your secret phrase >> ")
    times = enter_phrase()
    # calculate values
    times = remove_brute_errors(times)
    M = expected_value(times)
    D = variance(times, M)
    # update database
    if check_user(name):
        old_M, old_D = get_user(name)
        M = (old_M + M) / 2
        D = (old_D + D) / 2
    set_user(name, M, D)
    print("Successfully study")

def login():
    print("logining...")
    # get name
    name = input("Enter your name >> ")
    # check name
    if not check_user(name):
        print("No such user")
        return
    # measure times
    print("Enter your secret phrase >> ")
    times = enter_phrase()
    # calculate values
    times = remove_brute_errors(times)
    etalon_M, etalon_D = get_user(name)
    # check values
    if not Fisher_coefficient(etalon_D, times) or not equal_center(etalon_M, etalon_D, times):
        print("Incorrect handwriting")
        return
    print("Successfully login")

if __name__ == "__main__":
    while True:
        mode = input("Enter study, login or exit >> ")
        if mode == "exit":
            break
        elif mode == "study":
            study()
        elif mode == "login":
            login()
        else:
            print("Invalid input. Try again.")
    print("Thank you for using.")