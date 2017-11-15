#!/usr/bin/python3

eval_cookie_map = collections.defaultdict(list)
base_cookie_map = collections.defaultdict(list)
eval_segment_map = collections.defaultdict(list)
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
                    base_cookie_map[cookie].append(segment)
                    
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
                    eval_cookie_map[cookie].append(segment)

print(len(base_cookie_map.keys()))
print(len(eval_cookie_map.keys()))
print(len(base_segment_map.keys()))
print(len(eval)segment_map.keys()))
