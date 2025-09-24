#!/usr/bin/env python3

#regex python module
import re
import os

#Path to the input file. It holds our sample data. 
input_path = "input.txt"

#Function for extracting phone numbers
def extractPhoneNo(infoset):
    regex = r"\(?\d{3}\)?\s?-?\.?\d{3}-?\.?\d{4}" #Regex pattern for matching phone numbers
    numbers = re.findall(regex, infoset)  #re.findall returns all non-overlapping matches of pattern in string, as a list of strings.
    return numbers

#Function for extracting times(24-hour and 12-hour formats)
def extractTimes(infoset):
    regex = r"\b((1[0-2]|0?[1-9]):[0-5][0-9]\s?[AaPp][Mm]|(2[0-3]|[01]?[0-9]):[0-5][0-9](?!\s?[AaPp][Mm]))\b" #Regex pattern for matching times
    times = re.findall(regex, infoset)
    formatted_times = [time[0] if time[0] else time[4] for time in times] #Extract the full match from the tuple
    return formatted_times

#Function for extracting hashtags
def extractHashtags(infoset):
    regex = r"#\w+" #Regex pattern for matching hashtags
    hashtags = re.findall(regex, infoset)
    return hashtags

#Function for extracting HTML tags
def extractHTMLTags(infoset):
    regex = r"<[^>]+>" #Regex pattern for matching HTML tags
    tags = re.findall(regex, infoset)
    return tags

#Function for extracting credits cards numbers
def extractCreditCardNo(infoset):
    regex = r"\d{4}\s?-?\d{4}\s?-?\d{4}\s?-?\d{4}"
    cardNumbers = re.findall(regex, infoset)
    return cardNumbers

#Function for extracting URLs
def extractURLs(infoset):
    regex = r"https?:\/\/[^\s]+"
    urls = re.findall(regex, infoset)
    return urls

#Function for formatting list output. It returns the array output as a numbered list.
def format_list(items):
    return "\n".join([f"  {i+1}. {item}" for i, item in enumerate(items)])

#Check if input.txt file exists in the current directory. If not, print an error message and exit.
if not os.path.exists(input_path):
    print("Error: input.txt file is missing.")
    exit(1)

#Check if input.txt file is empty. If it is, print an error message and exit.
if os.path.getsize(input_path) == 0:
    print("Error: input.txt file is empty.")
    exit(1)

#Main function to read the input file and call the extraction functions
with open(input_path, "r") as file:
    infoset = file.read()

    phone_numbers = extractPhoneNo(infoset)
    html_tags = extractHTMLTags(infoset)
    credit_cards = extractCreditCardNo(infoset)
    URLs = extractURLs(infoset)
    Hashtags = extractHashtags(infoset)
    Times = extractTimes(infoset)

#Output the results. The length of each array is printed first, followed by the formatted list of items.
    print(f"({len(phone_numbers)}) Phone Numbers extracted from file:\n{format_list(phone_numbers)}\n")
    print(f"({len(html_tags)}) HTML tags extracted from file:\n{format_list(html_tags)}\n")
    print(f"({len(credit_cards)}) Credit card numbers extracted from file:\n{format_list(credit_cards)}\n")
    print(f"({len(URLs)}) URLs extracted from file:\n{format_list(URLs)}\n")
    print(f"({len(Hashtags)}) Hashtags extracted from file:\n{format_list(Hashtags)}\n")
    print(f"({len(Times)}) Times extracted from file:\n{format_list(Times)}\n") 

# Save output to output.txt using file_out.write()
with open("output.txt", "w") as file_out:
    file_out.write(f"({len(phone_numbers)}) Phone Numbers extracted from file:\n{format_list(phone_numbers)}\n\n")
    file_out.write(f"({len(html_tags)}) HTML tags extracted from file:\n{format_list(html_tags)}\n\n")
    file_out.write(f"({len(credit_cards)}) Credit card numbers extracted from file:\n{format_list(credit_cards)}\n\n")
    file_out.write(f"({len(URLs)}) URLs extracted from file:\n{format_list(URLs)}\n\n")
    file_out.write(f"({len(Hashtags)}) Hashtags extracted from file:\n{format_list(Hashtags)}\n\n")
    file_out.write(f"({len(Times)}) Times extracted from file:\n{format_list(Times)}\n")

print("Extracted data saved to output.txt!")