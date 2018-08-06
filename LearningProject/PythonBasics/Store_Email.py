#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyperclip, re

emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4}
''', re.VERBOSE)
