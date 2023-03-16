from pylatex import Document, Section, Subsection, Figure, NoEscape, Command, Package
from pylatex.base_classes.command import Options
from pylatex.labelref import Marker, Label
from datetime import datetime
from shutil import copy
from os import makedirs



if __name__ == '__main__':

    documentclass = Command('documentclass',
                            options=Options('reprint','amsmath','amssymb','aps'),
                            arguments=NoEscape(r'revtex4-2'))

    doc = Document(documentclass=documentclass)

    doc.append(Command('title',NoEscape(r'Improving Nb\textsubscript{3}Sn Cavity Performance Using Mechanical Polishing')))
   
    doc.append(Command('author','Eric Viklund'))
    doc.append(Command('affiliation','Department of Materials Science and Engineering, Northwestern University'))
    doc.append(Command('affiliation','Fermi National Accelerator Laboratory'))

    doc.append(Command('author','David N. Seidman'))
    doc.append(Command('affiliation','Department of Materials Science and Engineering, Northwestern University'))

    doc.append(Command('author','David Burk'))
    doc.append(Command('affiliation','Fermi National Accelerator Laboratory'))

    doc.append(Command('author','Sam Posen'))
    doc.append(Command('affiliation','Fermi National Accelerator Laboratory'))

    doc.append(Command('date',NoEscape(r'\today')))

    doc.append(NoEscape(r'\maketitle'))


    with doc.create(Section("Introduction")):
        doc.append(NoEscape(open('doc/sections/introduction/introduction.txt').read()))

    try:
        makedirs('.tmp')
    except:
        None
    copy('doc/bibliography/bib.bib','.tmp/')
    doc.append(Command('bibliography',
                    arguments='bib'))

    doc.generate_pdf(".tmp/"+datetime.now().strftime("%Y-%m-%d"))