print("select a shape to find area:\n1. circle\n2. rectangle\n3. square\n")
shape=input()
def aos(shape):
    if shape=="circle":
        r=float(input("enter the radius of circle:"))
        area=3.14*r*r
        print("area of circle is:",area)
    elif shape=="rectangle":
        l=float(input("enter the length of rectangle:"))
        b=float(input("enter the breadth of rectangle:"))
        area=l*b
        print("area of rectangle is:",area)
    elif shape=="square":
        a=float(input("enter the side of square:"))
        area=a*a
        print("area of square is:",area)
    else:
        print("invalid shape")
aos(shape)