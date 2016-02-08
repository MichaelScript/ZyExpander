# ZyExpander: A Nested ZipFile Expander For ZyBooks.
# By: Michael Green
# Expands and organizes by student nested zip files that ZyBook's grading
# system uses for some reason. 
import zipfile
import os
import sys
import argparse

# parsing cml arguments with argsparse
parser = argparse.ArgumentParser(description='Takes input zipfiles and expands them.')
parser.add_argument('zips', nargs='+',help="zipfiles you want to process")
parser.add_argument('-o',default="./",help="option to specify an output directory")
args = parser.parse_args()

students_dir = args.o + "/Students/"
processed_dir = args.o + "/Processed/"

if not os.path.exists(args.o):
	os.mkdir(args.o)
if not os.path.exists(students_dir):
	os.mkdir(students_dir)
if not os.path.exists(processed_dir):
	os.mkdir(processed_dir)
# Grabbing all the files, ignoring directories outright
for file in filter(os.path.isfile,args.zips):
	# Getting files that end in .zip
	if ".zip" in file[-4:]:
		assignment = zipfile.ZipFile( open(file, "rb") )
		for student in assignment.namelist():
			# Create student directory (based on student's name) if it doesn't exist already
			student_dir = students_dir + student.split("-")[0].lower() + "/"
			if not os.path.exists(student_dir):
				os.mkdir(student_dir)
			# We have to extract the nested zip files, because you can't
			# extract nested zips' contgents
			assignment.extract(student,student_dir)
			# Now we can extract the nested zip files' contents
			student_files = zipfile.ZipFile( open(student_dir + student, "rb") )
			for student_file in student_files.namelist():
				student_files.extract(student_file,student_dir)
			# Removing the nested ZipFile we had to extract
			os.remove(student_dir + student)
			student_files.close()
		assignment.close()
		# Finishing flag for individual zip files & saving backups of zipfiles in processed.
		print("Processed: " + file)
		os.rename(file, processed_dir + file)
print("ZyExpander Finished.")


