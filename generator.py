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
from string import Template


def main(files):

    # Construct JSON Data Source and Dash Board feed files for Grafana
    #ds = open("DS_feed.JSON","w+")
    #db = open("DB_feed.JSON","w+")

    # Open the id file
    id_list = open("id_list.txt","r")

    
    for id in id_list:

        # Create a new file
        id = id.rstrip()
        newFile = id + '.JSON'
        #newFile = newFile.rstrip()
        ds = open(newFile,"w+")
        ds_temp = open("DS_JSON_temp.txt","r")
        
        for entry in ds_temp:
            if entry[0] != "#":
                ds.write(entry)

        ds.close()
        
        

    id_list.close()

    
# Program starts here
if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file',nargs='+',help='path to the file')

    # Parse the files separately
    args_namespace=parser.parse_args()
    args=vars(args_namespace)['file']

    # Send files to main function
    main(args)
