#!env python3
'''
PDF encrypter with PyPDF2
'''
import os
import sys
import PyPDF2

def walk_tree(folder):
    for folder, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filepath = ''.join( (folder,"/",filename) )
            print(filepath)
            pdfreader = PyPDF2.PdfFileReader(open(filepath, 'rb'), strict=False)
            pdfwriter = PyPDF2.PdfFileWriter()

            for page in range(pdfreader.numPages):
                pdfwriter.addPage(pdfreader.getPage(page))

            encrypted_filepath = "%s_encrypted.pdf" % filepath
            resultpdf = open(encrypted_filepath, 'wb')
            pdfwriter.encrypt(password)
            pdfwriter.write(resultpdf)
            resultpdf.close()

            # try to decrypt it
            pdfdblreader = PyPDF2.PdfFileReader(open(encrypted_filepath, 'rb'), strict=False)

            try:
                pdfdblreader.decrypt(sys.argv[1])
            except Exception as e:
                print("Something went wrong: %s" % e)
                exit()

            # Delete if the exception doesn't occur
            os.remove(filepath)


if __name__ == "__main__":
    password = sys.argv[1]

    walk_tree('./input')