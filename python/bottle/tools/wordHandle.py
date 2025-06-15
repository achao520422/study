import zipfile
import xml.etree.ElementTree as ET


def extract_text_from_docx(docx_path):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    text = []

    with zipfile.ZipFile(docx_path) as docx:
        # 提取主文档内容
        document_xml = docx.read('word/document.xml')
        return document_xml.decode('utf8').replace('>', '>\n')


import zipfile
import xml.etree.ElementTree as ET
import json


def docx_to_json(path_to_docx):
    # 解压.docx文件
    with zipfile.ZipFile(path_to_docx, 'r') as z:
        print(z)
        # 读取document.xml文件
        content = z.read('word/document.xml')

    # 解析XML
    tree = ET.fromstring(content)

    # 示例：简单地提取所有文本 - 这里需要根据实际情况调整
    texts = []
    for paragraph in tree.findall('.//w:p',
                                  namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}):
        text = ''.join(node.text for node in paragraph.findall('.//w:t', namespaces={
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}) if node.text)
        texts.append(text)

    # 将结果转换为JSON
    return json.dumps({'paragraphs': texts}, ensure_ascii=False)


# 使用函数
# json_output = docx_to_json('胡涛 .docx')
# print(json_output)

print(extract_text_from_docx('胡涛 .docx'))