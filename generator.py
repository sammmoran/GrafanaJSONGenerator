# FileName: generator.py
# Author: Samuel Moran
# Created: 7/9/2019

# Description:
# This program generates JSON files for Grafana. It generates two JSON files:
# 1) one Data Source file, 2) another Dash Board file. These files are then
# fed into Grafana to automate DashBoard creation with panels.
# This program is part of a larger project to automate data feeding for
# DevOps observation.



import argparse


# This function will create the Data Source JSON file from nothing
# and populate it with information from the DS_JSON_temp file.
# The end result of this function is a Data Source JSON file to be
# fed into Grafana.
def createDS(id, ds_temp):
    
    # Create a new file using the Instance ID name
    id = id.rstrip()
    newFile = id + '.json'
    ds = open(newFile,"w+")

    ds.write("{")
    
    # Construct the Data Source template file using DS_JSON_temp.txt
    for entry in ds_temp:

        if entry == 'name\n':
            newEntry = '"name":"' + id + '",\n'
            ds.write(newEntry)
            
        # If just a regular line, simply add it to the JSON file
        if entry[0] != "#" and entry != 'name\n':
            ds.write(entry)

        # If the line contains a template header, modify it accordingly
        #if entry[0] == "$":
        #ds.write('"name":' + id + '",'+"\n")

       
        
    ds.write("}")
    
    ds.close()


def main(files):

    # Open the id file
    id_list = open("id_list.txt","r")

    # Iterate through the AWS Instances list
    for id in id_list:

        # Open the DS template file temporarily
        ds_temp = open("DS_JSON_temp.txt","r")

        # Pass to CreateDS function
        createDS(id, ds_temp)

        # Close the DS template file
        ds_temp.close()


    # JSON Data Source and Dash Board files have been created...

    # Close the id list
    id_list.close()

    # This program has reached its end...

    
# Program starts here
if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file',nargs='+',help='path to the file')

    # Parse the files separately
    args_namespace=parser.parse_args()
    args=vars(args_namespace)['file']

    # Send files to main function
    main(args)
