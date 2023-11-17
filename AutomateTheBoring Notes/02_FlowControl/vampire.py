#name = 'Carol'
#age = 3000
#if name == 'Alice':
   #print('Hi, Alice')
#elif age < 12:
    #print('You are not Alice, Kiddo')
#elif age > 2000:
   #print('Unlike you, Alice is not an undead, immortal vampire.')
#elif age > 100:
    #print('You are not Alice, grannie.') 
#2000 is printed because age is higher than 2000

name = 'Carol'
age = 3000
if name == 'Alice':
  print('Hi, Alice')
elif age < 12:
    print('You are not Alice, Kiddo')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.') 

#100 is printed because of the order the ELIF statements come in. First true is the first printed and the rest are ignored.