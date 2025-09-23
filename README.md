# ALU Regex Data Extraction

This project demonstrates the use of **Regular Expressions (Regex)** in Python to extract structured data from raw text.  

## Features
The script can extract: 
- URLs  
- 10 digit Phone numbers  
- HTML tags
- 16 digit credit card numbers
- Hashtags
- .... and more

## Example
Input text: Hello, contact us using these numbers: 07123456678 or (123) 456-7890 and at the email info@wall.greens.co.uk.

Output: 2 Phone numbers extracted from file: ['0712345678', '(123) 456-7890']

## Requirements
- Python 3.8+  

## How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/alu_regex-data-extraction-Mich-O.git

2. Navigate into the repository

   cd alu_regex-data-extraction-Mich-O-

3. Specify input
   
   By default, the input.txt file has sample data to be extracted.
   
   A user can edit the data to test the working of the python script. To do this:
   
      *echo "sample data" >> input.txt*

4. Run the script
   
   python main.py
