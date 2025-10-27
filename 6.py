import turtle as t

def setup():
    t.tracer(0)
    t.screensize(2000,2000)


def mink(n, a):
    if n == 0:
        t.fd(a)
    else:
        mink(n-1,a)
        t.lt(90)
        mink(n-1,a)
        t.rt(90)
        mink(n-1,a)
        t.rt(90)
        mink(n-1,a)
        mink(n-1,a)
        t.lt(90)
        mink(n-1,a)
        t.lt(90)
        mink(n-1,a)
        t.rt(90)
        mink(n-1,a)

              

def main():
    heihgt = int(input(print("heihgt:")))

    setup()
    
    
    mink(heihgt, 25)

    t.update()
    t.mainloop()

main()