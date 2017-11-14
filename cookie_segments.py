#!/usr/bin/python3

import re
import sys

# TODO: make decision re: cmd line/validation

cookie_jar = list()
segment_set = list()

# 
cookie_re = re.compile('([0-9a-f]{32})')
segment_re = re.compile('[A-Z][0-9]{5}_[0-9]{5}')

# dict with cookies as keys
eval_cookie_map = dict()
eval_segment_map = dict()

# build two dicts from evaluation
with open("eval.log") as f:
    for line in f:
        cookie = cookie_re.search(line)
        segment_set = segment_re.findall(line)
        if cookie != None:
            cookie = cookie.group()
            eval_cookie_map.update({cookie: segment_set})
            for seg in segment_set:
                if seg in eval_segment_map:
                    eval_segment_map[seg].append(cookie)
                else:
                    cookie_jar.append(cookie)
                    eval_segment_map.update({seg: list(cookie_jar)})
                    cookie_jar.clear()

# for k in eval_segment_map:
#     print(k)
#     for v in eval_segment_map[k]:
#         print(v)
# print(len(eval_cookie_map))

# print(eval_segment_map)
# dict with cookies as keys
base_cookie_map = dict()
base_segment_map = dict()

# build two dicts from baseline
with open("base.log") as f:
    for line in f:
        cookie = cookie_re.search(line)
        segment_set = segment_re.findall(line)
        if cookie != None:
            cookie = cookie.group()
            base_cookie_map.update({cookie: segment_set})
            for seg in segment_set:
                if seg in base_segment_map:
                    base_segment_map[seg].append(cookie)
                else:
                    cookie_jar.append(cookie)
                    base_segment_map.update({seg: list(cookie_jar)})
                    cookie_jar.clear()

# for k, v in eval_segment_map.items():
#     print(k, v)

# print(len(eval_cookie_map))
# print(len(eval_segment_map.values()))
# count = sum(len(v) for v in eval_segment_map.values())
# print(count)
# print(len(base_cookie_map))
# print(len(base_segment_map.items()))
# print(len(base_segment_map))

# print("Segments with added cookies: %d / %d")
# print("%d\t%s\t%d\t%l")
templist = set()
diffset = list()
seg_list = list()
cookie_list = list()
maybe_dict = dict()

for seg in eval_segment_map.keys():
    templist = set(eval_segment_map[seg]).difference(set(base_segment_map[seg]))
    print(templist)
    if len(templist) > 0:
        maybe_dict.update(seg, templist)

print(maybe_dict)
