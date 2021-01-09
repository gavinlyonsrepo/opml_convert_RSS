#!/usr/bin/env python3
"""python script to turn youtube opml sub file into text file for rss reader"""
# =======================HEADER=======================================
# title             : youtube_sub_convert.py
# description       : python script to turn youtube
# opml sub file or JSON  into text file for rss reader newsboat.
# author            : Gavin Lyons
# date              : OCT  2019
# version           : 1.3-3
# web               : See __URL__
# mail              : glyons66@hotmail.com
# python_version    : 3.8.5

# ==========================IMPORTS======================
# Import the system modules needed to run
import os
from xml.etree import ElementTree
import argparse
import json
from sys import platform

# =============Functions==============
# metadata
__VERSION__ = "1.3"
__URL__ = "https://github.com/gavinlyonsrepo/opml_convert_RSS"


# ================== FUNCTIONS ===============================
def opml_txt(text):
    """ function to turn opml(xml) file into textfile two parts
    parse the input and create output
    Stage 1 Parse the input file, json or xml
    Stage 2 Create the output file , txt
    """
    
    msg_func("bold", "Start in main")
    urls = []
    texts = []
    infilename, outfilename, tagname = process_cmd_arguments()
    ext = os.path.splitext(infilename)[-1].lower()
    
   #Parse the input file, json or xml, Stage 1
    try:
        if ext == ".xml":
            with open(infilename, 'rt') as inputfile:
                tree = ElementTree.parse(inputfile)
            for node in tree.findall('.//outline'):
                url = node.attrib.get('xmlUrl')
                if url:
                    urls.append(url)

            for node in tree.findall('.//outline'):
                text = node.attrib.get('text')
                if text:
                    texts.append(text)

            texts.pop(0)
            
        elif ext == ".json":
            
            with open(infilename, 'rt') as inputfile:
                data = json.load(inputfile)

            for mychannel in data:
                url = mychannel['snippet']['resourceId']['channelId']
                if  url:
                        urls.append("https://www.youtube.com/feeds/videos.xml?channel_id="+ url)
                   
                text = mychannel['snippet']['title']
                   
                if text:
                    texts.append(text)
            
        else:
            raise Exception("unknown extension")
            quit()
        
    except Exception as error:
        msg_func("red", "Error: with input file:  {} = {}".format(infilename, error))
        quit()
    else:
      print("Input file {} parsing completed.".format(infilename))


# Create the output file , Stage 2
    try:
        with open(outfilename, "w") as myoutfile:
            for i, j in zip(urls, texts):
                myoutfile.write('{0}  "~{1}"  {2}'.format(i, j, tagname) + '\n')
    except Exception as error:
        msg_func("red", "Error: With output file: {} = {}".format(outfilename, error))
        quit()
    else:
        print("Output file {} created. tagname {}.".format(outfilename, tagname))


def process_cmd_arguments():
    """Parse the command line arguments"""
    str_desc = "URL help at: {}".format(__URL__)
    parser = argparse.ArgumentParser(description=str_desc)
    parser.add_argument('-v', help='Print version and quit', default=False,
                        dest='version', action='store_true')
    parser.add_argument('-i', help='input filename and/or full path',
                        type=str, dest='infile')
    parser.add_argument('-o', help='output filename and/or full path, default ./outfile.txt',
                        type=str, default='outfile.txt', dest='outfile')
    parser.add_argument('-t', help='tagname,  default = youtube',
                        type=str, default='youtube', dest='tagname')
    args = parser.parse_args()
    if args.version:
        msg_func("bold", "Version: " + __VERSION__)
        msg_func("bold", "Endex")
        msg_func("line", "")
        quit()

    if args.infile:
        infilename = args.infile
    else:
        msg_func("red", "Error: No input file given")
        quit()

    if args.tagname:
        tagname = args.tagname

    if args.outfile:
        outfilename = args.outfile

    return infilename, outfilename, tagname


def msg_func(myprocess, mytext):
    """NAME : msg_func
    DESCRIPTION :prints to screen
    prints line, text.
    INPUTS : $1 process name $2 text input
    PROCESS :[1]  print line 
    [2] print text  "green , red ,blue "
    NOTE: only works for linux , for windows just prints text as asni escape codes 
    did not work in powershell
    """
    if platform == 'win32':
        print(mytext)
    else:
        # colours for print
        blue = '\033[94m'
        red = '\033[91m'
        bold = '\033[1m'
        end = '\033[0m'
        if myprocess == "line":  # print blue horizontal line of =
            print(blue + "="*80 + end)

        if myprocess == "red":  # print red text
            print(red + mytext + end)

        if myprocess == "blue":  # print blue text
            print(blue + mytext + end)

        if myprocess == "bold":  # print bold text
            print(bold + mytext + end)


# =====================MAIN===============================
if __name__ == '__main__':
    msg_func("line", "")
    opml_txt("Start")
    msg_func("bold", "Endex")
    msg_func("line", "")
else:
    opml_txt("Imported {}".format(__name__))
# =====================END===============================
