#!/usr/bin/env python3
import sys
import pandas as pd
           
def main():
    args = sys.argv                                                 #arguments
    combined = pd.DataFrame()                                       #creates empty dataframe
    for i in range(1, len(args)):
        next_file = pd.read_csv(args[i])                            #gets next file
        csv_name = args[i]                                          #gets the csv name
        filename = csv_name[11:]                                    #formats the csv name
        next_file.insert(loc=2, column="filename", value=filename)  #add filename to dataframe
        combined = pd.concat([combined, next_file])                 #concat nextfile to the combined dataframe
    combined = combined.reset_index()                               #resets the index
    combined.to_csv("combined.csv")                                 #outputs dataframe to csv
    
if __name__ == '__main__':
    main()