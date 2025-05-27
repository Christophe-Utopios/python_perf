from lxml import etree

with open("./exercices/correction_slide_66/livres.xml", "r", encoding="utf-8") as reader:
    content = reader.read()
    source = etree.fromstring(content)
    transform = etree.parse("./exercices/correction_slide_66/transform.xsl")
    transformer = etree.XSLT(transform)
    result = transformer(source)

with open("./exercices/correction_slide_66/new_result.xml", 'w', encoding="utf-8") as file:
    file.write(str(result))

print(result)