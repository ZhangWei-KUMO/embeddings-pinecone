import pdfplumber

# with pdfplumber.open("path/to/file.pdf") as pdf:
#     first_page = pdf.pages[0]
#     print(first_page.chars[0])
pdf = pdfplumber.open("./rootcloud_public.pdf")
page = pdf.pages[0]
print(page.find_table(table_settings={}))
print(page.chars[0])