"""Data Collection"""
a=float(input("Net Income of Current Year: "))
b=float(input("Total Asset of Current Year: "))
c=float(input("Cash flow from operation: "))
d=float(input("Net Income of Previous Year: "))
e=float(input("Total Asset of Previous Year: "))
f=float(input("Long Term Debt of Current Year: "))
g=float(input("Long Term Debt of Previous Year: "))
h=float(input("Current Asset of Current Year: "))
i=float(input("Current Asset of previous Year: "))
j=float(input("Current Liability of current Year: "))
k=float(input("Current Liability of previous Year: "))
l=float(input("Sales of Current Year: "))
m=float(input("Sales of Previous Year: "))
n=float(input("Gross profit of Current Year: "))
o=float(input("Gross profit of Previous Year: "))
p=float(input("No of share declared in current year: "))

"""Analysis"""

#ROA
ROA=(a/b)*100
R11=(": %.2f" % round(ROA))
R=str(R11)
R1=(R11+"%")
print("ROA OF CURRENT YEAR=", R1)
#CFO
CFO=(c/b)*100
CFO1=("{:.2f}".format(CFO))
C=str(CFO1)
C1=(C+"%")
print("CFO=",C1)
#D(ROA)
DROA=(d/e)*100
Dfina=(ROA-DROA)
Dfina1=("{:.2f}".format(Dfina))
Dfina2=(Dfina1+"%")
Dfinal=str(Dfina2)
print("D(ROA)=",Dfinal)
#D(Leverage)
DLEV1=(f-g)
DLEV2=(b+e)/2
DLEV11=(DLEV1/DLEV2)
DLEV=("{:.2f}".format(DLEV11))
print("D(Leverage)=",DLEV)
#D(Liquidity)
CR1=(h-j)
CR2=(i-k)
DLC0=(CR1-CR2)
DLC=("{:.2f}".format(DLC0))
print("D(Liquidity)=", DLC)
#D(Gross Margin)
GR1=(n/l)
GR2=(o/m)
DG0=(GR1-GR2)
DG=("{:.2f}".format(DG0))
print("D(Gross Margin)=", DG)
#D(Turnover)
AT1=(l/DLEV2)
AT2=(m/DLEV2)
DTUE1=(AT1-AT2)
DTUE=("{:.2f}".format(DTUE1))
print("D(Turnover)=", DTUE)

"""Point Count"""

if(ROA>=0):
    print("POINT 1")
else:
    print("POINT 0")

if(CFO>=0):
    print("POINT 1")
else:
    print("POINT 0")

if(CFO>=ROA):
    print("POINT 1")
else:
    print("POINT 0")

if (Dfina>=0):
        print("POINT 1")
else:
        print("POINT 0")
if (DLEV11>=0):
        print("POINT 1")
else:
        print("POINT 0")

if (p>=0):
        print("POINT 0")
else:
        print("POINT 1")

if (DLC0>=0):
        print("POINT 1")
else:
        print("POINT 0")

if (DG0>=0):
        print("POINT 1")
else:
        print("POINT 0")

if (DTUE1>=0):
        print("POINT 1")
else:
        print("POINT 0")

Total=((ROA>=0)+(CFO>=0)+(CFO>=ROA)+(Dfina>=0)+(DLEV11>=0)+(p>=0)+(DLC0>=0)+(DG0>=0)+(DTUE1>=0)-1)
print((Total))

"""Result Print"""
if Total in {0, 1, 2, 3}:
    print("The company is experiencing financial challenges or operational issues.")
elif Total in {4, 5, 6}:
    print("The company's performance is mixed; further investigation may be necessary.")
elif Total in {7, 8, 9}:
    print("Indicates strong financial health and operational efficiency of the company.")
else:
    print("error")