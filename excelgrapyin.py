#!/usr/bin/python3

"""learning how to rip data from excel into python and graph"""
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def main():
    now = datetime.datetime.now()

    mdf = pd.read_excel('mydata.xlsx', sheet_name="Sheet1")
    #print(mdf.columns)
    #print(mdf['year'].values)
    #print(mdf['min'].values)

    xaxislist = list(mdf['year'].values)
    yaxislist = list(mdf['min'].values)


    #xaxislist = ["2016", "2017", "2018", "2019"]
    #yaxislist = [100, 2200, 4, 55]
    plt.ylabel("Downtime in minutes")
    plt.xlabel("Years")
    plt.title("Total amount of downtume in minutes in year!")
    plt.plot(xaxislist, yaxislist)
    #plt.savefig(now.strftime("%Y-%m-%d-outage.png"))
    plt.show()


if __name__ == '__main__':
    main()
