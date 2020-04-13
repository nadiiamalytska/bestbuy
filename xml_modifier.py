import xml.etree.ElementTree

# модифікування текстових значень елементів (додавання/видалення) (2-3 значення)

xml_file = "sample.xml"
xml = xml.etree.ElementTree.parse(xml_file)
tree = xml.getroot()


def describe(item):
    name = item.find("Name")
    price = item.find("Price")
    print(name.text.strip())
    print(price.text.strip())


# Добавляет 2 текстовых значений элементов
appendix = "text"
for item in tree.findall('product'):
    name = item.find("Name")
    price = item.find("Price")
    print("До: ")
    describe(item)
    name.text = name.text.strip() + appendix
    price.text = price.text.strip() + "0"
    print("После: ")
    describe(item)

xml.write(xml_file)
print("\n\n")

# # Убирает 2 текстовых значений элементов
# removal = "текст"
# for item in tree.findall('product'):
#     name = item.find("Name")
#     price = item.find("Price")
#     print("До: ")
#     describe(item)
#     nameText = name.text.strip()
#     if nameText.endswith(removal):
#         name.text = nameText[:-len(removal)]
#     priceText = name.text.strip()
#     if priceText.endswith("0"):
#         priceText.text = priceText[:-len("0")]
#     print("После: ")
#     describe(item)
#
# xml.write(xml_file)
# print("\n\n")

from xml.etree import ElementTree

attr = 'custom_attribute'
attr2 = 'second_attribute'

# Добавляет 2 аттрибута и их значения в элементы
for item in tree.findall('product'):
    item.attrib[attr] = "value"
    item.attrib[attr2] = "value"
xml.write(xml_file)
result = ElementTree.tostring(tree, encoding='utf8', method='xml')
print(result)

# # Убиоает 2 аттрибута и их значения с элементов
# for item in tree.findall('product'):
#     try:
#         del item.attrib[attr]
#     except KeyError:
#         pass
#     try:
#         del item.attrib[attr2]
#     except KeyError:
#         pass
# xml.write(xml_file)
# result = ElementTree.tostring(tree, encoding='utf8', method='xml')
# print(result)
