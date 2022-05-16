from bs4 import BeautifulSoup

with open("text_files/famous_quotes.xml") as quote_file:
    xml_parse = BeautifulSoup(quote_file, "xml")