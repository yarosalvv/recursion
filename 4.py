import turtle as t

def setup():
    t.tracer(0)
    t.screensize(2000,2000)


def koh(n, a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1,a/3)
        t.lt(60)
        koh(n-1,a/3)
        t.rt(120)
        koh(n-1,a/3)
        t.lt(60)
        koh(n-1,a/3)          

def main():
    heihgt = int(input(print("heihgt:")))

    setup()
    
    
    koh(heihgt, 500)

    t.update()
    t.mainloop()

main()