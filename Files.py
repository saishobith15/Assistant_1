def file():
    import os
    name = input("which drive should I look into: ")
    if name.capitalize() == "D":
        path = input("Which file should I open: ")
        os.startfile(fr'{name}:\{path}')
    elif name.capitalize() == 'C':
        path = input("Which file should I open: ")
        os.startfile(fr'{name}:\{path}')
file()
