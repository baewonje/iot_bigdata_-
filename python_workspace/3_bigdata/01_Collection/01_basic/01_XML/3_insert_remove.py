from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note')

# <> <- 노드
# <노드명 속성 = "값">
# <노드A>
#  값
# </노드A>
#
to = Element('to') # 자식 노드
to.text = "Tove" # 현재 엘리먼트(Tag)에 값 추가
note.append(to) # 부모 노드에 자식노드 추가

SubElement(note, "From").text="jani"#SubElement를 활용ㅎ여 자식 노드에 추가
# 아래와 동일한 결과이다.
# from_tag = Element("from")
# from_tage.text = "jani"
# note.append(from_tag)
dump(note)

dummy = Element("dummy")
note.insert(1,dummy)
dump(note)
note.remove(dummy) # 부모 노드에 있는 자식 노드를 인자로 넘겨줘야 한다.
dump(note)

