#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

os.system('clear')
print "BPM CALCULATOR\n"
print "Press Ctrl + C to exit."
print "Press the enter key to measure the tempo."
total_beats = 0
total_time = 0
last_time = None
while True:
    try:
        raw_input()
    except KeyboardInterrupt:
        exit(0)
    os.system('clear')
    print "BPM CALCULATOR\n"
    total_beats += 1
    current_time = time.time()
    if not (last_time is None):
        time_delta = current_time - last_time
        total_time += time_delta
    if total_time > 0:
        print "%.2f BPM (based on %d beats)\n" % ((total_beats - 1) / total_time * 60, total_beats)
    last_time = current_time
    print "Press Ctrl + C to exit."



