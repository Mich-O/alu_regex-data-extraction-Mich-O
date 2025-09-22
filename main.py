#!/usr/bin env python3

#regex python module
import re

#Function for extracting phone numbers
def extractPhoneNo(infoset):
    regex = r"\d" 
    numbers = re.findall(regex, infoset)
    return numbers

print("Numbers extracted: " (extractPhoneNo("07899878676 my name is Claude and my no is 786")))
