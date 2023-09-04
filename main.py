import PyPDF2

pdfs = ['pdf1.pdf', 'pdf2.pdf']

merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
