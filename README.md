Description
---------

Command line python utility 
Converts the opml(Xml) file of a youtube user subscriptions provided by youtube, 
into a text file which can added to rss feeder setup. 
file like newsboat for example. Thus converting your youtube subscriptions,
into a group of tagged RSS feeds.

**Input:**

opml(xml) file provided by user on comand prompt uisng -f option

**Output:**

Output.txt file in following format:

[url] ~"[video_title]" [tag]

https://www.youtube.com/feeds/videos.xml?channel_id=UCI999ua  "~Python Training byBader"  youtube

Where tag = youtube

usage
--------

1. Download the python program, youtube_sub_convert.py.
2. In a web browser navigate to subscription manager page of youtube.
https://www.youtube.com/subscription_manager
3. At bottom of page click on "Export to RSS readers Export subscriptions".
4. This subscription_manager file will be downloaded into an opml(xml) file.
5. Run program in terminal. $ python3 youtube_sub_convert.py -f opmlfilename
6. A file called output.txt will be created at path of program. 
7. Copy this into RSS reader setup files.
 
 
Arguments
-------------
usage: youtube_sub_convert.py [-h] [-v] [-f FILE]

URL help at: https://github.com/gavinlyonsrepo/miscellaneous/tree/master/pytho
n/youtube_sub_convert

optional arguments:
  -h, --help  show this help message and exit
  -v          Print version and quit
  -f FILE     inputfile, + filename

