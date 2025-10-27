import turtle as t

def setup():
    t.tracer(1)
    t.screensize(2000,2000)


def levi(n, a):
    if n == 0:
        t.fd(a)
    else:
        t.lt(45)
        levi(n-1,a)
        t.rt(90)
        levi(n-1,a)
        t.lt(45)
        
        
              

def main():
    heihgt = int(input(print("heihgt:")))

    setup()
    
    
    levi(heihgt, 25)

    t.update()
    t.mainloop()

main()