from js import *
import solr
import ntpath
import urllib

# ESTABLISHING CONNECTION TO MY SQL DATABASE
# ************************                      
jb=JobSeeker()
color = ["#60AFFE", "#ffca3a", "#a8a4a4", "#66cdaa", "#ff4444","#ffc3a0","#daa536","#e61f44","#e7846f","#cdb0f2","#509ddd","#5ca36a","#e65d1f"];
def get_rec(skills, type):

  if type=="companies":

    skillsRefined=None

    jb.setKeySkills(skills)
    skills=jb.KeySkills

  # SETTING SOLR CONNECTION
    s = solr.SolrConnection('http://192.168.1.71:8983/solr/companies')
  # ***********************
    st=""

  # EXECUTING SOLR QUERY FOR EVERY OBJECT (PROFILE OF USER) OF CLASS JobSeeker

    if len(skills)>5000:
      skillsRefined=skills[:(5000-len(skills))]
    else:
      skillsRefined=skills
    skref=skillsRefined.replace("*","").split(" ")
  #print "SKILLS HAVE: " + skillsRefined
  #print "RECOMMENDATIONS: "

    ar=[]
    json='{"dataObj":['
    for i in range(0,len(skref)):
      if skref[i]!="c++":
        res=s.query("keyword:*" + skref[i] + "* & description:*" + skref[i] + "*")
      else:
        res=s.query("keyword:c++ & description:c++")
      json=json + '{"value":"' + str(res.numFound) +'",' + '"color":"' + color[i] + '",' + '"skill":"' + skref[i] + '"},'

  # SOLR QUERY EXECUTION
    sr=skillsRefined.replace("*c*","c").replace("*c++*","c++")
    print sr
    response=s.query("keyword:(" + sr + ") & description:(" + sr + ")")
    if len(skref)>1:
      print skref
      json=json + '{"value":"' + str(response.numFound) +'",' + '"color":"#FF5A5E",' + '"skill":"' + skillsRefined.replace("*","").replace(" ",", ") + '"}'
  # ********************
    json=json + ']}'
    j=1
  # SHOWING THE RECOMMENDATIONS (as file path for the time being)
    for hit in response.results:
      st = st + hit['compname'][0].title() + " - KeyWords: <span style='color: white'>" + hit['keyword'][0] + "</span><br/>"
      j=j+1
    st=st + json
    return(st)


  else:

    skillsRefined=None

    jb.setKeySkills(skills)
    skills=jb.KeySkills

  # SETTING SOLR CONNECTION
    s = solr.SolrConnection('http://192.168.1.71:8983/solr/jobseekers')
  # ***********************
    st=""

  # EXECUTING SOLR QUERY FOR EVERY OBJECT (PROFILE OF USER) OF CLASS JobSeeker

    if len(skills)>5000:
      skillsRefined=skills[:(5000-len(skills))]
    else:
      skillsRefined=skills
    skref=skillsRefined.replace("*","").split(" ")
  #print "SKILLS HAVE: " + skillsRefined
  #print "RECOMMENDATIONS: "

    ar=[]
    json='{"dataObj":['
    for i in range(0,len(skref)):
      if skref[i]!="c++":
        res=s.query("key_skill:*" + skref[i] + "* & resume_title:*" + skref[i] + "*")
      else:
        res=s.query("key_skill:c++ & resume_title:c++")
      json=json + '{"value":"' + str(res.numFound) +'",' + '"color":"' + color[i] + '",' + '"skill":"' + skref[i] + '"},'


    sr=skillsRefined.replace("*c*","c").replace("*c++*","c++")



  # SOLR QUERY EXECUTION
    response=s.query("key_skill:(" + sr + ") & resume_title:(" + sr + ")")
    if len(skref)>1:
      print skref
      json=json + '{"value":"' + str(response.numFound) +'",' + '"color":"#FF5A5E",' + '"skill":"' + skillsRefined.replace("*","").replace(" ",", ") + '"}'
  # ********************
    json=json + ']}'
    j=1
  # SHOWING THE RECOMMENDATIONS (as file path for the time being)
    for hit in response.results:
      st = st + hit['name'][0].title() + " - SKILLS HAVE: <span style='color: white'>" + hit['key_skill'][0] + "</span><br/>"
      j=j+1
    st=st+json
    return(st)

  # ***************************
    
  #print "\n"
# ************************************************************************** 