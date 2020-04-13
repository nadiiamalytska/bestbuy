import lxml.etree as ET
import webbrowser

output_file = "output.html"

xsl = ET.parse("sample.xsl")
transform = ET.XSLT(xsl)
dom = ET.parse("sample.xml")
transformed_dom = transform(dom)
result = ET.tostring(transformed_dom)

with open(output_file, 'w+') as f:
    output = str(result)
    f.write(output)

webbrowser.open(output_file, new=2)
