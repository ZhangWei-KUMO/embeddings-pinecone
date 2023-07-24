import csv

def convert_csv_to_text(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        output = []
        for row in reader:
            description = ', '.join([f"{key}: {value}" for key, value in row.items()])
            output.append(description)
        text = '. '.join(output)
        with open('allText.txt', 'w', encoding='utf-8') as file:
            file.write(text)
        return text

csv_file = 'table_65_2.csv'
text = convert_csv_to_text(csv_file)
print(text)
