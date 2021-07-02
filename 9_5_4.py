def add_dic(zidian,en,ch):
    zidian[str(en)]=str(ch)
    return zidian
def search_dic(zidian,en):
    print(zidian[str(en)])
zidian = {}
while True:
    order = input('order：1-input，2-search，3-quit:')
    if order == '1':
      add_dic(zidian,en=input('english words：'),ch=input('chinese meaning：'))
    elif order == '2':
        search_dic(zidian,en=input('english words：'))
    elif order == '3':
        break
    else :
        print('Wrong order!')
    
