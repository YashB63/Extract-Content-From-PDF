import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("enter_file_name.pdf"):
#     for element in page_layout:
#         #print(element)

text = extract_text("enter_file_name.pdf")
print(text)

pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)
names = [n[:-2] for n in matches]
print(names)