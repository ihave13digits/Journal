#!/usr/bin/python3

# Log by digits version 1.6-2019-7

import os, getpass
from datetime import datetime

from text import *

root_folder = os.path.dirname(__file__)
try:
    os.mkdir(os.path.join(root_folder, 'data'))
    data_folder = os.path.join(root_folder, 'data')
    os.makedirs(os.path.join(data_folder, 'user'))
    os.makedirs(os.path.join(data_folder, 'data'))
except FileExistsError:
    data_folder = os.path.join(root_folder, 'data')

user_file = os.path.join(data_folder, 'user')
data_file = os.path.join(data_folder, 'data')

PIN = int()
DATA = {'user' : "",
        'pass' : "",
        'date' : "",
        'enum' : 0,
        'color' : [255, 255, 255]
        }
new_user = False

class Data:

    def save(user):
        global new_user
        if new_user == True:
            with open(os.path.join(data_file, user), 'w') as f:
                f.write(Data.crypt(str(DATA['user']), L=PIN))
                f.write("\n")
                f.write(Data.crypt(str(DATA['pass']), L=PIN))
                f.write("\n")
                f.write(Data.crypt(str(DATA['date']), L=PIN))
                f.write("\n")
                f.write(str(DATA['enum']))
                f.write("\n")
                f.write(str(DATA['color'][0]))
                f.write("\n")
                f.write(str(DATA['color'][1]))
                f.write("\n")
                f.write(str(DATA['color'][2]))
                f.write("\n")
            new_user = False
        else:
            with open(os.path.join(data_file, user), 'w') as f:
                f.write(Data.crypt(str(DATA['user']), L=PIN))
                f.write("\n")
                f.write(Data.crypt(str(DATA['pass']), L=PIN))
                f.write("\n")
                f.write(Data.crypt(str(DATA['date']), L=PIN))
                f.write("\n")
                f.write(str(DATA['enum']))
                f.write("\n")
                f.write(str(DATA['color'][0]))
                f.write("\n")
                f.write(str(DATA['color'][1]))
                f.write("\n")
                f.write(str(DATA['color'][2]))
                f.write("\n")

    def load(user):
        with open(os.path.join(data_file, user), 'r') as f:
            DATA['user'] = Data.crypt(str(f.readline().strip()), L=PIN, mode='d')
            DATA['pass'] = Data.crypt(str(f.readline().strip()), L=PIN, mode='d')
            DATA['date'] = Data.crypt(str(f.readline().strip()), L=PIN, mode='d')
            DATA['enum'] = int(f.readline().strip())
            DATA['color'][0] = int(f.readline().strip())
            DATA['color'][1] = int(f.readline().strip())
            DATA['color'][2] = int(f.readline().strip())

    def crypt(txt, L=47, mode='e'):
        chars = "a0Z1b2Y3c4X5d6W7e8V9f`U~g,T.h?S!i@R#j$Q%k^P&l*O-m=N_n+M(o)L{p}K[q]J<r>I;s:H/t'G\"u|F vEwDxCyBzA"
        cypher = ""
        for c in txt:
            if c in chars:
                if mode == "e":
                    character = (chars.find(c) + L) % 94
                if mode == "d":
                    character = (chars.find(c) - L) % 94
                cypher += chars[character]
            else:
                cypher += c
        return cypher

class User:

    def menu():
        os.system('clear')
        print("(1) New")
        print("(2) Log")
        print("(0) Exit")
        sel = input(": ")
        if sel == "1":
            User.new()
        if sel == "2":
            Engine.run()
        if sel == "0":
            exit()

    def new():
        global PIN, new_user
        new_user = True
        os.system('clear')
        print("You will need to input a username(any length or common characters),")
        print("password(any length or common characters),")
        print("and key number(any length of digits).")
        print("")
        print("Remember: your username and password will be encrypted and stored, but your")
        print("key will not be stored and cannot be recovered.  Your key is your real password.")
        print("")
        print("Press 'enter' to continue.")
        sel = input()
        os.system('clear')
        print("Enter your name")
        username = input(": ")
        DATA['user'] = username
        print("Enter your password")
        DATA['pass'] = getpass.getpass(": ")
        print("Enter key number")
        PIN = int(getpass.getpass(": "))
        
        try:
            Data.load(username)
            if username == DATA['user']:
                print("User already exists")
            else:
                pass
        except FileNotFoundError:
            try:
                Data.save(DATA['user'])
                os.makedirs(os.path.join(user_file, DATA['user']))
                Engine.run()
            except FileExistsError:
                print("User already exists")

    def login():
        global PIN
        os.system('clear')
        print("Enter your name")
        username = input(": ")
        print("Enter your password")
        password = getpass.getpass(": ")
        print("Enter key number")
        PIN = int(getpass.getpass(": "))
        try:
            Data.load(username)
            if username == DATA['user'] and password == DATA['pass']:
                return True
            else:
                User.menu()
                return False
        except FileNotFoundError:
            User.menu()

    def reset():
        global PIN
        print("(1) Username")
        print("(2) Password")
        print("(3) Key")
        select = input(": ")
        if select == "1":
            print("Are you sure you want to reset your username? Y/N")
            sel = input().lower()
            if sel == "y":
                users_file = os.path.join(data_folder, 'data')
                specs_file = os.path.join(users_file, DATA['user'])
                user_files = os.path.join(data_folder, 'user')
                spec_files = os.path.join(user_files, DATA['user'])
                root = os.getcwd()
                os.chdir(root)

                print("Enter new username")
                new_username = input(": ")
                os.renames(spec_files, os.path.join(user_files, new_username))
                os.renames(specs_file, os.path.join(users_file, new_username))
                DATA['user'] = new_username
                os.chdir(root)
                Data.save(DATA['user'])
            else:
                pass
        if select == "2":
            print("Are you sure you want to reset your password? Y/N")
            sel = input().lower()
            if sel == "y":
                print("Enter new password")
                new_password = getpass.getpass(": ")
                DATA['pass'] = new_password
            else:
                pass
        if select == "3":
            print("Are you sure you want to reset your key? Y/N")
            sel = input().lower()
            if sel == "y":
                print("Enter new key number")
                newPIN = int(getpass.getpass(": "))
                spec_file = os.path.join(user_file, DATA['user'])
                last_file = str(str(DATA['enum'])+".txt")
                try:
                    old_data = ""
                    for x in range(1, DATA['enum']+1):
                        x_file = str(str(x) + ".txt")
                        with open(os.path.join(spec_file, x_file), 'r') as f:
                            old_data = Data.crypt(f.read(), L=PIN, mode='d')
                        with open(os.path.join(spec_file, x_file), 'w') as f:
                            f.write(Data.crypt(old_data, L=newPIN))
                        x += 1
                    PIN = newPIN
                except FileNotFoundError:
                    pass
            if sel == "n":
                pass

