monthdays = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
print(monthdays.keys())
print(monthdays.values())
print(monthdays.items())
print(monthdays['May'])
monthdays['Feb'] = 29
d = {'a1':35,'a2':35}
monthdays.update(d)
monthdays.pop('a1')
print(monthdays)
