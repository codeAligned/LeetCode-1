import sys

_logs = []
for line in sys.stdin.readlines():
	_logs.append(line.strip())
	
res = parse_log_stats(_logs)

javg = ""
jerrors = ""
uerrors = ""

avgs = sorted(res['job_avg'].keys())
for k in avgs:
	v = res["job_avg"][k]
	javg += " ({},{}) ".format(k,v)
	
errors = sorted(res['job_errors'].keys())
for k in errors:
	v = res["job_errors"][k]
	jerros += " {} [{}]".format(k,", ".join(sorted(v)))
	
users = sorted(res["user_errors"].keys())
for k in users:
	v = res[]
