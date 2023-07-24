import pdfplumber
import csv

def extract_tables_to_csv(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            tables = page.extract_tables()

            for table_number, table in enumerate(tables):
                csv_path = f"table_{page_number + 1}_{table_number + 1}.csv"

                with open(csv_path, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(table)

                print(f"Table {table_number + 1} on page {page_number + 1} extracted to {csv_path}")

# 使用示例
pdf_path = "./rootcloud_public.pdf"
extract_tables_to_csv(pdf_path)
