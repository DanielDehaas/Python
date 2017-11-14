#!/usr/bin/python3

#!/usr/bin/python3

import re
import sys

# TODO: make decision re: cmd line/validation

# cookie_jar = list()
segment_set = list()

cookie_re = re.compile('([0-9a-f]{32})')
segment_re = re.compile('[A-Z][0-9]{5}_[0-9]{5}')

# dict with cookies as keys
eval_cookie_map = dict()
eval_segment_map = dict()

with open("eval.log") as f:
    for line in f:
        cookie_jar = cookie_re.search(line)
        segment_set = segment_re.findall(line)
        if cookie_jar != None:
            eval_cookie_map.update({cookie_jar.groups(): segment_set})
            for seg in segment_set:
                if seg in eval_segment_map:
                    eval_segment_map[seg].append(cookie_jar.groups())
                else:
                    eval_segment_map.update({seg: list(cookie_jar.groups())})

# for k in eval_segment_map:
#     print(k)
#     for v in eval_segment_map[k]:
#         print(v)
# print(len(eval_cookie_map))

# dict with cookies as keys
base_cookie_map = dict()
base_segment_map = dict()


with open("base.log") as f:
    for line in f:
        cookie_jar = cookie_re.search(line)
        segment_set = segment_re.findall(line)
        if cookie_jar != None:
            base_cookie_map.update({cookie_jar.groups(): segment_set})
            for seg in segment_set:
                if seg in base_segment_map:
                    base_segment_map[seg].append(cookie_jar.groups())
                else:
                    base_segment_map.update({seg: list(cookie_jar.groups())})

# dict with segments as keys
# eval_segment_map = dict()


# for zed in dum_list:
#     print(zed)
# invert dict
# temp = set(a for b in eval_cookie_map.values() for a in b)
# eval_segment_map = dict((new_key, [key for key, 
# value in eval_cookie_map.items() if new_key in temp]) for new_key in temp)
# print(eval_segment_map)

# for k in eval_cookie_map:
#     if eval_cookie_map.get(k) == None:
#         print("doodoo")
#     else:
#         print(eval_cookie_map.get(k))

# for k in eval_cookie_map:
#     for c in eval_cookie_map.get(k):
#         eval_segment_map.update({c, k})

# for k, v in eval_cookie_map.items():
#     for x in v.items():
#         eval_segment_map.update({x, k})


# for key in eval_cookie_map:
#     for value in eval_cookie_map[key]:
#         eval_segment_map[value] = key

# dict with segments as keys
# base_segment_map = dict()

# invert dict
# for key in base_cookie_map:
#     for value in base_cookie_map[key]:
#         base_segment_map[value] = key


# print(len(eval_cookie_map))
# print(len(eval_segment_map))
# print(len(base_cookie_map))
# print(len(base_segment_map))

# print(eval_cookie_map)
# print(eval_segment_map)

# for k in base_segment_map:
#     print(k + ':')
#     for v in enumerate(base_segment_map[k]):
#         print(v)


# print(base_segment_map)
# reusable dict to repopulate for each report
# results_map = dict()
# difference_map = dict()
# tempset = list()

# for segs in base_segment_map:
#     for cooks in base_segment_map.get(segs):    
#            print(cooks) 


# print(sys.getsizeof(eval_cookie_map))
# print(sys.getsizeof(base_segment_map))
