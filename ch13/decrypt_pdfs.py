#!env python3
'''
PDF decrypter with PyPDF2
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

            if(pdfreader.isEncrypted == True):
                try:
                    pdfreader.decrypt(sys.argv[1])
                except Exception as e:
                    print("Something didn't work: %s" % e)
                    continue
                decrypted_filepath = "%s_decrypted.pdf" % filepath
                pdfwriter = PyPDF2.PdfFileWriter()
                resultpdf = open(decrypted_filepath, 'wb')
                for page in range(pdfreader.numPages):
                    pdfwriter.addPage(pdfreader.getPage(page))
                pdfwriter.write(resultpdf)
                resultpdf.close()


if __name__ == "__main__":
    password = sys.argv[1]

    walk_tree('./input')