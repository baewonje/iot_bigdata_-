from xml.etree.ElementTree import Element,parse
import xml.etree.ElementTree as ET

f = open('Korean2.xml','r', encoding='UTF-8')
text = f.read()
f.close()

print(text)

root_node = ET.fromstring(text)
print(root_node.find('data').text)

