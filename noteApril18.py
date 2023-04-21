#input
data.iloc[2]
#output =>
mpg                           18.0
cylinders                        8
displacement                 318.0
horsepower                   150.0
weight                        3436
acceleration                  11.0
model_year                      70
origin                         usa
name            plymouth satellite
Name: 2, dtype: object
#input
data.iloc[2,2]
#output 318
#-------------------------
data.iloc[100:110, 2:5]
#output
	displacement	horsepower	weight
100	250.0	88.0	3021
101	198.0	95.0	2904
102	97.0	46.0	1950
103	400.0	150.0	4997
104	400.0	167.0	4906
105	360.0	170.0	4654
106	350.0	180.0	4499
107	232.0	100.0	2789
108	97.0	88.0	2279
109	140.0	72.0	2401

#------------------
#data,loc[ 2, "displacement"]
# expr.ident 
# if the 