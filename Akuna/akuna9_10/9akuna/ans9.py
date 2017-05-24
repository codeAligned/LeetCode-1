import collections
def parse_log_stats(log_list):
	job_info = collections.defaultdict(dict)
	user_errors = collections.defaultdict(list)
	job_errors = {}
	curr_work = ""
	for log in log_list:
		log_data = log.split()
		type_ = log_data[3]
		type_ = type_[1:len(type_)-2]
		user = log_data[2]
		user = user[1:len(user)-1]
		
		if type_ == 'DEBUG' and log_data[4] == 'Starting':
			curr_work = log_data[5]
			if curr_work not in job_errors:
				job_errors[curr_work] = []
			#print curr_work
			if log_data[5] not in job_info:
				job_info[log_data[5]] = {"duration":0,"count" : 1}
			else:
				job_info[log_data[5]]["count"] += 1
		#print " "
		#print user,curr_work,type_
		#print " "
		if type_ == 'INFO':
			#print curr_work,log
			job_info[curr_work]["duration"] += int(log_data[-2])
			
		elif type_ == 'ERROR':
			error_msg = " ".join(log_data[4:])
			#print error_msg
			user_errors[user].append(error_msg)
			job_errors[curr_work].append(error_msg)
			
	job_avg = {}
	for job in job_info:
		avg = job_info[job]["duration"]*1.0/job_info[job]["count"]
		job_avg[job] = avg
		
		
	return {"job_avg":job_avg, "user_errors":user_errors, "job_errors":job_errors}
	
	
log_list = []
with open("input003.txt") as f:
	log_list=f.readlines()


res = parse_log_stats(log_list)
for r in res:
	if r=="job_avg": print r, res[r]
	else:
		print r
		for rr in res[r]:
			print rr,res[r][rr]
