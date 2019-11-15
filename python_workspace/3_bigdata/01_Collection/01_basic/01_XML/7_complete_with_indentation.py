from xml.etree.ElementTree import Element, dump, SubElement,ElementTree

def indent(elem, level = 0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.startswith()):
            elem.tail = i

note = Element("note")
to = Element('to') # 자식 노드
to.text = "Tove" # 현재 엘리먼트(Tag)에 값 추가
note.append(to) # 부모 노드에 자식노드 추가

SubElement(note, "From").text="jani"#SubElement를 활용ㅎ여 자식 노드에 추가

dummy = Element("dummy")
note.insert(1,dummy)
note.remove(dummy)

note.attrib["date"]="20190722"

SubElement(note,"geading").text = "reminder"
SubElement(note,"body").text = "don't forget me this weekend!"

indent(note)

dump(note)

ElementTree(note).write("note.xml")


