"""Use regex to find the average price of coffee every year from the given text blob. Print the year along with the avg coffee price for that year.

Text blob:

According to the USDA, the average price of a pound of coffee beans was $4.18 in 2020. In 2019, the average price was $4.12, and in 2018, the average price was $4.16.
Based on these prices, we can estimate that the average price of a pound of coffee beans in 2022 will be around $4.20.
Of course, this is just an estimate, and coffee bean prices could fluctuate depending on the factors mentioned above.
"""

import re

s= '''According to the USDA, the average price of a pound of coffee beans was $4.18 in 2020. In 2019, the average price was $4.12. We don't know the price in 2023, In 2018
the average price was $4.16. Based on these prices, we can estimate that the average price of a pound of coffee beans in 2022 will be around $4.20.Of course,
this is just an estimate, and coffee bean prices could fluctuate depending on the factors mentioned above.'''

print(f'Given string is: \n{s}')

regex = re.compile('\\$(\\d[\\d.,]*)\\b')  ###(r'\$(\d[\d.,]*)\b')
reg= "\d{4}"#re.compile(r'/^\d{4}$/')


a=re.findall(regex, s)
b=re.findall(reg, s)

print(a)
print(b)
for i in range(0,len(a)):
    print(f"Price is {a[i]} and year is {b[i]}")


#a= [float(i) for i in a]
#b= [int(i) for i in b]
d = dict((price, year) for price, year in zip(a,b))

for key, val in d.items():
    print(f"In year {val} average price of coffee was ${key}" )

