import PyPDF4
import docx
import openpyxl

#Creates a new document for the report
ceo_report = docx.Document()

#Adds the contents of the operations document to the ceo report
operations_file = docx.Document('text_files/operations.docx')

ceo_report.add_heading("Operations", 1)

for paragraph in operations_file.paragraphs:
    ceo_report.add_paragraph(paragraph.text)

ceo_report.add_page_break()

#Adds the contents of the sales spreadsheet to the ceo report
sales_file = openpyxl.load_workbook('text_files/sales.xlsx')

#Adds the contents of the marketing PDF to the ceo report
marketing_file = open('text_files/marketing.pdf', 'rb')

ceo_report.add_heading("Marketing", 1)

pdfReader = PyPDF4.PdfFileReader(marketing_file)

pdf_page = pdfReader.getPage(0)

#Pulls text from page and fixes the extraneous spaces and new lines 
pdf_text = pdf_page.extractText().split("\n")

ceo_report.add_paragraph(pdf_text)

marketing_file.close()

#Adds the contents of the IT webpage to the ceo report
it_file = open('text_files/IT.html', 'r')

#Saves the CEO report document to the text_files folder
ceo_report.save("text_files/ceo_report.docx")