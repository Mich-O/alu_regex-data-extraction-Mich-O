#!/usr/bin env python3

#regex python module
import re

#Function for extracting phone numbers
def extractPhoneNo(infoset):
    regex = r"\(?\d{3}\)?\s?-?\.?\d{3}-?\.?\d{4}" 
    numbers = re.findall(regex, infoset)
    if len(numbers) == 0:
        return "No phone numbers found"
    return numbers


#Function for extracting HTML tags
def extractHTMLTags(infoset):
    regex = r"<[^>]+>" 
    tags = re.findall(regex, infoset)
    if len(tags) == 0:
        return "No HTML tags found"
    return tags


#Function for extracting credits cards numbers
def extractCreditCardNo(infoset):
    regex = r"\d{4}\s?-?\d{4}\s?-?\d{4}\s?-?\d{4}"
    cardNumbers = re.findall(regex, infoset)
    if len(cardNumbers) == 0:
        return "No credit card numbers found"
    return cardNumbers

#Function for extracting URLs
def extractURLs(infoset):
    regex = r"https?:\/\/[^\s]+"
    urls = re.findall(regex, infoset)
    if len(urls) == 0:
        return "No URLs found"
    return urls

with open("input.txt", "r") as file:
    infoset = file.read()

    print(f"Phone Numbers extracted from file: {extractPhoneNo(infoset)}\n")
    print(f"HTML tags extracted from file: {extractHTMLTags(infoset)}\n")
    print(f"Credit card numbers extracted from file: {extractCreditCardNo(infoset)}\n")
    print(f"URLs extracted from file: {extractURLs(infoset)}")