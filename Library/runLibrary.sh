#!/bin/bash
file="Library"
 gcc -std=c11 -Wall -Wextra -pedantic -c -fPIC $file.c -o $file.o
 gcc -shared $file.o -o $file.dll

 python LibraryCharger.py
 read -p "Press any key to continue..."