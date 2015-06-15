import re

# CLASS TO STORE THE DATA OF USERS IN ITS OBJECTS
class JobSeeker:
  KeySkills = ""
  KeySkillsSP1 = ""
  KeySkillsSP2 = ""
  KeySkillsSP3 = ""
  KeySkillsSP4 = ""
  def getKeySkills(cls):
    return cls.KeySkills;

 # GETTING THE SKILL SET IN DESIRED FORMAT BY APPLYING REGEX
  def setKeySkills(cls, KeySkillsScrap):
    KeySkillsScrap=str(KeySkillsScrap)
    cls.KeySkillsSP1=KeySkillsScrap.replace("and", "").replace("AND", "").replace("or", "").replace("NOT", "")
    cls.KeySkillsSP2=re.sub("[^a-zA-Z0-9.++]", " " ,cls.KeySkillsSP1)
    cls.KeySkillsSP3=re.sub("\s+"," ",cls.KeySkillsSP2).strip()
    cls.KeySkillsSP4=re.sub(r"((\b\w+\++)|(\b\w+\b))",r"*\1*",cls.KeySkillsSP3)
    cls.KeySkills=cls.KeySkillsSP4
    return;
  # *********************************************************

# *************************************************