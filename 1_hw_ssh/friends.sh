#!/bin/bash

# Get the first character of my username
first_char=$(whoami | cut -c1)

# List all users whose username starts with the same character
ls /afs/ms/u/"$first_char"/
