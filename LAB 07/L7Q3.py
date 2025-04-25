print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
dict =[{'Deptno': 900 , 'Emprollno': 109 , 'Salary': 500001},
       {'Deptno': 901 , 'Emprollno': 100, 'Salary': 510000},
       {'Deptno': 902 , 'Emprollno': 119 , 'Salary': 500000},
       {'Deptno': 910 , 'Emprollno': 101 , 'Salary': 500020},
       {'Deptno': 920 , 'Emprollno': 191 , 'Salary': 500200}]
f = max (dict, key=lambda  x:x['Salary'])
g= min (dict, key=lambda  x:x['Salary'])
print(f"The maximum value of dictionary is {f}")
print(f"The maximum value of dictionary is {g}")

