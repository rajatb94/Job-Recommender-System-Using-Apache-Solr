from js import *
from time import sleep
import MySQLdb
import pycurl
import re
import requests
import urllib
requests.head('http://192.168.1.71:8983/solr/companies/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true')
db = MySQLdb.connect(passwd="zettamine",db="job_details",host="192.168.1.71",port=3306,user="root")
cur = db.cursor() 
sql = "SELECT compName, keyword, description FROM job_postings"
cur.execute(sql)
results=cur.fetchall()
headers = {'content-type': 'text/xml; charset=utf-8'}
url='http://192.168.1.71:8983/solr/companies/update'
jobseeker=JobSeeker()
k=0

def req():
	try:
		response = requests.post(url, data=dt, headers=headers)
	except:
		sleep(1)
		req()
for row in results:
	k=k+1
	jobseeker.setKeySkills2(row[0])
	r1=jobseeker.KeySkills
	jobseeker.setKeySkills(row[1])
	r2=jobseeker.KeySkills
	jobseeker.setKeySkills(row[2])
	r3=jobseeker.KeySkills
	dt='<add><doc><field name="compname">' + r1 + '</field><field name="keyword">' + r2 + '</field><field name="description">' + r3 + '</field></doc></add>'
	req()
	print k

	 

requests.head('http://192.168.1.71:8983/solr/companies/update?commit=true')
print "Done"
