def input_error(func): # Обробка помилок
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Give me name and phone please."
            elif func.__name__ == "change_contact":
                return "Give me name and changes please."
        except IndexError:
            return "Give me name please."

    return inner

def parse_input(user_input): # Введення команд юзера
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): # Додавання контакту
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): # Зміна данних контакту
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts): # Показ номеру телефона за именем
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def main():   
    contacts = {}
    print("Welcome to the assistant bot!") # Вітання
    while True:
        user_input = input("Enter a command: ") # Введення команд
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: # Закриття программи
            print("Good bye!")
            break
        
        elif command in ["hello", "hi"]: # Початок роботи
            print("How can I help you?")
        
        elif command == "add": # Додати контакт
            print(add_contact(args, contacts))
        
        elif command == "change": # Змінити контакт
            print(change_contact(args, contacts))

        elif command == "phone": # Знайти за ім'ям 
            print(show_phone(args, contacts))

        elif command == "all": # Всі контакти 
            print(contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()