class Journal:

    def entry():
        spec_file = os.path.join(user_file, DATA['user'])
        os.system('clear')
        print(DATA['user'])
        DATA['enum'] += 1
        next_file = str(str(DATA['enum'])+".txt")
        print("Write data to be stored")
        data = input(": ")
        in_data = Data.crypt(data, L=PIN)
        current_time = Data.crypt(str(DATA['date']), L=PIN)
        with open(os.path.join(spec_file, next_file), 'w') as f:
            f.write(current_time)
            f.write("\n")
            f.write(in_data)
            f.write('\n')

    def read():
        spec_file = os.path.join(user_file, DATA['user'])
        os.system('clear')
        last_file = str(str(DATA['enum'])+".txt")
        try:
            for x in range(1, DATA['enum']+1):
                print(x)
                x_file = str(str(x) + ".txt")
                with open(os.path.join(spec_file, x_file), 'r') as f:
                    for line in f:
                        l = Data.crypt(line, L=PIN, mode='d')
                        Text.stream(l, DATA['color'][0], DATA['color'][1], DATA['color'][2])
                    x += 1
                    sel = input()
        except FileNotFoundError:
            data = None
            print("No entries found")
            sel = input(": ")

    def erase():
        user_file = os.path.join(data_folder, 'user')
        spec_file = os.path.join(user_file, DATA['user'])
        os.system('clear')
        root = os.getcwd()
        spec_file = os.path.join(user_file, DATA['user'])
        os.chdir(spec_file)
        for x in range(DATA['enum']):
            print(x)
            x += 1
            users_file = str(str(x) + ".txt")
            os.remove(users_file)
        os.chdir(root)
        DATA['enum'] = 0
        Data.save(DATA['user'])

class Engine:

    def settings():
        print("(1) Color")
        sel = input(": ")
        if sel == "color" or sel == "1":
            mode = "color"
        
        if mode == "speed":
            pass
        if mode == "color":
            print("Current color values: {} {} {}".format(DATA['color'][0], DATA['color'][1], DATA['color'][2]))
            print("Enter a number(0-255)")
            r_val = int(input("R: "))
            g_val = int(input("G: "))
            b_val = int(input("B: "))
            DATA['color'][0] = r_val
            DATA['color'][1] = g_val
            DATA['color'][2] = b_val

    def menu():
        os.system('clear')
        Data.save(DATA['user'])
        Data.load(DATA['user'])
        print("{}".format(DATA['user']))
        print("")
        print("(1) Read")
        print("(2) Write")
        print("(3) Erase")
        print("(4) Reset")
        print("(5) Options")
        print("(0) Exit")
        print("")
        choice = input(": ")
        os.system('clear')
        if choice == "read" or choice == "1":
            Journal.read()
        if choice == "write" or choice == "2":
            Journal.entry()
        if choice == "erase" or choice == "3":
            print("Are you sure you want to erase all journal entries? Y/N")
            select = input(": ").lower()
            if select == "y":
                Journal.erase()
            else:
                pass
        if choice == "reset" or choice == "4":
            User.reset()
        if choice == "options" or choice == "5":
            Engine.settings()
        if choice == "exit" or choice == "0":
            exit()

    def run():
        running = User.login()
        while running:
            DATA['date'] = str(datetime.today())
            Engine.menu()

User.menu()
