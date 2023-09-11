import PyPDF2

pdfs = ['pdf1.pdf', 'pdf2.pdf']

merger = PyPDF2.PdfMerger()
try:
    for pdf in pdfs:
        merger.append(pdf)
except Exception as e:
    print("Error :- ", e)
merger.write("result.pdf")
merger.close()
