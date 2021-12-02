import glob

# folder = "C:\\Users\\mfg\\Desktop\\SVN\\autoScripts\\JMeter_Service\\FunctionTestScript\\CustomerQuote\\"
pattern = r'C:/Users/mfg/Desktop/SVN/CM_Service/tests/SerializationTests/**/*.jmx'
# C:\Users\mfg\Desktop\SVN\CM_Service\tests\MaterialOrdersTests\resources\jmeter\jmx
for filename in glob.glob(pattern, recursive=True):
    with open(filename, 'r', encoding="utf8") as f:
        txt = f.read()
        f.close()
        modified = False
        if txt.find("./login.jmx") != -1:
            txt = txt.replace("./login.jmx", "../../../../JMeter/Login-Fragment.jmx")
            modified = True
        if txt.find("./Login.csv") != -1:
            modified = True
            txt = txt.replace("./Login.csv", "../../../../JMeter/login.csv")
        if txt.find("../../../../JMeter/Logout-Fragment.jmx") != -1:
            modified = True
            txt = txt.replace("../../../../JMeter/Logout-Fragment.jmx", "../../../../JMeter/Fragment_Logout.jmx")

        if modified:
            f = open(filename, 'w', encoding="utf8")
            f.write(str(txt))
            print(filename, " modified ")
            f.close()

