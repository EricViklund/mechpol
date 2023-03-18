from pylatex import Document, Section, Subsection, Figure, NoEscape, Command, Package
from pylatex.base_classes.command import Options
from pylatex.base_classes.containers import Environment
from pylatex.labelref import Marker, Label
from datetime import datetime
from shutil import copy
from os import makedirs

class Abstract(Environment):
    """A class to wrap LaTeX's abstract environment."""



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

    with doc.create(Abstract()) as abstract:
        abstract.append(NoEscape(open('doc/sections/abstract.txt').read()))

    with doc.create(Section("Introduction")):
        doc.append(NoEscape(open('doc/sections/introduction.txt').read()))

    with doc.create(Section("sample study")) as section:
        doc.append(NoEscape(open('doc/sections/sample_study.txt').read()))
    
        with section.create(Subsection("Centrifugal Barrel Polishing")):
            section.append(NoEscape(open('doc/sections/centrifugal_barrel_polishing.txt').read()))
    
        with section.create(Subsection("Coupon Cavity")):
            section.append(NoEscape(open('doc/sections/coupon_cavity.txt').read()))

        with section.create(Subsection(NoEscape(r"Nb\textsubscript{3}Sn Coating Using Tin Vapor-Diffusion"),label='nb3sn_coating')):
            section.append(NoEscape(open('doc/sections/nb3sn_coating.txt').read()))

        with section.create(Subsection(NoEscape(r"Surface Analysis of Mechanically Polished Nb\textsubscript{3}Sn Coated Samples"),label='sample_analysis')):
            section.append(NoEscape(open('doc/sections/sample_analysis.txt').read()))

    with doc.create(Section(NoEscape(r"Polishing a Nb\textsubscript{3}Sn Cavity Using CBP"),label='cavity_cbp')) as section:
        doc.append(NoEscape(open('doc/sections/cavity_cbp.txt').read()))

        with section.create(Subsection(NoEscape(r"Low Temperature Re-coating Procedure"),label='recoating')):
            section.append(NoEscape(open('doc/sections/recoating.txt').read()))

        with section.create(Subsection(NoEscape(r"SRF Cavity RF-Performance Testing"),label='vts')):
            section.append(NoEscape(open('doc/sections/vts.txt').read()))

        with section.create(Subsection(NoEscape(r"Performance of a Polished Nb\textsubscript{3}Sn SRF Cavity"),label='cavity_results')):
            section.append(NoEscape(open('doc/sections/cavity_results.txt').read()))

    with doc.create(Section("Discussion")):
        doc.append(NoEscape(open('doc/sections/discussion.txt').read()))

    with doc.create(Section("Conclusion")):
        doc.append(NoEscape(open('doc/sections/conclusion.txt').read()))
        
    
    try:
        makedirs('.tmp')
    except:
        None
    copy('doc/bibliography/bib.bib','.tmp/')
    doc.append(Command('bibliography',
                    arguments='bib'))

    doc.generate_pdf(".tmp/"+datetime.now().strftime("%Y-%m-%d"))