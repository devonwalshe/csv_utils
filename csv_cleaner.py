#!/Users/azymuth/www/virtualenv/fest/bin/python
# -*- coding: utf-8 -*-
### Reads CSV file, forces Unicode encoding on all fields and outputs to file that is readable. 

### TODO - read encoding of infile, then send it to different functions depending on what it is. In all  (most?) cases strip out newlines

import sys
import os
import csv
import chardet

file_location = "/Users/azymuth/www/open_glasgow/csv_convert/Walters_list_Humiun_08_07b.csv"



# def get_dialect(csv_file):
#   f = open(csv_file, 'rU')
#   dialect = csv.Sniffer().sniff(f.read(1024))    
#   return dialect
# 
# csv_dialect = get_dialect(file_location)
# 
# def unicode_csv_reader(unicode_csv_data, dialect=csv_dialect, **kwargs):
#     # csv.py doesn't do Unicode; encode temporarily as UTF-8:
#     
#     csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
#                             dialect=dialect, **kwargs)
#     for row in csv_reader:
#         # decode UTF-8 back to Unicode, cell by cell:
#         yield [unicode(cell, 'utf-8') for cell in row]
# 
# def utf_8_encoder(unicode_csv_data):
#     for line in unicode_csv_data:   
#             yield line.encode('utf-8')   



## Read

def get_char_enc(in_file):
  rawdata = in_file.read()
  result = chardet.detect(rawdata)
  return result['encoding']


## Change


def encode_data_to_utf(data, char_encoding):
  csv_file = []
  for row in data:
    new_row = []
    for field in row:
      try:
        new_field = field.replace("\n", " ").decode(char_encoding).encode('utf-8')
        new_row.append(new_field)
      except (UnicodeDecodeError) as e:
        error_message = str(e)
        print e
      pass
    csv_file.append(new_row)
  return csv_file   


#### Write

def csv_writer(path, data):
 
  with open(path, 'wb') as out_file:
      writer = csv.writer(out_file)
      writer.writerows(data)
   

## Execute
     
# f = unicode_csv_reader(open(file_location, 'rU'))
f = open(file_location, 'rU')
char_encoding = get_char_enc(f)

csv_file = csv.reader(open(file_location, 'rU'))

encoded_data = encode_data_to_utf(csv_file, char_encoding)

csv_writer(file_location+"_converted.csv", encoded_data)      