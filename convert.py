import fitz  # PyMuPDF
import csv
import sys
import argparse

def pdf_to_csv(pdf_path, csv_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Open a CSV file to write the extracted data
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
#
#Year Title Director MPAA Runtime J E R K S            
            # Extract text from the page
            text = page.get_text()
 
            # Split the text into lines
            lines = text.split('\n')
            #print(lines)
            for line in lines:
            

# lines looks like
# ['6/5/12 5:15 PM', 'The List', 'Page 44 of 44', 'http://kunalbhat.com/thelist/', 'Gran Torino', '2008', 'Forgetting Sarah Marshall', 'Nicholas Stoller', 'R', '111', '0', '0', '0', '0', '0', '1985', 'To Live and Die in L.A.', 'William Friedkin', 'R', '116', '0', '0', '0', '0', '0', '']

            
            
            print("-----------------------------------------------") 
            # Write each line to the CSV file
            for line in lines:
                csv_writer.writerow([line])
    
    print(f"PDF successfully converted to CSV: {csv_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to CSV")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_csv", help="Path to the output CSV file")
    args = parser.parse_args()

    pdf_to_csv(args.input_pdf, args.output_csv)

if __name__ == "__main__":
    main()
