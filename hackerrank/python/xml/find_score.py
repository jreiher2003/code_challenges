import xml.etree.ElementTree as ET 


tree = ET.parse('hacker.xml')
root = tree.getroot()
count = 0
for child in root.iter():
    count += len(child.attrib)

print count