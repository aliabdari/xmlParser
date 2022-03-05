import numpy as np
import xml.etree.ElementTree as ET


def parse_xml_file():
    tree = ET.parse('TrainTestData.xml')

    # getting the parent tag of the xml document
    root = tree.getroot()

    for i in range(len(root)):
        time1 = int(float(root[i].attrib['time']))
        print(len(root[i]))
        for j in range(len(root)):
            time2 = int(float(root[j].attrib['time']))
            if time1 >= time2 or time2 - time1 > 1:
                continue


if __name__ == '__main__':
    parse_xml_file()
