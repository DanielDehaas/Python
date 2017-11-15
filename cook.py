#!/usr/bin/python3

import collections
import re
import sys
import time

start = time.time()

base_cookie_map = collections.defaultdict(list)
base_segment_map = collections.defaultdict(list)

with open("evaluator-integration-baseline.log", "r") as f:
    for line in f:
        m = re.match("^.*evaluated: ([0-9a-f]*) ==> \\[([A-Z].*)?\\]", line)
        if m:
            cookie, segments = m.group(1), m.group(2)
            if not segments:
                base_cookie_map[cookie] = []
            else:
                for seg in segments.split(", "):
                    base_segment_map[seg].append(cookie)
                    base_cookie_map[cookie].append(seg)

eval_cookie_map = collections.defaultdict(list)
eval_segment_map = collections.defaultdict(list)

with open("evaluator-integration.log", "r") as f:
    for line in f:
        m = re.match("^.*evaluated: ([0-9a-f]*) ==> \\[([A-Z].*)?\\]", line)
        if m:
            cookie, segments = m.group(1), m.group(2)
            if not segments:
                eval_cookie_map[cookie] = []
            else:
                for seg in segments.split(", "):
                    eval_segment_map[seg].append(cookie)
                    eval_cookie_map[cookie].append(seg)

# print(len(base_cookie_map.keys()))
# print(len(eval_cookie_map.keys()))
# print(len(base_segment_map.keys()))
# print(len(eval_segment_map.keys()))

seg_list_eval = eval_segment_map.keys()
seg_list_base = base_segment_map.keys()
seg_set = set(list(seg_list_base) + list(seg_list_eval))

report_dict_plus = dict()
report_dict_minus = dict()

for seg in eval_segment_map.keys():
    templist = set(eval_segment_map[seg]).difference(set(base_segment_map[seg]))
        # seg_list.append(seg)
    if len(templist) > 0:
        seg_list.append(seg)
        cookie_jar = list(templist)
        report_dict_plus.update({seg: cookie_jar})

seg_list.sort()
delta = len(report_dict_plus)
count = len(base_segment_map.keys())
print('Segments with added cookies: ', delta, '/', count)



end = time.time()
print(end - start)
