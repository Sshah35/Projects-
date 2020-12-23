# Name: Siddharth Kapoor

# ID:900467489

import csv
import matplotlib.pyplot as plt

# make the not-a-number constant (without numpy)
NaN = float('NaN')


# Remember that in math, infinite does not equal infinite,thus
# NaN does not equal NaN. All real numbers equal themselves
def isNaN(n):
    return n != n


# Parsenums (simplified for comma-free required, and only floats desired)
def parseNums(x):
    try:
        return float(x)
    except:
        return NaN


# Take a row (dictionary) and convert a list of named columns from text into floats
def Numify_Columns(Row, Columns):
    for column in Columns:
        Row[column] = parseNums(Row[column])

    #################### START


# Constants and Globals
count = 0
total = 0.0
Degrees = {}
Number_of_Men = []
dict = {}
Number_of_Women = []
COLUMNS = ["RELAFFIL", "UGDS_WOMEN", "UGDS", "UGDS_MEN", "HIGHDEG", "INEXPFTE", "AVGFACSAL"]
FILE = 'C:/comp in python/MERGED2014_15_PP.csv'

data = open(FILE, 'rU')


# Create the reader

def read_funding_data(path):
    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row


Degrees = {}
Degrees_list = []
school_data = []
Missing_Salaray_Count = 0
Majors = ['PCIP01', 'PCIP02', 'PCIP03', 'PCIP04', 'PCIP05', 'PCIP06', 'PCIP07', 'PCIP08', 'PCIP09', 'PCIP10', 'PCIP11',
          'PCIP12', 'PCIP13', 'PCIP14', 'PCIP15', 'PCIP16', 'PCIP17', 'PCIP18', 'PCIP19', 'PCIP20', 'PCIP21', 'PCIP22',
          'PCIP23', 'PCIP24', 'PCIP25', 'PCIP26', 'PCIP27', 'PCIP28', 'PCIP29', 'PCIP30', 'PCIP31', 'PCIP32', 'PCIP33',
          'PCIP34', 'PCIP35', 'PCIP36', 'PCIP37', 'PCIP38', 'PCIP39', 'PCIP40', 'PCIP41', 'PCIP42', 'PCIP43', 'PCIP44',
          'PCIP45', 'PCIP46', 'PCIP47', 'PCIP48', 'PCIP49', 'PCIP50', 'PCIP51', 'PCIP52', 'PCIP53']
for degrees in Majors[0:54]:  # try to make a loop which run from 0 to 53 and give the list of all PCIP values appear
    Degrees_list.append(degrees)
print "number of degrees", Degrees_list
for Row in read_funding_data(FILE):
    Degrees = {}
    if Row["STABBR"] == "IL":
        Numify_Columns(Row, COLUMNS)
        for header in Row.keys():
            if header in Degrees_list:
                Numify_Columns(Row, [header])
                if Row[header] > 0:
                    Degrees[header] = Row[header]
        # sort the degrees
        Sorted_Degrees = sorted(Degrees.items(),cmp = lambda x,y: cmp(y[0][1],x[0][1]))
        if len(Sorted_Degrees) > 0:
            # gives the institution name, ugds_men, ugds_women and degrees of the "IL" area
            dict[Row["INSTNM"]] = {"UGDS_MEN": Row["UGDS_MEN"], "UGDS_WOMEN": Row["UGDS_WOMEN"],
                                   "Degrees": Sorted_Degrees[0:5]}
            if Row["UGDS_MEN"] > Row["UGDS_WOMEN"]:
                for men in Sorted_Degrees[0:5]:
                    Number_of_Men.append(men[0])
            elif Row["UGDS_WOMEN"] > Row["UGDS_MEN"]:
                for women in Sorted_Degrees[0:5]:
                    Number_of_Women.append(women[0])
print(dict)
data.close()
men = []
women = []

'''bar only counts the numerical value so I count how many times men and women occurs
based on their degree level and then visualize it'''

for degree in Majors:
    men.append((Number_of_Men.count(degree)))
    women.append(Number_of_Women.count(degree))
print "number of men", men
print "number of women", women

# now visualize a stacked bar graph

plt.figure(figsize=(25, 15), dpi=128)  # use to adjust the size of the bar graph
plt.title("Gender based on Degrees of IL area", size=40)
plt.xlabel("DEGREES", fontsize=25)
plt.bar(Majors, men, label="men", width=0.50)  # bar graph 1 with width size is 0.50
plt.ylabel("Gender\n Men & Women", fontsize=25)
plt.bar(Majors, women, bottom=men, label="women", width=0.50)
plt.xticks(rotation=90)  # rotate the values of x axis by 90 degree
plt.legend(prop={"size": 30})  # legend is used to display the label in our bar grapbh
plt.savefig("degrees_project.png")  # this will save this figure

plt.tick_params(axis="both", which="major", labelsize=20)
plt.show()










