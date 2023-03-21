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

    with doc.create(Section("Introduction",label="introduction")):
        doc.append(NoEscape(open('doc/sections/introduction.txt').read()))

    with doc.create(Section("sample study",label="samplestudy")) as section:
        doc.append(NoEscape(open('doc/sections/sample_study.txt').read()))
    
        with section.create(Subsection("Centrifugal Barrel Polishing",label="centrifugalbarrelpolishing")):
            section.append(NoEscape(open('doc/sections/centrifugal_barrel_polishing.txt').read()))
    
        with section.create(Subsection("Coupon Cavity", label="couponcavity")):
            section.append(NoEscape(open('doc/sections/coupon_cavity.txt').read()))
            
            with section.create(Figure(position='htb')) as fig:
                fig.add_image('../doc/figs/Coupon_Cavity.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"(A) A schematic of the coupon cavity and the sample holder used to polish the Nb\textsubscript{3}Sn coated samples. The sample holder can hold 1 cm diameter disks by clamping the sides of the sample with set screws. (B) Pictures of the sample holder sitting outside the coupon cavity and with a sample mounted as seen from the inside of the coupon cavity."))
                fig.append(Label(Marker('couponcavity',prefix='fig')))

        with section.create(Subsection(NoEscape(r"Nb\textsubscript{3}Sn Coating Using Tin Vapor-Diffusion"),label='nb3sn_coating')):
            section.append(NoEscape(open('doc/sections/nb3sn_coating.txt').read()))

        with section.create(Subsection(NoEscape(r"Surface Analysis of Mechanically Polished Nb\textsubscript{3}Sn Coated Samples"),label='sample_analysis')):
            section.append(NoEscape(open('doc/sections/sample_analysis.txt').read()))
            
            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/Optical_Surface_Profiles.png',width=NoEscape(r'0.3\textwidth'))
                fig.add_caption(NoEscape(
                    r"Surface height maps of Nb\textsubscript{3}Sn samples mechanically polished for different lengths of time ranging from 2 to 8 hours compared to the initial state of the Nb\textsubscript{3}Sn coating."))
                fig.append(Label(Marker('opticalsurfaceprofiles',prefix='fig')))
            
            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/Surface_Roughness_Graph.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"Surface roughness of Nb\textsubscript{3}Sn samples mechanically polished for different lengths of time calculated from the surface height maps (top). The power spectral density (PSD) of the surface profile after different amounts of tumbling as well as the PSD of electropolished Nb and a thinly coated Nb/textsubscript{3}Sn film."))
                fig.append(Label(Marker('surfaceroughnessgraph',prefix='fig')))

            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/Material_Removal_Graph.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"The thickness of the Nb\textsubscript{3}Sn film after mechanically polished for different lengths of time using felt cubes or wooden spheres as the polishing media."))
                fig.append(Label(Marker('materialremovalgraph',prefix='fig')))

            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/SEM_Images.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"SEM micrographs of a Nb\textsubscript{3}Sn a thin coated sample (A), standard coated sample (B), a sample after polishing for 2 hours (C), and a sample after polishing for 6 hours (D)."))
                fig.append(Label(Marker('semimages',prefix='fig')))

            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/SEM_Images.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"SEM micrographs of a Nb\textsubscript{3}Sn a thin coated sample (A), standard coated sample (B), a sample after polishing for 2 hours (C), and a sample after polishing for 6 hours (D)."))
                fig.append(Label(Marker('semimages',prefix='fig')))

            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/Sample_Surface_Scratches.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"SEM micrograph showing a Nb\textsubscript{3}Sn sample polished for 30 hours using wooden spheres and a colloidal abrasive suspension. Nb\textsubscript{3}Sn films polished using wooden spheres show microscopic scratches and cracks on the surface. A cross section of the surface shows that the cracks penetrate deep into the film."))
                fig.append(Label(Marker('samplesurfacescratches',prefix='fig')))

            with section.create(Figure(position='t')) as fig:
                fig.add_image('../doc/figs/Sample_Surface_Damage_Layer.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"TEM images of a Nb\textsubscript{3}Sn sample polished using wooden spheres. The polishing procedure creates a 10 nm thick layer of disordered Nb\textsubscript{3}Sn."))
                fig.append(Label(Marker('samplesurfacedamagelayer',prefix='fig')))



    with doc.create(Section(NoEscape(r"Polishing a Nb\textsubscript{3}Sn Cavity Using CBP"),label='cavity_cbp')) as section:
        doc.append(NoEscape(open('doc/sections/cavity_cbp.txt').read()))

        with section.create(Subsection(NoEscape(r"Low Temperature Re-coating Procedure"),label='recoating')):
            section.append(NoEscape(open('doc/sections/recoating.txt').read()))

        with section.create(Subsection(NoEscape(r"SRF Cavity RF-Performance Testing"),label='vts')):
            section.append(NoEscape(open('doc/sections/vts.txt').read()))

        with section.create(Subsection(NoEscape(r"Testing the Polished Nb\textsubscript{3}Sn SRF Cavity"),label='cavity_results')):
            section.append(NoEscape(open('doc/sections/cavity_results.txt').read()))

            with section.create(Figure(position='htb')) as fig:
                fig.add_image('../doc/figs/VTS_Test_Graph.png',width=NoEscape(r'0.5\textwidth'))
                fig.add_caption(NoEscape(
                    r"The RF performance of the Nb\textsubscript{3}Sn-coated SRF cavity before and after mechanically polished and after a re-coating treatment."))
                fig.append(Label(Marker('vtstestgraph',prefix='fig')))


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