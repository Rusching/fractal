import turtle as tl
import pdb



def draw(n, angle, start_cmd, alpha, rules, step=5):
    cmd = start_cmd
    tmp = ""
    stack = []
    try:
        for _ in range(n):
            for each_l in cmd:
                if each_l in alpha:
                    tmp += rules[each_l]
                else:
                    tmp += each_l
            cmd = tmp
            tmp = ""
    except:
        pdb.set_trace()
    print(cmd)
    
    tl.tracer(False)
    tl.screensize (200,5000)
    tl.hideturtle()
    t = tl.Pen()
    t.left(90)
    for each_l in cmd:
        if each_l == "F":
            t.forward(step)
        elif each_l == "f":
            t.up()
            t.forward(step)
            t.down()
        elif each_l == "+":
            t.left(angle)
        elif each_l == "-":
            t.right(angle)
        elif each_l == "[":
            stack.append((t.position(), t.heading()))
        elif each_l == "]":
            t.up()
            preState = stack.pop()
            t.setposition(preState[0])
            t.setheading(preState[1])
            t.down()

    tl.update()
    tl.getscreen().getcanvas().postscript(file="tree1.eps")
    tl.done()

def main():
    n = 6
    angle = 20
    # Fl -> F
    # Fr -> f
    # Fl→  Fl+Fr++Fr-Fl--FlFl-Fr+
    # Fr→ -Fl+FrFr++Fr+Fl--Fl-Fr
    start_cmd = "X"
    alpha = "XF[]"
    # rules = {
    #     "F": "FF-[-F+F+F]+[+F-F-F]",
    #     "[": "[",
    #     "]": "]"
    # }
    rules = {
        "X": "F[+X]F[-X]FF+X",
        "F": "FF",
        "[": "[",
        "]": "]",
    }
    draw(n, angle, start_cmd, alpha, rules, step=5)

if __name__ == "__main__":
    main()
