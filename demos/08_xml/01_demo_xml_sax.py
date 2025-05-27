import xml.sax

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    # Appelée automatiquement par le parseur à chaque balise d'ouverture
    def startElement(self, name, attrs):
        print(f"élément trouvé {name}")
        if attrs:
            print(f"Attributs {attrs}")
            for attr in attrs.values():
                print(attr)

    # Appelée automatiquement par le parseur à chaque balise de fermeture
    def endElement(self, name):
        print(f"Fin de l'élément : {name}")

xml_handler = XMLHandler()

# Création d'un parseur SAX
parser = xml.sax.make_parser()

parser.setContentHandler(xml_handler)

with open("./demos/08_xml/exemple.xml") as file:
    parser.parse(file) # Lance le traitement, déclenche les méthodes du handler