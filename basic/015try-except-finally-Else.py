# try - run this code
# except - block lets you handle the error
# else - block if no exception in the programme
# finally - this code always execute

try:
    # b
    a =1/0
except NameError:
    print('not defined')
except Exception as e:
    print('Exception: ', e)
else:
    print('lol')
finally:
    print('Always!')