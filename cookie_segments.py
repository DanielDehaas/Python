#!/usr/bin/python3

import collections
import re
import sys
import time

if len(sys.argv) != 3:
    base =  "evaluator-integration-baseline.log"
    eval =  "evaluator-integration.log"
else:
    base = argv[1]
    eval = argv[2]

start = time.time()

base_cookie_map = collections.defaultdict(list)
base_segment_map = collections.defaultdict(list)

with open(base, "r") as f:
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

with open(eval, "r") as f:
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
seg_list = list()
report_dict_plus = dict()
report_dict_minus = dict()

for seg in eval_segment_map.keys():
    templist = set(eval_segment_map[seg]).difference(set(base_segment_map[seg]))
    if len(templist) > 0:
        seg_list.append(seg)
        cookie_jar = list(templist)
        cookie_jar.sort()
        report_dict_plus.update({seg: cookie_jar})

seg_list.sort()
delta = len(report_dict_plus)
count = len(base_segment_map.keys())
print('Segments with added cookies: ', delta, '/', count)
counter = 0
for s in seg_list:
    print('%d\t%s\t%d\t%s' % (counter, s, len(report_dict_plus[s]), report_dict_plus[s]))
    counter += 1
print()

seg_list.clear()

for seg in base_segment_map.keys():
    if seg in eval_segment_map.keys():
        templist = set(base_segment_map[seg]).difference(set(eval_segment_map[seg]))
        if len(templist) > 0:
            seg_list.append(seg)
            cookie_jar = list(templist)
            cookie_jar.sort()
            report_dict_minus.update({seg: cookie_jar})
    elif seg not in eval_segment_map.keys():
        templist = set(base_segment_map[seg])
        cookie_jar = list(templist)
        seg_list.append(seg)
        cookie_jar.sort()
        report_dict_minus.update({seg: cookie_jar})

seg_list.sort()
delta = len(report_dict_minus)
count = len(base_segment_map.keys())
print('Segments with missing cookies: ', delta, '/', count)
counter = 0
for s in seg_list:
    print('%d\t%s\t%d\t%s' % (counter, s, len(report_dict_minus[s]), report_dict_minus[s]))
    counter += 1
print()

eval_segment_map.clear()
base_segment_map.clear()
report_dict_plus.clear()
report_dict_minus.clear()
cookie_jar.clear()

for c in eval_cookie_map:
    templist = set(eval_cookie_map[c]).difference(set(base_cookie_map[c]))
    if len(templist) > 0:
        cookie_jar.append(c)
        seg_list = list(templist)
        seg_list.sort()
        report_dict_plus.update({c: seg_list})

cookie_jar.sort()
delta = len(report_dict_plus)
count = len(base_cookie_map.keys())
print('Cookies in extra segments: ', delta, '/', count)
counter = 0
for c in cookie_jar:
    print('%d\t%s\t%d\t%s' % (counter, c, len(report_dict_plus[c]), report_dict_plus[c]))
    counter += 1
print()

cookie_jar.clear()

for c in base_cookie_map:
    if c in eval_cookie_map.keys():
        templist = set(base_cookie_map[c]).difference(set(eval_cookie_map[c]))
        if len(templist) > 0:
            cookie_jar.append(c)
            seg_list = list(templist)
            seg_list.sort()
            report_dict_minus.update({c: seg_list})
    elif seg not in eval_cookie_map.keys():
        templist = set(base_cookie_map[c])
        seg_list = list(templist)
        seg_list.sort()
        cookie_jar.append(c)
        report_dict_minus.update({c: seg_list})

cookie_jar.sort()
delta = len(report_dict_minus)
count = len(base_cookie_map.keys())

print('Cookies omitted from segments: ', delta, '/', count)
counter = 0
for c in cookie_jar:
    print('%d\t%s\t%d\t%s' % (counter, c, len(report_dict_minus[c]), report_dict_minus[c]))
    counter += 1
print()


end = time.time()
print(end - start)
