from xml.etree.ElementTree import Element,parse
import xml.etree.ElementTree as ET


tree = ET.parse("students_info.xml")
note = tree.getroot()
counter = 0

# while counter <= 8 :
for child in note.getiterator():
    if child.tag == "student":
        for key in child.keys():
            if key == 'name' or key == 'sex':
                print(child.get(key))
        age_tag = child.find("age")
        print(age_tag.text)
        major_tag = child.find("major")
        print(major_tag.text)
                # computer_tag = child1.find("language")

                    # print("없음")
                # else:
                #     print(computer_tag.text)
    # counter =counter +1




