import turtle as t

def setup():
    t.tracer(1)
    t.screensize(2000,1500)


def k(n, a):
    if n == 0:
        t.fd(a)
        t.rt(90)

    else:
        for i in range(4):
            k(0, a)

        t.rt(4.5)
        t.up()
        t.fd(10)
        t.down()
        k(n - 1, a*0.96)

def main():
    setup()

    k(30, 250)

    t.update()
    t.mainloop()

main()