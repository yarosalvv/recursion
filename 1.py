import turtle as t
t.tracer(0)

t.screensize(2000,1500)

def koh(n, a):
    if n == 0:
        t.fd(a)
        t.rt(90)

    else:
        for i in range(4):
            koh(0, a)

        t.rt(4.5)
        t.up()
        t.fd(10)
        t.down()
        koh(n - 1, a*0.96)


koh(30, 250)


t.update()
t.mainloop()