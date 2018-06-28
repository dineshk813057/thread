#question1
import datetime
import threading
import time
def task():
    for i in range(3):
        print("thread is starting",datetime.datetime.now())
        time.sleep(5)
    print("thread ends",datetime.datetime.now())

task()

#question2
import threading
import time
import datetime
def task():
    for i in range(1,11):
        print("number is %d"%(i),datetime.datetime.now())
        time.sleep(1)

task()

#question3
import datetime
import time
l=[1,2,3,4,5]
i=0
for j in l:
    
    time.sleep(i)
    print(j,datetime.datetime.now())
    i+=2
            

#question4
import datetime
import time
import threading
class task(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
        
    def fact(self):
        self.n=1
        while(self.num>0):
            self.n=self.n*self.num
            self.num=self.num-1
        print("factorial is %d"%(self.n))
    def run(self):
        self.fact()

num=int(input("enter number you want factorial of"))
thread=task(num)
thread.start()




    


    

    





    


    

    

