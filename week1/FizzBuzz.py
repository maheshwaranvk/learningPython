#Assignment - https://drive.google.com/open?id=1U8JPzNRmuNLXHx2atzxYad3lw0MZkchR&usp=drive_fs

def fizzBuzz(a):
    for i in range(1,a+1):
        if (i%3==0 and i%5==0):
            print("FizzBuzz")
        elif (i%3==0 and not i%5==0):
            print("Fizz")
        elif (i%5==0 and not i%3==0):
            print("Buzz")
        else :
            print(i)
fizzBuzz(12)