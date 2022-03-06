import xml.etree.ElementTree as ET
import os
import time
from tqdm import tqdm


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def parse_xml_file():
    tree = ET.parse('TrainTestData.xml')

    # getting the parent tag of the xml document
    root = tree.getroot()

    if os.path.exists("data.txt"):
        os.remove("data.txt")
    data_file = open("data.txt", "w")

    for i in tqdm(range(len(root)-2)):
        time1 = int(float(root[i].attrib['time']))
        l1 = []
        for i_element in root[i]:
            l1.append(i_element.attrib['id'])
        for j in range(i + 1, i + 2):
            time2 = int(float(root[j].attrib['time']))
            if time1 >= time2 or time2 - time1 > 1:
                continue
            l2 = []
            for j_element in root[j]:
                l2.append(j_element.attrib['id'])
            l1_l2_intersection = intersection(l1, l2)
            for vehicle in l1_l2_intersection:
                for k in range(j + 1, j + 2):
                    time3 = int(float(root[k].attrib['time']))
                    if time2 >= time3 or time3 - time2 > 1:
                        continue
                    l3 = []
                    for k_element in root[k]:
                        l3.append(k_element.attrib['id'])
                    if vehicle in l3:
                        l1_v_index = l1.index(vehicle)
                        l2_v_index = l2.index(vehicle)
                        l3_v_index = l3.index(vehicle)
                        data_file.write(vehicle)
                        data_file.write(",")
                        data_file.write(root[i][l1_v_index].attrib['x'] + "," + root[i][l1_v_index].attrib['y'])
                        data_file.write(",")
                        data_file.write(root[j][l2_v_index].attrib['x'] + "," + root[j][l2_v_index].attrib['y'])
                        data_file.write(",")
                        data_file.write(root[k][l3_v_index].attrib['x'] + "," + root[k][l3_v_index].attrib['y'])
                        data_file.write("\n")
    data_file.close()


if __name__ == '__main__':
    start_time = time.time()
    parse_xml_file()
    print("--- %s seconds ---" % (time.time() - start_time))
