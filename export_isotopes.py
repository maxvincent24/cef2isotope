

## Import dependencies
import pandas as pd
from lxml import etree
import sys


path_file = sys.argv[1]
file_basename = '.'.join(path_file.split('.')[:-1])

## Parse tree of cef file
tree = etree.parse(path_file)


## For each isotope, we create a list of its infos
# <whole_infos> will be a list of lists (each isotope)
whole_infos = []


## From xpath, we can get all the infos :
# /CEF/CompoundList/Compound/Location : compound MZ, RT and intensity
# /CEF/CompoundList/Compound/Spectrum/MSPeaks/p : isotope x, rx, y, z, s

for compound in tree.xpath('/CEF/CompoundList/Compound'):

    #print(100 * '-')

    isotope_infos = []

    ## location
    location = compound.xpath('Location')
    
    for loc in location:

        # compound ID
        compoundID = loc.get('m') + '@' + loc.get('rt')
        #print(f'compoundID : {compoundID}')

        isotope_infos.extend([compoundID, loc.get('m'), loc.get('rt')])
        
        # intensity
        intensity = loc.get('a')
        #print(f'intensity : {intensity}')

    ## isotopes
    isotopes = compound.xpath('Spectrum/MSPeaks/p')

    for isotope in isotopes:

        isotope_infos_curr = isotope_infos[:]

        x = isotope.get('x')
        rx = isotope.get('rx')
        y = isotope.get('y')
        z = isotope.get('z')
        s = isotope.get('s')

        isotope_infos_curr.extend([s, x, rx, y, z])
        #print(isotope_infos_curr)

        whole_infos.append(isotope_infos_curr)


#print('\n')

print(f'Total number of isotopes : {len(whole_infos)}')

# Convert list of lists to pandas dataframe
columns = ['compoundID', 'parentMZ', 'parentRT', 'adduct', 'x', 'rx', 'y', 'z']
exported_isotopes = pd.DataFrame(whole_infos, columns=columns)
print(exported_isotopes.shape)

# Save pandas dataframe to csv file
exported_isotopes.to_csv(file_basename + '.csv', index=False, header=True)

print('csv file successfully created :)')


