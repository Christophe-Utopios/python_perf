from lxml import etree

# Charger le document XML
source_doc = etree.parse("./demos/09_xsl/source.xml")

# Charger la feuille de style
style_doc = etree.parse("./demos/09_xsl/style.xsl")

# Créer un transformateur
transformer = etree.XSLT(style_doc)

result = transformer(source_doc)

with open("./demos/09_xsl/new_result.xml", "w") as file:
    file.write(str(result))