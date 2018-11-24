print('Hello, Django girls!')
if 3 > 2:
    if 3 < 2:
        print('It works!')
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
name = 'Ray'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Ray':
    print('Hey Rayray!')
else:
    print ('Hey you!')
def hi():
    print('Hi there!')
    print('How are you?')
hi ()
def hi(name):
    if name == 'Ray':
        print('Hi Rayray!')
    elif name == 'Ola':
        print('Hi Ola!')
    else:
        print('Hi you!')
hi("Nobody")
def hi(name):
    print('Hi ' + name + '!')
hi("Rachel")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ray']
for name in girls:
    hi(name)
    print('Next girl')
