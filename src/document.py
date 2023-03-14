from pylatex import Document, Section, Subsection, Figure, NoEscape, Command, Package
from pylatex.base_classes.command import Options
from pylatex.labelref import Marker, Label
from datetime import datetime



if __name__ == '__main__':

    documentclass = Command('documentclass',
                            options=Options('reprint','amsmath','amssymb','aps'),
                            arguments=NoEscape(r'revtex4-2'))

    doc = Document(documentclass=documentclass)

    doc.append(Command('bibliography',
                    arguments='bib'))

    doc.generate_pdf(datetime.now().strftime("%Y-%m-%d"))