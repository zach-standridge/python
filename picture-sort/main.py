#!/usr/bin/env python3
import datetime
import os

print("What directory do you want sorted?", end=' ')
directory = input()

print(directory)

for file in os.listdir(directory):
    if file.lower.endswith(('.jpeg', '.mp4', '.jpg')):
        print(file)
        print(os.path.getctime(file))
