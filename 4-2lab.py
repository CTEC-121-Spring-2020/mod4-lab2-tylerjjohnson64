"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # code here
    win = GraphWin("demo",800,800)
    win.setCoords(-4,0, -4.0, 4.0, 4.0)
    p1 = Circle(Point(2, 3),0.1)
    p1.setFill("red")
    p2 = Point(-3, 1).draw(win)
    p3 = Point(-1.5, -2.5).draw(win)
    input()
main()    