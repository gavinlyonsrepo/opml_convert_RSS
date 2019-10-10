Overview
--------------------------------------------
* Name: opml_convert_RSS
* Description: Command line python utility , converts opml(xml) to RSS.
* Author: Gavin Lyons.
* Software: python 3.6.8
* Copyright: 2019 (C) GPL 
 
Description
---------

Command line python utility, 
Converts the opml(Xml) file of a youtube user subscriptions provided by youtube, 
into a text file which can added to RSS reader setup file
file, like newsboat for example. Thus converting your youtube subscriptions,
into a group of tagged RSS feeds. 
Example input xml and output txt files are available in Documents folder
The user can select input file path, output file path and custom tag.

**Input:**

opml(xml) file provided by user on command prompt using -i option.

**Output:**

The output.txt is file is provided by user using -o option 
If no file is provided the program uses a default file called output.txt at path of
program. The output file is in file in following format:

[url] ~"[video_title]" [tag]

https://www.youtube.com/feeds/videos.xml?channel_id=UCI999ua  "~Python Training by Bader"  youtube

Where tag default = youtube, A custom tag can be added using -t option.

Usage
--------

NOTE: Currently only works on Linux.

1. Download the python program, opml_convert_rss.py.
2. In a web browser navigate to subscription manager page of youtube.
https://www.youtube.com/subscription_manager
3. At bottom of page click on "Export to RSS readers -- Export subscriptions".
4. This subscription_manager file will be downloaded into an opml(xml) file.
5. Run program in terminal. 

* $ python3 opml_convert_rss.py -i infile -o outfile -t tech
* -i infile is the full path and/or filename of input xml file.
* -o outfile is the full path and/or filename of output txt file.
* -t tech is a custom tag.
* -t and -o options can be omitted and defaults used if user wants.

6. Example input in terminal $python3 opml_convert_rss.py -i ~/Downloads/te -o test -t testtag

output:

![SS](https://raw.githubusercontent.com/gavinlyonsrepo/opml_convert_RSS/master/screenshots/opml.png)

7. Copy the output file into RSS reader setup files(eg newsboat)
 
 
**Arguments**

usage: opml_convert_rss.py [-h] [-v] [-i INFILE] [-o OUTFILE] [-t TAGNAME]

URL help at: https://github.com/gavinlyonsrepo/opml_convert_RSS

optional arguments:

* -h, --help  show this help message and exit
* -v          Print version and quit
* -i INFILE   input filename and/or full path
* -o OUTFILE  output filename and/or full path, default ./outfile.txt
* -t TAGNAME  tagname, default = youtube

