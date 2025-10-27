import turtle as t

def setup():
    t.tracer(0)
    t.screensize(2000,2000)


def koh(n, a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1,a)
        t.lt(90)
        koh(n-1,a)
        t.rt(90)
        koh(n-1,a)
        t.rt(90)
        koh(n-1,a)
        koh(n-1,a)
        t.lt(90)
        koh(n-1,a)
        t.lt(90)
        koh(n-1,a)
        t.rt(90)
        koh(n-1,a)

              

def main():
    heihgt = int(input(print("heihgt:")))

    setup()
    
    
    koh(heihgt, 50)

    t.update()
    t.mainloop()

main()