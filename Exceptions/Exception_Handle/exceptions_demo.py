class Exceptions():

    def exceptions_handle_demo(self):
        try:
          a = 10
          b = 20
          c = 0
          d = (a + b) / c
          print(d)

        except:
            print('We are in Except Block')


obj = Exceptions()
obj.exceptions_handle_demo()
