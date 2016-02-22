# Author : Mandeep Singh
# Bio : https://github.com/daxlab
# A small utility to download individual files from a github repo.
# License : MIT

import urllib2
import argparse

parser = argparse.ArgumentParser(description="A small utility to download individual files from a github repo.")
parser.add_argument("-u", "--url", help="path to image file", required=True)
args = parser.parse_args()

url = args.url

# remove blob
url = url.replace("/blob", "")
url = url.replace("github", "raw.githubusercontent")
# print url
filename = url.split('/')[-1]
# print filename

print "Hang on ... Your file is downloading ..."
f = urllib2.urlopen(url)
data = f.read()
with open(filename, "wb") as code:
    code.write(data)

