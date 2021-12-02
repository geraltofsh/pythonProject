# import fnmatch
# import os
#
# matches = []
# for root, dirnames, filenames in os.walk(r'C:/Users/mfg/Desktop/SVN/autoScripts/JMeter_Service/TestFragement/SetUp'):
#     for filename in fnmatch.filter(filenames, '*.jmx'):
#         matches.append(os.path.join(root, filename))
import string

from bs4 import BeautifulSoup as Soup
import glob

# pattern = r'C:/Users/mfg/Desktop/SVN/autoScripts/JMeter_Service/**/*.jmx'
pattern = r'C:/Users/mfg/Desktop/SVN/CM_Service/tests/**/*.csv'
for filename in glob.glob(pattern, recursive=True):
    # with open(filename, 'r', encoding="utf8") as f:
    #     xml = f.read()
    #     f.close()
    #     # soup = Soup(xml, features='lxml-xml')
    #     headers_count = xml.find("ReceiptsUnplanned.jmx")
    #     if headers_count > 0:
    #         print(filename)
    if "login.csv" in filename.lower():
        print(filename)