import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            all_text += text + "\n"
    with open('allText.txt', 'w', encoding='utf-8') as file:
        file.write(all_text)
    return all_text

# 指定要读取的PDF文件路径
pdf_path = "./rootcloud_public.pdf"

# 调用函数提取文本
all_text = extract_text_from_pdf(pdf_path)

# 打印提取的文本
#print(all_text)
