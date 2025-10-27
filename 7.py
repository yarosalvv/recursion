import turtle as t

def setup():
    t.tracer(0)
    t.screensize(2000,2000)


def led(n, a):
    if n == 0:
        t.fd(a)
    else:
        led(n-1,a)
        t.lt(90)
        led(n-1,a*0.5)
        t.rt(180)
        led(n-1,a*0.5)
        t.lt(90)
        led(n-1,a)
        
              

def main():
    heihgt = int(input(print("heihgt:")))

    setup()
    
    
    led(heihgt, 25)

    t.update()
    t.mainloop()

main()