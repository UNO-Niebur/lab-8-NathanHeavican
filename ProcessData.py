#ProcessData.py
#Name: Nathan heavican
#Date: 3/26/26
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    
    student_id = makeID(data[0], data[1], data[3])
    
    major = " ".join(data[6:])
    student_major_year = makeMajorYear(major, data[5])
    
    outFile.write(data[1] + "," + data[0] + "," + student_id + "," + student_major_year + "\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  """Creates a user ID from first initial, last name, and last 3 digits of ID."""
  first = first.lower()
  last = last.lower()
  while len(last) < 5:
    last = last + "x"
  idLen = len(idNum)
  id = first[0] + last + idNum[idLen - 3: ]
  return id

def makeMajorYear(major, year):
  """Formats major and year as an abbreviated string."""
  if year == "Freshman":
    year = "FR"
  elif year == "Sophomore":
    year = "SO"
  elif year == "Junior":
    year = "JR"
  elif year == "Senior":
    year = "SR"
  major = major.upper()
  major_year = major[0:3] + "-" + year
  return major_year

if __name__ == '__main__':
  main()
