# -*- coding: utf-8 -*-


from colorama import Fore, init
from os import name, system
from threading import Thread
from src.data import sites
from src.logger import Logger
from src.checker import check_accounts


all_data = ''


if name == 'nt':
    init()

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def main():
    global all_data

    clear()
    start_mess = '''
    |---------------------|
    |       by rady       |
    |                     |
    |    UserDetective    |
    |                     |
    |       by rady       |
    |---------------------|

    '''
    print(Fore.GREEN + start_mess)

    name = input(Fore.YELLOW + '[*] Enter Username: ')


    print('\n[*] Wait...\n')
    for site in sites:
        res = check_accounts(site, name)
        if res == 200:
            result = '[+] ' + sites[site] + ': ' + site + name
            all_data += result + '\n'
            print(Fore.GREEN + result)
        else:
            result = '[-] ' + sites[site]
            all_data += result + '\n'
            print(Fore.RED + result)
    
    log = Logger(all_data)
    print(Fore.WHITE)

    input()


if __name__ == '__main__':
    main()


