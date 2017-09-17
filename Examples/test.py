from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.MAGENTA + 'Hello')
print(Back.GREEN + 'World')
print(Style.DIM + 'James Bond')
print(Style.RESET_ALL)
print('back to normal now')