#!/usr/bin/env python3
"""python script to turn youtube opml sub file into text file for rss reader"""
# =========================HEADER=======================================
# title             : youtube_sub_convert.py
# description       : python script to turn youtube
# opml sub file into text file for rss reader newsboat.
# author            :Gavin Lyons
# date              :17/08/2017
# version           : 1.0
# web               :https://github.com/gavinlyonsrepo/
# mail              :glyons66@hotmail.com
# python_version    : 3.6

# ==========================IMPORTS======================
# Import the system modules needed to run 
from xml.etree import ElementTree
import argparse
import sys

# =============Functions==============
# metadata
__VERSION__ = "1.1"
__URL__ = "https://github.com/gavinlyonsrepo/miscellaneous/tree/master/python/youtube_sub_convert"

# ================== FUNCTIONS ===============================
def opml_txt(text):
    """ function to turn opml file into textfile two parts
    parse and input and create output"""
    print(text)
    urls = []
    texts = []
    filename = process_cmd_arguments()

#  Parse the input file.
    try: 
        with open(filename, 'rt') as f:
            tree = ElementTree.parse(f)
        for node in tree.findall('.//outline'):
            url = node.attrib.get('xmlUrl')
            if url:
                urls.append(url)

        for node in tree.findall('.//outline'):
            text = node.attrib.get('text')
            if text:
                texts.append(text)
        
        texts.pop(0)
        
    except Exception as error:
            print("Problem with input file {} = {}".format(filename , error))
            quit()
    else:
            print("Input file {} parsed".format(filename))

# Create the output file.
    try:
        with open("outfile.txt", "w") as myoutfile:
            for i, j in zip(urls, texts):
                myoutfile.write('{0}  "~{1}"  youtube'.format(i, j) + '\n')
    except Exception as error:
            print("Problem making output file {}".format(error))
            quit()
    else:
            print("Output file outfile.txt created")

    print("End")


def process_cmd_arguments():
    """Parse the command line arguments"""
    str_desc = "URL help at: {}".format(__URL__)
    parser = argparse.ArgumentParser(description=str_desc)
    parser.add_argument( '-v', help='Print version and quit', default=False, dest='version', action='store_true')
    parser.add_argument(
        '-f', help='inputfile + filename',
        type=str, dest='file')
    args = parser.parse_args()
    if args.version:
       print("Version" + __VERSION__)
       quit()
       
    if args.file:
        filename = (sys.argv[2])
        return filename
    
    
# =====================MAIN===============================
if __name__ == '__main__':
    opml_txt("Start in main")
else:
    opml_txt("Imported {}".format(__name__))
# =====================END===============================
