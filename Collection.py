#Dependencies
import xport
import pandas as pd
import glob

###Glob SAS files
#1_Demographics
demograph_df = pd.DataFrame()

for i in glob.glob('DEMO_Demogr_Data/*.xpt'):
    sas_i = pd.read_sas(i, index=None)
    #print(sas_i)
    sas_df= pd.DataFrame(sas_i)
    demograph_df = demograph_df.append(sas_df, ignore_index=True)

demograph_df.head()
#demograph_df


#2_Diabetes
diabetes_df = pd.DataFrame()

for i in glob.glob('DIQ_Diab_Data/*.xpt'):
    sas_i = pd.read_sas(i, index=None)
    #print(sas_i)
    sas_df= pd.DataFrame(sas_i)
    diabetes_df = diabetes_df.append(sas_df, ignore_index=True)

diabetes_df.head()
#diabetes_df


#3_Dietary
dietary_df = pd.DataFrame()

for i in glob.glob('DRIFF_Diet_Data/*.xpt'):
    sas_i = pd.read_sas(i, index=None)
    #print(sas_i)
    sas_df= pd.DataFrame(sas_i)
    dietary_df = dietary_df.append(sas_df, ignore_index=True)

dietary_df.head()
#dietary_df

#__________________________________________________________________#
#To SQL
from pandas.io import sql
import MySQLdb

#Enter these variables - to be made into inputs?
host = "########"
user = "########"
password = "##########"

#Database connection
con= MySQLdb.connect(host=host, user=user, port=3306, passwd=password)

#__________________________________________________________________#
#Database Layout
