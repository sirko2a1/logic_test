while True:
    user_input = input("Введіть команду: ")
    
    if user_input == "привіт":
        print("Привіт, Я тут.")
    elif user_input == "як справи?":
        print("Добре, дякую")
    elif user_input == "що робиш?":
        print("Розмовляю з вами.")
    elif user_input == "вийти":
        print("Арівідерчі.")
        break
    else:
        print("Не розумію вашої команди.")
