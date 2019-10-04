#!/usr/bin/python3

# TextStreaming by digits version 0.6 2018.12

from os import system
from sys import stdout, platform
from time import sleep

clear_cmd = ''

if platform.startswith('win32'):
    clear_cmd = 'cls'
else:
    clear_cmd = 'clear'

class Text:

    def clear():
        system(clear_cmd)

    def sstream(txt, spd=0.06, clr=''):
        if clr == 'b':
            system(clear_cmd)
        for c in txt:
            stdout.write(c)
            stdout.flush()
            sleep(spd)
        print("")

    def cstream(txt, spd=0.06, dly=0, hdr='', hdr_m=1, end='', end_x=1, clr=''):
        if dly == 0:
            if clr == 'b':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)
            if hdr != '':
                print(hdr + '\n' * hdr_m)
            for c in txt:
                stdout.write(c)
                stdout.flush()
                sleep(spd)
            if clr == 'a':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)
            print(end * end_x, end='')

        if dly > 0:
            delay = spd * dly
            if clr == 'b':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)
            if hdr != '':
                print(hdr + '\n' * hdr_m)
            for c in txt:
                stdout.write(c)
                stdout.flush()
                sleep(spd)
            print(end * end_x, end='')
            sleep(delay)
            if clr == 'a':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)

    def fstream(text_file, spd=0.06, dly=0, hdr='', hdr_m=1, end='', end_x=1, clr=''):
        with open(text_file, 'r') as txt:
            if dly == 0:
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for char in txt:
                    for c in char:
                        stdout.write(c)
                        stdout.flush()
                        sleep(spd)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                print(end * end_x, end='')

            if dly > 0:
                delay = spd * dly
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for char in txt:
                    for c in char:
                        stdout.write(c)
                        stdout.flush()
                        sleep(spd)
                print(end * end_x, end='')
                sleep(delay)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)

    def stream(text_file, r, g, b, spd=0.06, dly=0, hdr='', hdr_m=1, end='\n', end_x=1, clr=''):
        if '.txt' in text_file:
            FBG = 38#48
            with open(text_file, 'r') as txt:
                if dly == 0:
                    if clr == 'b':
                        system(clear_cmd)
                    if clr == 'b+a':
                        system(clear_cmd)
                    if hdr != '':
                        print(hdr + '\n' * hdr_m)
                    for char in txt:
                        for c in char:
                            stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                            stdout.flush()
                            sleep(spd)
                    if clr == 'a':
                        system(clear_cmd)
                    if clr == 'b+a':
                        system(clear_cmd)
                    print(end * end_x, end='')

                if dly > 0:
                    delay = spd * dly
                    if clr == 'b':
                        system(clear_cmd)
                    if clr == 'b+a':
                        system(clear_cmd)
                    if hdr != '':
                        print(hdr + '\n' * hdr_m)
                    for char in txt:
                        for c in char:
                            stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                            stdout.flush()
                            sleep(spd)
                    print(end * end_x, end='')
                    sleep(delay)
                    if clr == 'a':
                        system(clear_cmd)
                    if clr == 'b+a':
                        system(clear_cmd)
        else:
            FBG=38#48
            if dly == 0:
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for c in text_file:
                    stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                    stdout.flush()
                    sleep(spd)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                print(end * end_x, end='')

            if dly > 0:
                delay = spd * dly
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for c in text_file:
                    stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                    stdout.flush()
                    sleep(spd)
                print(end * end_x, end='')
                sleep(delay)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
