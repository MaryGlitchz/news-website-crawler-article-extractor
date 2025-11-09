from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def export_to_xml(data, file_path):
    root = Element("articles")
    for item in data:
        article = SubElement(root, "article")
        for k, v in item.items():
            child = SubElement(article, k)
            child.text = str(v)
    tree = ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)