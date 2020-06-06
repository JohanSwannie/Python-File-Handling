import xml.etree.ElementTree as ET

tree = ET.parse('xml-example01.xml')
root = tree.getroot()

print(root.tag, '  ', root.attrib)

for child in root:
    print(child.tag, '  ', child.attrib)

print(root[0][0][0].attrib)
print(root[0][0][0][2].text)

for favvy in root.iter('favorite'):
    print(favvy.attrib)
print('-' * 100)

for sport in root.findall('sport'):
    popularity = sport.find('popularity').text
    name = sport.get('name')
    print(name, popularity)

for popularity in root.iter('popularity'):
    popularity_N = int(popularity.text) + 1
    popularity.text = str(popularity_N)
    popularity.set('upd', 'y')

tree.write('xml-example01.xml')

for sport in root.findall('sport'):
    popularity = int(sport.find('popularity').text)
    if popularity < 65:
        root.remove(sport)

tree.write('xml-example01.xml')

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
