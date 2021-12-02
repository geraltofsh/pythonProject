import glob

from bs4 import BeautifulSoup as Soup
import os

# folder = "C:\\Users\\mfg\\Desktop\\SVN\\autoScripts\\JMeter_Service\\FunctionTestScript\\CustomerQuote\\"
pattern = r'C:/Users/mfg/Desktop/SVN/CM_Service/tests/ServiceContractsTests/**/*.jmx'
# C:\Users\mfg\Desktop\SVN\CM_Service\tests\MaterialOrdersTests\resources\jmeter\jmx
for filename in glob.glob(pattern, recursive=True):
    with open(filename, 'r', encoding="utf8") as f:
        xml = f.read()
        f.close()
        soup = Soup(xml, features='lxml-xml')
        headers_count = len(soup.findAll("HeaderManager"))
        i = 1
        is_update = False
        if headers_count > 0:
            print("find the header manager in ", filename)
        for e in soup.findAll("HeaderManager"):
            if e["enabled"] == "true":
                for child in e.findAll("elementProp"):
                    if child["name"] == "Referer":
                        e["enabled"] = "false"
                        is_update = True
                        break

            i = i + 1

        if headers_count > 0 and is_update is True:
            f = open(filename, 'w', encoding="utf8")
            f.write(str(soup))
            print(filename, " modified ")
            f.close()
            headers_count = 0

# rpt_side = soup.TrdCaptRpt.RptSide
# rpt_side['Txt1'] = 'Updated'
# rpt_side.Pty['ID'] = 'Updated'

# print (soup)
