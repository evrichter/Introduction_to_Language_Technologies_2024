#!/bin/bash

# Print the last 5 lines of the file news.txt
tail -n 5 news.txt | sed 's/$/$/'

