from xml.etree.ElementTree import Element, dump

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

dump(note)
dump(to)