#!/usr/bin/python3

import re
import sys

# TODO: make decision re: cmd line/validation

# eval = open("evaluator.log","r")
#baseline = open("baseline.log","r")

# new_dict = dict()
cookie_jar = set()
# set_of_segs = set()
segment_set = set()

cookie = re.compile('([0-9a-f]{32})')
segment = re.compile('[A-Z][0-9]{5}_[0-9]{5}')

with open("evaluator.log") as f:
    for line in f:
        # cookie_jar = cookie.findall(line)
        cookie_jar.update(cookie.findall(line))
        segment_set = segment.findall(line)
        # set_of_segs.update(segment.findall(line))
        print(segment_set)
        print('doodoo')
        
        # for word in cookie_jar:
        #     print(word)

# # f.close()
print(len(segment_set))
print(len(cookie_jar))
# with open("evaluator.log") as f:
#     for line in f:
#         segment_set = segment.findall(line)

# for word in cookie_jar:
#     print(word)

# for seg in set_of_segs:
#     print(seg)
# print(sorted(set_of_segs))
# #re.findall(cookie, eval.read())

# # for line in open("evaluator.log"):
# #     re.findall(cookie, line)
# f.close()
