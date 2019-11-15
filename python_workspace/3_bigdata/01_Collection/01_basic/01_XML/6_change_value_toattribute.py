from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note', date = "20190722", to = "Tove")

# to = Element('to') # 자식 노드
# to.text = "Tove" # 현재 엘리먼트(Tag)에 값 추가
# note.append(to) # 부모 노드에 자식노드 추가

SubElement(note, "From").text="jani"#SubElement를 활용ㅎ여 자식 노드에 추가

dump(note)
