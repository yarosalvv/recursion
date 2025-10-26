import turtle as t

def setup():
    t.tracer(1)
    t.screensize(2000,1500)


def tree(n, h, a):
    if n == 0:
        return 
    
    t.fd(h)
    t.rt(a)

    tree(n-1, h*0.6, a)

    t.lt(a*2)

    tree(n-1, h*0.6, a)

    t.rt(a)
    t.bk(h)
    

def main():
    heihgt = int(input(print("heihgt:")))
    angle = int(input(print("angle:")))
          
    setup()

    t.lt(90)

    tree(heihgt, 200, angle)

    t.update()
    t.mainloop()

main()


