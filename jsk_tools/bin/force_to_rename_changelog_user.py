#!/usr/bin/env python
import sys
import StringIO
import re
# change contributors name generated by catkin_genarate_changelog
# usage:
# $ ./force_to_rename_changelog_user.py CHANGELOG.rt
# $ find . -name CHANGELOG.rst -exec rosrun jsk_tools force_to_rename_changelog_user.py {} \;

# sudo apt-get install python-progressbar
from progressbar import *

REPLACE_RULES={
    "k-okada": "Kei Okada",
    "garaemon": "Ryohei Ueda",
    "ueda": "Ryohei Ueda",
    "furushchev": "Yuki Furuta",
    "yoheikakiuchi": "Yohei Kakiuchi",
    "aginika": "Yuto Inagaki",
    "tarukosu": "Yusuke Furuta",
    "furuta": "Yusuke Furuta",
    "manabu": "Manabu Saito",
    "pr2 application": "JSK Lab member",
    "pr2admin": "JSK Lab member",
    "terasawa": "Ryo Terasawa",
    "yuohara": "Yu Ohara",
    "ohara": "Yu Ohara",
    "chen": "Xiangyu Chen",
    "cretaceous-creature": "Xiangyu Chen",
    "au@leus": "Chi Wun Au",
    "hrp2": "JSK Lab Member",
    "h-kamada": "Hitoshi Kamada",
    "s-noda": "Shintaro Noda",
    "iori": "Iori Kumagai",
    "wesleypchan": "Wesley Chan",
    "mmurooka": "Masaki Murooka",
    "masakimurooka": "Masaki Murooka",
    "iory": "Iori Yanokura"}

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def replaceContributors(line):
    match = re.match("\* Contributors: (.*)", line)
    if match:
        authors = [a.strip() for a in match.group(1).split(",")]
        replaced_authors = []
        for author in authors:
            org_author = author
            author = author.lower()
            if author in REPLACE_RULES:
                replaced_authors.append(REPLACE_RULES[author])
            else:
                replaced_authors.append(org_author)
        # remove duplicats, but not change orders
        return "* Contributors: " + ", ".join(remove_duplicates(replaced_authors))
    else:
        return line

def main(file_name):
    replaced_str = StringIO.StringIO()
    with open(file_name, "r") as f:
        widgets = ["%s: " % (file_name), Percentage(), Bar()]
        lines = f.readlines()
        pbar = ProgressBar(maxval=len(lines), widgets=widgets).start()
        for line in lines:
            if line.startswith("* Contributors:"):
                replaced_str.write(replaceContributors(line) + "\n")
            else:
                replaced_str.write(line)
            pbar.update(pbar.currval + 1)
        pbar.finish()
    with open(file_name, "w") as f:
        f.write(replaced_str.getvalue())

if __name__ == "__main__":
    main(sys.argv[1])
