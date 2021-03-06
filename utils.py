Systems = ['GASTRIC / METABOLISM',
           'HAEMATOLOGICAL',
           'CARDIOVASCULAR',
           'DERMATOLOGICALS',
           'UROGENITAL',
           'ENDOCRINE',
           'ANTIINFECTIVES',
           'ANTINEOPLASTIC / IMMUNOMODULATORY',
           'MUSCULO-SKELETAL',
           'NERVOUS',
           'ANTIPARASITICS',
           'RESPIRATORY',
           'SENSORY ORGANS']

selection = ['Name',
             'Max Phase',
             'Molecular Weight',
             'AlogP',
             'Polar Surface Area',
             '#Rotatable Bonds',
             'Inorganic Flag',
             'Heavy Atoms',
             'HBA (Lipinski)',
             'HBD (Lipinski)',
             'Molecular Species',
             'Molecular Formula']

numeric_columns = ['Max Phase',
                   'Molecular Weight',
                   'AlogP',
                   'Polar Surface Area',
                   '#Rotatable Bonds',
                   'Inorganic Flag',
                   'Heavy Atoms',
                   'HBA (Lipinski)',
                   'HBD (Lipinski)']

pca_columns = ['Molecular Weight',
               'AlogP',
               'Topological Polar Surface Area',
               'Rotatable Bond Count',
               'Inorganic Flag',
               'Heavy Atom Count',
               'Hydrogen Bond Acceptor Count',
               'Hydrogen Bond Donor Count',
               'double bond equivalents']

renaming_dict = {'HBD (Lipinski)': 'Hydrogen Bond Donor Count',
                 'HBA (Lipinski)': 'Hydrogen Bond Acceptor Count',
                 '#Rotatable Bonds': 'Rotatable Bond Count',
                 'Polar Surface Area': 'Topological Polar Surface Area',
                 'Heavy Atoms': 'Heavy Atom Count'}

colors_by_phase = ['rgb(15, 7, 135)',
                   'rgb(124, 6, 165)',
                   'rgb(202, 71, 120)',
                   'rgb(247, 149, 64)',
                   'rgb(240, 247, 33)']

colors_by_system = ['rgb(193, 114, 0)',
                    'rgb(115, 6, 0)',
                    'rgb(210, 17, 27)',
                    'rgb(248, 208, 206)',
                    'rgb(255, 124, 117)',
                    'rgb(160, 192, 164)',
                    'rgb(2, 39, 74)',
                    'rgb(112, 242, 128)',
                    'rgb(248, 231, 206)',
                    'rgb(136, 148, 161)',
                    'rgb(0, 89, 11)',
                    'rgb(118, 178, 235)',
                    'rgb(7, 67, 125)']
