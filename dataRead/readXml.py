import xml.etree.ElementTree as ET

# Parsea el archivo XML
tree = ET.parse('data.xml')
root = tree.getroot()


# Convierte el XML en un diccionario
'''xml_dict = {}
for child in root:
    if len(child) > 0:
        xml_dict[child.tag] = {}
        for subchild in child:
            xml_dict[child.tag][subchild.tag] = subchild.text
    else:
        xml_dict[child.tag] = child.text
'''

# Convierte el XML en un diccionario
xml_dict = {child.tag: {subchild.tag: subchild.text for subchild in child} 
            if len(child) > 0 else child.text for child in root}

print(xml_dict)
