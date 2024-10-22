def main():
    while True:
        welcome = input("Internet or Files or Exit: ")
        if welcome.capitalize() == "Internet":
            import web
        elif welcome.capitalize() == "Files":
            import Files
        elif welcome == 'exit':
            print("Good bye!!")
            break
        else:
            print("Invalid input. Please enter 'Internet' or 'Files'.")

main()
