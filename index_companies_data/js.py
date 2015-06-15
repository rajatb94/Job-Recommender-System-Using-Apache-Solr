import re

# CLASS TO STORE THE DATA OF USERS IN ITS OBJECTS
class JobSeeker:
  KeySkills = ""
  KeySkillsSP1 = ""
  KeySkillsSP2 = ""


  def getKeySkills(cls):
    return cls.KeySkills;

 # GETTING THE SKILL SET IN DESIRED FORMAT BY APPLYING REGEX
  def setKeySkills(cls, KeySkillsScrap):
    KeySkillsScrap=str(KeySkillsScrap)
    cls.KeySkillsSP1=KeySkillsScrap.replace("and", "").replace("AND", "").replace("or", "").replace("NOT", "")
    cls.KeySkillsSP2=re.sub("[^a-zA-Z0-9+]", " " ,cls.KeySkillsSP1)
    cls.KeySkills=cls.KeySkillsSP2
    return;
   # GETTING THE SKILL SET IN DESIRED FORMAT BY APPLYING REGEX
  def setKeySkills2(cls, KeySkillsScrap):
    KeySkillsScrap=str(KeySkillsScrap)
    cls.KeySkillsSP2=re.sub("[^a-zA-Z0-9+]", " " ,KeySkillsScrap).replace("#","\#")
    cls.KeySkills=cls.KeySkillsSP2
    return;
  # *********************************************************
# *************************************************