import os, sys
from itertools import islice
import re
pattern = re.compile(".*(import|package).*(hbase)")
rootdir = "hbase-2.1.0"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:

        file_path = os.path.join(subdir, file)

        # print(file_path)
        # print(os.path.dirname(file_path))
        if file_path.split(".")[-1] == "java":
            # print(file_path)
            try:
                with open(file_path, "r+") as fo:
                    for index in range(100):
                        line = fo.readline()
                        # print(line)
                        if pattern.match(line):
                            print(line)
                            importOrpackage = line.split(" ")[1]
                            importOrpackage = importOrpackage.replace(";", "")
                            importOrpackage = importOrpackage.split(".")[-1]
                            importOrpackage = importOrpackage.replace("\n", "")
                            # importOrpackage = importOrpackage.replace(" ", "")
                            temp = file_path.replace("\\", "/")
                            # print(temp + " -> " + importOrpackage + ".java")
            except:
                pass
