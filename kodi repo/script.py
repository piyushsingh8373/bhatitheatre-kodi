import os
import hashlib
from xml.etree import ElementTree as ET

ADDONS_DIR = '.'
ADDONS_XML = 'addons.xml'
CHECKSUM_FILE = 'addons.xml.sha256'

def get_addons():
    xml_blocks = []
    for folder in os.listdir(ADDONS_DIR):
        path = os.path.join(ADDONS_DIR, folder)
        if os.path.isdir(path) and os.path.exists(os.path.join(path, 'addon.xml')):
            tree = ET.parse(os.path.join(path, 'addon.xml'))
            root = tree.getroot()
            xml_blocks.append(ET.tostring(root, encoding='unicode'))
    return xml_blocks

def create_addons_xml():
    print("Generating addons.xml...")
    addons = get_addons()
    addons_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n' + "\n".join(addons) + '\n</addons>'

    with open(ADDONS_XML, 'w', encoding='utf-8') as f:
        f.write(addons_xml)

    sha256 = hashlib.sha256(addons_xml.encode('utf-8')).hexdigest()
    with open(CHECKSUM_FILE, 'w') as f:
        f.write(sha256)

    print("addons.xml and addons.xml.sha256 created.")

create_addons_xml()
