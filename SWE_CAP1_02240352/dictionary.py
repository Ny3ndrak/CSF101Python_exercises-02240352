import docx as d2t

docx_file = 'dictionary.docx'
txt_file = 'dictionary.txt'

docx = d2t.process(docx_file)

file=open(txt_file, 'w', encoding='utf-8')
file.write(docx)
file.close()
