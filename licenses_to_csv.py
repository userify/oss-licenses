#! /usr/bin/env python

import csv

f = open("README.md").read()
output = open("licenses.csv", "w")
c = csv.writer(output, dialect="excel", quoting=csv.QUOTE_MINIMAL)

f = f.split("\n## ")

f = f[1:]
linecount = 0

for counter,tpackage in enumerate(f):
    package = tpackage.split("\n")
    linecount += len(package)
    package_name = package[0].split(":")[1].strip()
    print counter, linecount
    package_license = [line for line in package if line.startswith("License:")][0].split(":")[1].strip()
    license = tpackage.split("Full License Text:")[1].strip()
    c.writerow([package_name, package_license, license])


