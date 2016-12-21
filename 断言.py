class MyError(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message
# try:
#     raise MyError('我的异常')
# except MyError as e:
#     print(e)

a = 1
try:
    raise MyError('我的异常')
except MyError as e:
    print(e)
else:
    print("hahah else")
finally:
    print("no matter right or wrong,run this anyway!")

