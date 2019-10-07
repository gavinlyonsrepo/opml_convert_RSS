Overview
--------------------------------------------
* Name: opml_convert_RSS
* Description: Command line python utility , converts opml(xml) to RSS.
* Author: Gavin Lyons.


Description
---------

Command line python utility, 
Converts the opml(Xml) file of a youtube user subscriptions provided by youtube, 
into a text file which can added to RSS reader setup file 
file, like newsboat for example. Thus converting your youtube subscriptions,
into a group of tagged RSS feeds.

**Input:**

opml(xml) file provided by user on comand prompt using -f option.

**Output:**

Output.txt file in following format:

[url] ~"[video_title]" [tag]

https://www.youtube.com/feeds/videos.xml?channel_id=UCI999ua  "~Python Training by Bader"  youtube

Where tag = youtube

usage
--------

1. Download the python program, youtube_sub_convert.py.
2. In a web browser navigate to subscription manager page of youtube.
https://www.youtube.com/subscription_manager
3. At bottom of page click on "Export to RSS readers -- Export subscriptions".
4. This subscription_manager file will be downloaded into an opml(xml) file.
5. Run program in terminal. $ python3 youtube_sub_convert.py -f opmlfilename
6. A file called output.txt will be created at path of program. 
7. Copy this into RSS reader setup files.
 
 
Arguments
-------------

usage: youtube_sub_convert.py [-h] [-v] [-f FILE]

URL help at: 

https://github.com/gavinlyonsrepo/opml_convert_RSS

optional arguments:

1.  -h, --help  show  help message and exit
2.  -v          Print version and quit
3.   -f FILE     inputfile xml file , fullpath and/or filename


Exmaples files
--------------------
Example input xml and output txt files are available in Documents folder

Copyright
-------------------

Copyright (C) 2019 Gavin Lyons, This program is free software; 
you can redistribute it and/or modify it under the terms of the 
GNU General Public license published by the Free Software Foundation.
