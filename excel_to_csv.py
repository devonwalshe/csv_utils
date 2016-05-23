##Converts excel to python
import os 
import xlrd
import csv
import re
from xlrd import XLRDError
from zipfile import BadZipfile

### 1. set base directory

base_dir=('/Users/azymuth/Documents/Life/Active/Projects/Future_City_Glasgow/References/HackDays/3_Health/Collections')
output_dir = ('/Users/azymuth/Documents/Life/Active/Projects/Future_City_Glasgow/References/HackDays/3_Health/CSV_Files/')

# regular expression to extract package_title from path

def get_path(file_path):
  regex = re.compile(".*/([^/#]*)(#.*|$)")
  r = regex.match(file_path)
  filename = r.groups()[0]
  return filename
  

def excel_to_csv(input_file, package_dir):

    wb = xlrd.open_workbook(input_file)
    sh = wb.sheet_by_name(wb.sheet_names()[0])
    
    filename = os.path.splitext(get_path(input_file))[0]

    csv_file = open(package_dir+filename+".csv", 'wb')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()   
  
    
  
### 3. recursively search through folders collecting .xls or .xlsx files

all_files = []


for root, subfolders, files in os.walk(base_dir):
   all_files.append({'root':root, 'files':files})


def folders_to_paths(all_folders):
  all_folder_paths = []
  for pair in all_folders:
    for subfolder in pair["folders"]:
      all_folder_paths.append(pair["root"]+"/"+subfolder)
      
  return all_folder_paths


    

  
def no_csv_find(files):
  no_csv = []  
  
  for items in all_files:
    for filename in items["files"]:
      if not any(os.path.splitext(filename)[0]+".csv" in s for s in items["files"]):
        if os.path.splitext(filename)[1] == ".xls":
          no_csv.append({'root':items['root']+"/", 'path':items['root']+"/"+filename})

        elif os.path.splitext(filename)[1] == ".xlsx":
          no_csv.append({'root':items['root']+"/", 'path':items['root']+"/"+filename}) 
  
  return no_csv

### 4. For each file, convert to .csv if there isn't already one and put it in the output folder.


def convert_all(no_csv):
  
  for files in no_csv:
    try:
      
      
      #Only use if outputting to a different folder
      
      # package = get_path(file_pair["root"])
      # package_dir = output_dir + package + "/"
      # if not os.path.exists(package_dir):
      #   os.makedirs(package_dir)     
      print "csv'ing %s" % files['root']
      excel_to_csv(files['path'], files['root'])
      
    except (TypeError, XLRDError, UnicodeEncodeError, BadZipfile) as e:
      print e
      print files
      pass          

### 5. Run it 

no_csv = no_csv_find(all_files)

convert_all(no_csv)