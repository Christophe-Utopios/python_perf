import xml.dom.minidom

dom_tree = xml.dom.minidom.parse("./demos/08_xml/exemple.xml")

root_element = dom_tree.documentElement

print(f"Element racine : {root_element.tagName}")

# Parcours les élément enfant du root
for node in root_element.childNodes:
    if node.nodeType == node.ELEMENT_NODE:
        print(f"Element : {node.tagName}")
        if node.hasAttributes():
            print("Attributs : ")
            for attr in node.attributes.values():
                print(attr)

        for child_node in node.childNodes:
            if child_node.nodeType == child_node.TEXT_NODE:
                print(f"Contenu : {child_node.data}")

# Exemple de modification du contenu
first_child = root_element.firstChild
first_child.data = "Nouveau contenu"

with open("./demos/08_xml/exemple.xml", "w") as file:
    dom_tree.writexml(file)
