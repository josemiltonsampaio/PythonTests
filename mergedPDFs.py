import PyPDF2
import os

pdfFiles = []

for fileName in os.listdir("."):
    if fileName.endswith(".pdf"):
        pdfFiles.append(fileName)

if pdfFiles:
    pdfWriter = PyPDF2.PdfFileWriter()

for file in pdfFiles:
    pdfFile = open(file, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutputFile = open("merged.pdf", "wb")
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()
