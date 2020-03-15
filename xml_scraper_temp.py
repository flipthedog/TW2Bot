import xml.etree.ElementTree as ET


text_file = open("C:/Users\Jan\Documents\Projects\TribalWars\pyTWBot\worldinfo.xml", "r")
n = text_file.read()
text_file.close()

new_source = "<html xmlns=\"http://www.w3.org/1999/xhtml\"><head><style id=\"xml-viewer-style\"> </style>" + n.split("</style>")[1]
new_source = new_source.split("</win>")[0] + "</win></body></html>"
print(new_source)

root = ET.fromstring(new_source)

info = {}

for child in root.iter():
    tagname = child.tag
    info[tagname] = child.text
    if tagname is "wind":
        continue
    print(child.tag, child.attrib, child.text)