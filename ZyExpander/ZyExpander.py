#!/usr/local/bin/python3
# ZyExpander: A Nested ZipFile Expander For ZyBooks.
# By: Michael Green
# Expands and organizes by student nested zip files that ZyBook's grading
# system uses for some reason. 
import zipfile
import os
import argparse

# Goes through our argument list and pulls out the files to process along with any
# optional inputs specified.
def get_args():
	# argparse makes our life easier by looking for flags and creating descriptions
	# for the help flag automatically.
	parser = argparse.ArgumentParser(description='Takes input zipfiles and expands them.')
	parser.add_argument('zips', nargs='+',help="zipfiles you want to process")
	parser.add_argument('-o',default=".",help="option to specify an output directory (default is current directory)")
	parser.add_argument('-s', default="/Students/",help="option to specify the name of the students directory (default is Students)")
	parser.add_argument('-p',default="/Processed/",help="option to specify where to place processed zip files (default is Processed)")
	args = parser.parse_args()
	return [args.zips,args.o,args.o + args.s,args.o + args.p]

def check_path(path):
		if not os.path.exists(path):
			print("Creating path: " + path + "...")
			os.mkdir(path)

# Verifying that input arguments supplied are existing zip files
def type_check(args):
	try:
		for arg in args:
			if ".zip" not in arg[-4:] and not os.path.isfile(arg):
				raise ValueError(arg)
	except ValueError as error:
		print("Either the argument \"" + str(error.args[0]) + "\" isn't a zip file or it's not a file at all! Or maybe something else went horribly wrong....")



def expand(zip,output_paths):
	lab = zipfile.ZipFile( open(zip, "rb") )	
	for student in lab.namelist():
		#Replace of leading zip path with output dir and extra information on file names
		student_dir = output_paths[0] + student.split("-")[0].lower() + "/"
		check_path(student_dir)
		# We have to extract the nested zip files, because you can't
		# extract nested zips' contgents
		lab.extract(student,student_dir)
		# Now we can extract the nested zip files' contents
		student_files = zipfile.ZipFile( open(student_dir + student, "rb") )
		for student_file in student_files.namelist():
			student_files.extract(student_file,student_dir)
		# Removing the extra zip directory we had to extract
		os.remove(student_dir + student)
		student_files.close()
	lab.close()
	# Finishing flag for individual zip files
	print("Processed: " + zip)
	#Moving processed file into appropriate directory
	os.rename(zip, output_paths[1] + zip)

def init():
	args = get_args()
	type_check(args[0])
	for path in args[1:]:
		check_path(path)
	for zip in args[0]:
		expand(zip,args[2:])
		print("Extracted: " + zip )


init()

