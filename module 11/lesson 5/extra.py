class a:
     def __init__(self):
        print( "i am class a,parent of class b" )
       
class b(a):
      def __init__(self):
           print("i am claas b,parent of class a")
            
class c(b):
       def __init__(self):
            print("i am claas c")

a1=a()
a2=b()
a3=c()

