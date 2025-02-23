from lxml import etree
import sys

xml_file = sys.argv[1]
path_w   = sys.argv[2]


# XML ファイルパス
#xml_file = 'work/_org_test1_presentation.xml'
#path_w = 'work/_new_test1_presentation.xml'

# XML を解析
tree = etree.parse(xml_file)

# 整形表示
xml_str = etree.tostring(tree, pretty_print=True).decode()


with open(path_w, mode='w') as f:
    f.write(xml_str)

#with open(path_w) as f:
#    print(f.read())
