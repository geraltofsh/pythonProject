import datetime
import glob
import os
import sys


def main(argv):
    # pattern = r'T:\qraleg_service\build\CATS_logs\**\*'
    pattern = argv[0]
    for filename in glob.glob(pattern, recursive=True):
        if os.path.isfile(filename):
            print(filename)
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
            today = datetime.datetime.today()
            if (today - modified_date).days > 7:
                try:
                    os.remove(filename)
                    print("The file is deleted.")
                except :
                    print("Warning: The file is unable to delete.")


if __name__ == '__main__':
    main(sys.argv[1:])
