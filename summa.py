# %%
a = 5
b = 10
c = a + b
print(c)

# %%
for i in range(0,5):
    print(i)

# %%
i = 0
while i != 10:
    i += 1
    print(i)

# %%
list_ = []
set_ = {}
tuple_ = ()
dict_ = {'summa':'harish','lav':'yuvan','ninju':'sanju'}

# %%
print([1,2,3,4,4])
print({1,2,3,4,4})


print((1,2,3,4,4))

print(dict_)

# %%
print(dict_['ninju'])

# %%
"""
1
12
123
1234    
"""
n = 4

for row in range(0,n):
    for col in range(1,row+2):
        print(col,end="")
    print()

