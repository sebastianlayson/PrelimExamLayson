class Triangle:
    def calculatePerimeter(sideA,sideB,sideC):
        return sideA + sideB + sideC
    def calculateArea (height,base):
        return (height*base)/2
sideA = 10
sideB = 10
sideC = 10
height =20
base = 15
perimeter = Triangle.calculatePerimeter(sideA,sideB,sideC)
area = Triangle.calculateArea(height,base)
print ("This is the perimeter:", perimeter)
print ("This is the area:",area)

