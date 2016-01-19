#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright 2015-2016 Richard Huang <rickypc@users.noreply.github.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
IMAP Library - a IMAP email testing library.
"""

from os.path import split
from re import sub
import sys


def main(argv):
    """Adds analytics code into auto generated documentation."""
    try:
        path = argv[0]
    except IndexError:
        print("analytics.py <file_path>")
        sys.exit(1)

    with open(path) as reader:
        content = reader.read()

    analytics = """<script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
    ga('create','UA-325170-8','auto');ga('set','checkProtocolTask',null);
    ga('send','pageview','%s');
</script>""" % (split(path)[1])

    content = sub(r"</body>", analytics + "\n</body>", content)

    with open(path, "w") as writer:
        writer.write(content)

if __name__ == "__main__":
    main(sys.argv[1:])
