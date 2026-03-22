#!/usr/bin/env python3
"""
Python script to convert YouTube OPML subscription file or JSON export
into a text file suitable for RSS readers (e.g. newsboat).

Author: Gavin Lyons
URL:    https://github.com/gavinlyonsrepo/opml_convert_RSS
"""
import os
import sys
import json
import argparse
from xml.etree import ElementTree

# metadata
__VERSION__ = "1.3"
__URL__ = "https://github.com/gavinlyonsrepo/opml_convert_RSS"


def msg(msg_type: str, text: str) -> None:
    """Print colored/bold messages (Linux only; falls back to plain text on Windows)"""
    if sys.platform == "win32":
        print(text)
        return

    colors = {
        "red": "\033[91m",
        "blue": "\033[94m",
        "bold": "\033[1m",
        "end": "\033[0m",
    }

    if msg_type == "line":
        print(colors["blue"] + "=" * 80 + colors["end"])
    elif msg_type == "red":
        print(colors["red"] + text + colors["end"])
    elif msg_type == "blue":
        print(colors["blue"] + text + colors["end"])
    elif msg_type == "bold":
        print(colors["bold"] + text + colors["end"])


def parse_opml(filename: str) -> tuple[list[str], list[str]]:
    """Parse .opml / .xml subscription file"""
    urls = []
    titles = []

    try:
        with open(filename, "rt", encoding="utf-8") as f:
            tree = ElementTree.parse(f)

        for node in tree.findall(".//outline"):
            url = node.attrib.get("xmlUrl")
            if url:
                urls.append(url)

        for node in tree.findall(".//outline"):
            text = node.attrib.get("text")
            if text:
                titles.append(text)

        # Remove first (usually folder/root) title
        if titles:
            titles.pop(0)

    except (FileNotFoundError, PermissionError, ElementTree.ParseError) as e:
        msg("red", f"Error reading/parsing OPML file '{filename}': {e}")
        sys.exit(1)

    return urls, titles


def parse_youtube_json(filename: str) -> tuple[list[str], list[str]]:
    """Parse YouTube takeout JSON subscriptions file"""
    urls = []
    titles = []

    try:
        with open(filename, "rt", encoding="utf-8") as f:
            data = json.load(f)

        for channel in data:
            try:
                channel_id = channel["snippet"]["resourceId"]["channelId"]
                title = channel["snippet"]["title"]

                urls.append(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
                titles.append(title)
            except KeyError:
                continue  # skip malformed entries

    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        msg("red", f"Error reading/parsing JSON file '{filename}': {e}")
        sys.exit(1)

    return urls, titles


def convert_subscriptions(infile: str, outfile: str, tag: str = "youtube") -> None:
    """Main conversion logic"""
    msg("bold", "Starting conversion...")

    ext = os.path.splitext(infile)[-1].lower()

    if ext in {".xml", ".opml"}:
        urls, titles = parse_opml(infile)
    elif ext == ".json":
        urls, titles = parse_youtube_json(infile)
    else:
        msg("red", f"Unsupported file extension: {ext}")
        sys.exit(1)

    if len(urls) != len(titles):
        msg("red", f"Warning: number of URLs ({len(urls)}) ≠ titles ({len(titles)})")

    try:
        with open(outfile, "wt", encoding="utf-8") as f:
            for url, title in zip(urls, titles):
                f.write(f'{url}  "~{title}"  {tag}\n')
    except (PermissionError, OSError) as e:
        msg("red", f"Failed to write output file '{outfile}': {e}")
        sys.exit(1)

    msg("bold", f"Done. Created {outfile!r} with {len(urls)} channels (tag: {tag})")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description=f"Convert YouTube subscriptions to newsboat RSS format.  See: {__URL__}"
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version and exit"
    )
    parser.add_argument(
        "-i", "--infile",
        help="Input file (.opml/.xml or .json)",
    )
    parser.add_argument(
        "-o", "--outfile",
        default="outfile.txt",
        help="Output file (default: ./outfile.txt)",
    )
    parser.add_argument(
        "-t", "--tag",
        default="youtube",
        help="Tag to append to each line (default: youtube)",
    )

    args = parser.parse_args()

    # Handle --version early, before requiring infile
    if args.version:
        msg("bold", f"Version: {__VERSION__}")
        msg("bold", "End")
        msg("line", "")
        sys.exit(0)

    # Now enforce that infile is provided (since version is already handled)
    if not args.infile:
        parser.error("the following arguments are required: -i/--infile")

    return args


def main() -> None:
    """Entry point"""
    msg("line", "")
    args = parse_arguments()

    if args.version:
        msg("bold", f"Version: {__VERSION__}")
        msg("bold", "End")
        msg("line", "")
        sys.exit(0)

    convert_subscriptions(args.infile, args.outfile, args.tag)

    msg("bold", "Finished.")
    msg("line", "")


if __name__ == "__main__":
    main()
