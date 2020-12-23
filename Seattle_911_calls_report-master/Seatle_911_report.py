import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

df=pd.read_csv("C:/python crash course/udemy/Seattle_Police_Department_911_Incident_Response.csv")
print(df)
print(df.info())
print(df.head())


x=df["Event Clearance Group"].iloc[0]
print(x.split(':')[0])

reason=df["Reason"]=df["Event Clearance Group"].apply(lambda event:event)
print(reason)

count=df["Reason"].value_counts()
print("\t\t\t\t\t\t call records according to each incident \t\t\t\t\t\t \n",count)

plt.figure(dpi=128,figsize=(10,8))
plt.tight_layout()
plt.xticks(rotation=90)
plt.title("Seattle_Police_Department \n Total call records of Incidents",fontsize=20)
plt.savefig("seattle.svg")
sb.countplot(x="Reason",data=df)

plt.xlabel("Incidents",fontsize=20)
plt.ylabel("Number of calls")
plt.show()

tp=df["Event Clearance Date"]=pd.to_datetime(df["Event Clearance Date"])
print(tp)

time=df["Event Clearance Date"].iloc[0]
print(time.hour)
print(time.minute)
print(time.dayofweek)
print(time.month)

# You will create these columns based off of the timeStamp column

df["Hour"]=df["Event Clearance Date"].apply(lambda  time: time.hour)
df["dOW"]=df["Event Clearance Date"].apply(lambda  time:time.dayofweek)
df["Month"]=df["Event Clearance Date"].apply(lambda  time: time.month)
print(df.head())


dmap={0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
df["dOW"]=df["dOW"].map(dmap)
print(df.head())
                     #Month
#How many calls reports in a Month
plt.figure(figsize=(12,3))
sb.countplot(x="dOW",data=df,palette="viridis")
plt.title("Call reports on each day\n weekdays are more violent than weekends")
plt.show()
plt.savefig("Each_day_calls.svg")

#Now create a gropuby object called byMonth, where you group the DataFrame
# by the month column and
# use the count() method for aggregation. Use the head() method on this
#  returned DataFrame.

                                  #read it again????
byMonth=df.groupby("Month").count()
print(byMonth.head())


byMonth["Event Clearance Description"].plot()
plt.show()
plt.savefig("calls.svg")


dmap={0:"Jnauary",1:"February",2:"March",3:"April",4:"May",5:"June",6:"July",7:"August",8:"Septembet",
       9:"October",10:"November",11:"December"}
df["Month"]=df["Month"].map(dmap)
print("Month now converted to string",df.head())

#call reports according to each month
sb.countplot(x="Month",data=df,palette="viridis")
plt.title("Number of calls according to each Month")
plt.xticks(rotation=90)
plt.show()
plt.savefig("each_month_calls.svg")

# use seaborn's lmplot() to create a linear fit on the number of calls per month.

sb.lmplot(x="Month",y="Event Clearance Description",data=byMonth.reset_index())
plt.show()
plt.savefig("calls.svg")

df["Date"]=df["Event Clearance Date"].apply(lambda t:t.date())
print(df.head())

date=df.groupby("Date").count().plot()
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
plt.figure(dpi=128,figsize=(10,8))
plt.title("Total number of emergency calls")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
plt.savefig("emergency_calls.svg")

val=df["Date"].value_counts()
print(val)

#LIQUOR
df[df["Reason"]=="LIQUOR VIOLATIONS"].groupby("Date").count()["CAD Event Number"].plot()
plt.title(" Violence occured by Liquor ")
plt.tight_layout()
plt.show()
plt.savefig("Liquor_calls.svg")

#Assault
df[df["Reason"]=="ASSAULTS"].groupby("Date").count()["CAD Event Number"].plot()
plt.title(" Violence occured by Assault ")
plt.tight_layout()
plt.show()
plt.savefig("Assault_calls.svg")

#Traffic
df[df["Reason"]=="TRAFFIC RELATED CALLS"].groupby("Date").count()["CAD Event Number"].plot()
plt.title(" Traffic related calls ")
plt.tight_layout()
plt.show()
plt.savefig("Traffic_calls.svg")

