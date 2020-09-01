# 09 Working with PDFs

# There are several packages to work with PDFs file.
# History of pyPdf, PyPDF2, and PyPDF4
# The original pyPdf package was released way back in 2005. The last official release of pyPdf was in 2010.
# After a lapse of around a year, a company called Phasit sponsored a fork of pyPdf called PyPDF2.
# The code was written to be backwards compatible with the original and worked quite well for several years, with its last release being in 2016.
# There was a brief series of releases of a package called PyPDF3, and then the project was renamed to PyPDF4.
# All of these projects do pretty much the same thing, but the biggest difference between pyPdf and PyPDF2+ is that the latter versions added Python 3 support.
# There is a different Python 3 fork of the original pyPdf for Python 3, but that one has not been maintained for many years.
# While PyPDF2 was recently abandoned, the new PyPDF4 does not have full backwards compatibility with PyPDF2.

# Although Mosh course is on "pyPDF2", I am using "pyPDF4"

import PyPDF4

with open("first.pdf", "rb") as pdf_file: # We use the "with" to open a PDF file. And we open it in the "rb" mode read binary, so we can use it as a "reader" object with the PyPDF$ package.
    reader = PyPDF4.PdfFileReader(pdf_file)
    print(reader.numPages) # With the reader oject we can use several methods. In this case "numPages" returns the number os pages
    page = reader.getPage(0) # With the "getPage" method we can geta page from the PDF. Important, the page count starts at 0
    page.rotateClockwise(90) # With the page object we can use several other methods. In here "rotateClockwise()" to rotate the page. This is only rotates the page object in memory, and does not modify the original PDF. So we need to write this to a separe PDF file.
    writer = PyPDF4.PdfFileWriter() # Here we create the writer object.
    writer.addPage(page) # Here we are adding the page object to our new pdf, in memory.
    with open("rotated.pdf", "wb") as output: # We create a new file and use the "wb" write binary.
        writer.write(output) # we use our writer to write to the new file.

merger = PyPDF4.PdfFileMerger() # To merge pdf we first create a merger object with the  ".PdfFileMerger()"
file_names = ["first.pdf", "second.pdf"] # Here we are using a list with the PDF file we want to merge. We cloud itarete over all the PDF in a folder.
for file_name in file_names: # with the for loop we iterate over the list with the PDf files
    merger.append(file_name) # We use the ".append()" method to add each PDF to our merger object in memory.

merger.write("combined.pdf") # With the ".write()" we create a new file in disk from our merge object. Here e named it "combined.pdf"