import webbrowser
import os
def web():
    while True:
        url_input = input("What should I search on the internet or should I open a particular website or search a file or Exit : \n ")
        if url_input == 'website' or url_input == 'a particular website':
            new_url = input("which website should I search: ")
            webbrowser.open_new_tab(f"https://www.{new_url}.com")
        elif url_input == 'internet' or url_input == 'search the internet':
            url = input("What should I search the internet: ")
            webbrowser.open_new_tab(f"https://www.google.com/search?client=opera-gx&q={url}&sourceid=opera&ie=UTF-8&oe=UTF-8")
        elif url_input == 'exit':
            print("good bye...")
            break
        elif url_input == 'file' or url_input == 'open files':
            print("Opening...")
            import Files
web()   