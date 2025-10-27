import turtle as t

def setup():
    t.tracer(0)
    t.screensize(2000,2000)


def led2(n, a):
    if n == 0:
        t.fd(a)
    else:
        led2(n-1,a)
        t.lt(120)
        led2(n-1,a*0.5)
        t.lt(180)
        led2(n-1,a*0.5)
        t.lt(120)
        led2(n-1,a*0.5)
        t.lt(180)
        led2(n-1,a*0.5)
        t.lt(120)
        led2(n-1,a)
        
        
              

def main():
    heihgt = int(input(print("heihgt:")))

    setup()
    
    
    led2(heihgt, 25)

    t.update()
    t.mainloop()

main()