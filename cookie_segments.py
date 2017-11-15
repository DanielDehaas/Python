#!/usr/bin/python3

import re
import sys
import time

# TODO: make decision re: cmd line/validation

start = time.time()

cookie_jar = list()
segment_set = list()

# 
cookie_re = re.compile('([0-9a-f]{32})')
segment_re = re.compile('[A-Z][0-9]{5}_[0-9]{5}')

# dict with cookies as keys
eval_cookie_map = dict()
eval_segment_map = dict()

# build two dicts from evaluation
with open("evaluator-integration.log") as f:
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

base_cookie_map = dict()
base_segment_map = dict()

# build two dicts from baseline
with open("evaluator-integration-baseline.log") as f:
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

templist = set()
seg_list = list()
cookie_list = list()
maybe_dict = dict()
segment_set = set()
# segment_set = set(list(eval_segment_map.keys()) + list(base_segment_map.keys()))

for s in eval_segment_map.keys():
    segment_set.update(s)

for s in base_segment_map.keys():
    segment_set.update(s)

seg_list_eval = eval_segment_map.keys()
seg_list_base = base_segment_map.keys()
print(len(segment_set))
print(len(eval_segment_map.keys()))
print(len(base_segment_map.keys()))
# count = sum(len(v) for v in base_cookie_map.values())
# print('muthafucking: ', count)
# for seg in segment_set

for seg in eval_segment_map.keys():
    templist = set(eval_segment_map[seg]).difference(set(base_segment_map[seg]))
    # seg_list.append(seg)
    if len(templist) > 0:
        seg_list.append(seg)
        cookie_jar = list(templist)
        maybe_dict.update({seg: cookie_jar})

seg_list.sort()
delta = len(maybe_dict)
count = len(base_segment_map.keys())
print('Segments with added cookies: ', delta, '/', count)
# # print(maybe_dict)
seg_list.clear()
maybe_dict.clear()
cookie_jar.clear()

for seg in base_segment_map.keys():
    templist = set(base_segment_map[seg]).difference(set(eval_segment_map[seg]))
    # seg_list.append(seg)
    if len(templist) > 0:
        seg_list.append(seg)
        cookie_jar = list(templist)
        maybe_dict.update({seg: cookie_jar})

# for seg in base_segment_map.keys():
#     if seg in seg_list_eval:
#         templist = set(base_segment_map[seg].difference(set(eval_segment_map[seg]))
#         seg_list.append(seg)
#         if len(templist) > 0:
#             cookie_jar = list(templist)
#             maybe_dict.update({seg: cookie_jar})
#     else:
#         # templist = set(eval_segment_map.get(seg))
#         seg_list.append(seg)
#         cookie_jar = eval_segment_map[seg]
#         maybe_dict.update({seg: cookie_jar})


seg_list.sort()
delta = len(seg_list)
cookie_list.clear()
count = len(base_segment_map.keys())
# count = len(maybe_dict.values())
print('Segments with missing cookies: ', delta, '/', count)


# for seg in eval_segment_map.keys():
#     templist  = set(base_segment_map.get(seg)).difference(set(eval_segment_map.get(seg)))
#     # print(templist(type))
#     # print(type(templist))
#     seg_list.append(seg)
#     if len(templist) > 0:
#         cookie_list = list(templist)
#         maybe_dict.update({seg: cookie_list})





# for seg in eval_segment_map.keys():
#     templist = set(eval_segment_map[seg]).difference(set(base_segment_map[seg]))
#     # print(templist)
#     seg_list.append(seg)
#     if len(templist) > 0:
#         cookie_list = list(templist)
#         maybe_dict.update({seg: cookie_list})

# seg_list.sort()
# delta = len(maybe_dict)
# # count = sum(len(v) for v in maybe_dict.values())
# count = len(base_segment_map.items())
# print('Segments with added cookies: ', delta, '/', count)

# # print(len(maybe_dict.items()))
# # count = 0
# # for j in maybe_dict.items():
# #     count += len(maybe_dict[j])
# # print('motherfuckin: ', count)

# # print(count)
# # print(maybe_dict)
# maybe_dict.clear()
# seg_list.clear()
# # # print(maybe_dict)

# for seg in eval_segment_map.keys():
#     templist  = set(base_segment_map.get(seg)).difference(set(eval_segment_map.get(seg)))
#     # print(templist(type))
#     # print(type(templist))
#     seg_list.append(seg)
#     if len(templist) > 0:
#         cookie_list = list(templist)
#         maybe_dict.update({seg: cookie_list})


# seg_list.sort()
# delta = len(maybe_dict)
# cookie_list.clear()
# print('Segments with added cookies: ', delta, '/', count)
# # print(maybe_dict)

# for c in eval_cookie_map.key():
#     templist = set(eval_cookie_map[c]).difference(set(base_cookie_map[c]))
#     cookie_list.append(c)
#     if len(templist) > 0:
#         seg_list = list(templist)
#         maybe_dict.update({c: seg_list})

end = time.time()
print(end - start)
