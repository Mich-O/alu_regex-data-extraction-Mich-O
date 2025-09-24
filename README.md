# ALU Regex Data Extraction

## Project Overview
This project demonstrates the use of **Regular Expressions (Regex)** in Python to extract structured data from raw text.  

## Repository Structure
- alu_regex-data-extraction-Mich-O : directory
 - main.py : python file with regex functions 
 - input.txt : text file with data for extraction
 - output.txt : contains output from the sample data extracted from input.txt
 - README.md : documentation of project
 - LICENSE
 - .gitignore


## Features
The script can extract: 
- URLs  
- 10 digit Phone numbers  
- HTML tags
- 16 digit credit card numbers
- Hashtags
- Time in both the 12-hour and 24-hour format

After the extraction, the displayed output is saved in the file output.txt

## Example demonstration
Input(text from input.txt):

    Hello, contact us using these numbers: 07123456678 or (123) 456-7890 preferrably between 8.30 am and 17:00 on weekdays.

Output: 

        (2) Phone numbers extracted from file: 
         1. 0712345678
         2. (123) 456-7890

        (2) Times extracted from file:
         1. 8:30 am
         2. 17:00

        Extracted data saved to output.txt!

## Requirements
- Python 3.8+  

## How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/alu_regex-data-extraction-Mich-O.git

2. Navigate into the repository

   cd alu_regex-data-extraction-Mich-O-

3. **Specify input**
   
   By default, the input.txt file has sample data to be extracted.
   
   A user can edit the data to test the working of the python script. To do this:
   
      *nano input.txt, delete data in input.txt, populate input.txt with preferred data, ctrl+O, press ENTER, ctrl+X*

4. Run the script:
   
   python main.py
