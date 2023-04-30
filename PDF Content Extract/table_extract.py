import tabula


tables = tabula.read_pdf("enter_file_name.pdf", pages="all")
print(type(tables[0]))
df = tables[0]
print(df[df.height > 5])