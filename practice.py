import os
cwd = os.getcwd()
print("current working directory: {0}".format(cwd))
path = "c:/Users/kris/Desktop/Class Folder/Module_3/Election_Analysis/Resources/election_results.csv"
os.chdir(path)
new_wd = os.getcwd()
print ("Directory changed successfully %s" % new_wd)
path = "c:/Users/kris/Desktop/Class Folder/Module_3/Election_Analysis/Resources"
os.chdir(path)