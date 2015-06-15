from js import *
import MySQLdb
import pycurl
from time import sleep
import re
import requests
import urllib
requests.head('http://192.168.1.71:8983/solr/jobseekers/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true')
db = MySQLdb.connect(passwd="zettamine",db="job_details",host="192.168.1.71",port=3306,user="root")
cur = db.cursor() 
sql = "SELECT js_id, name, resume_title, key_skill, exp_year, exp_current_co,preferred_location,gender FROM job_seekers"
cur.execute(sql)
results=cur.fetchall()
headers = {'content-type': 'text/xml; charset=utf-8'}
url='http://192.168.1.71:8983/solr/jobseekers/update'
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
	 r0=jobseeker.KeySkills
	 jobseeker.setKeySkills2(row[1])
	 r1=jobseeker.KeySkills
	 jobseeker.setKeySkills(row[2])
	 r2=jobseeker.KeySkills
	 jobseeker.setKeySkills(row[3])
	 r3=jobseeker.KeySkills
	 jobseeker.setKeySkills(row[4])
	 r4=jobseeker.KeySkills
	 jobseeker.setKeySkills(row[5])
	 r5=jobseeker.KeySkills
	 jobseeker.setKeySkills(row[6])
	 r6=jobseeker.KeySkills
	 jobseeker.setKeySkills(row[7])
	 r7=jobseeker.KeySkills
	 dt="""
	 <add><doc>

	 <field name="js_id">%s</field>
	 <field name="name">%s</field>
	 <field name="resume_title">%s</field>
	 <field name="key_skill">%s</field>
	 <field name="exp_year">%s</field>
	 <field name="exp_current_co">%s</field>
	 <field name="preferred_location">%s</field>
	 <field name="gender">%s</field>
	 </doc></add>
	 """ %(r0, r1, r2, r3, r4, r5, r6, r7)
	 print k
	 req()

requests.head('http://192.168.1.71:8983/solr/jobseekers/update?commit=true')
print "Done"
