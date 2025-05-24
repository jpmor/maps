import xml.etree.ElementTree as ET
import re
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python alter_kml.py <kml_file_path>")
        sys.exit(1)

    kml_file = sys.argv[1]
    tree = ET.parse(kml_file)
    root = tree.getroot()
    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
    placemarks = root.findall('.//kml:Document/kml:Placemark', namespaces=namespace)
    for placemark in placemarks:
        krs_name_short = placemark.find('.//kml:SimpleData[@name="krs_name_short"]', namespaces=namespace).text
        name_element = ET.Element(f'{{{namespace["kml"]}}}name')
        name_element.text = re.sub(r'\s+', ' ', krs_name_short).strip()
        placemark.insert(0, name_element)

    ET.register_namespace('kml', namespace['kml'])
    tree.write(kml_file, encoding='utf-8', xml_declaration=True)
