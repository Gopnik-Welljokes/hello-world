from turtle import *

colors = ['black','dimgrey','dimgray','grey','gray','darkgrey','darkgray','silver','lightgrey','lightgray',
          'gainsboro','whitesmoke','white','snow','rosybrown','lightcoral','indianred','brown','firebrick',
          'maroon','darkred','red','mistyrose','salmon','tomato','darksalmon','coral','orangered','lightsalmon'
          ,'sienna','seashell','chocolate','saddlebrown','sandybrown','peachpuff','peru','linen','bisque',
          'darkorange','burlywood','antiquewhite','tan','navajowhite','blanchedalmond','papayawhip','moccasin',
          'orange','wheat','oldlace','floralwhite','darkgoldenrod','goldenrod','cornsilk','gold','lemonchiffon',
          'khaki','palegoldenrod','darkkhaki','ivory','beige','lightyellow','lightgoldenrodyellow','olive',
          'yellow','olivedrab','yellowgreen','darkolivegreen','greenyellow','chartreuse','lawngreen','honeydew',
          'darkseagreen','palegreen','lightgreen','forestgreen','limegreen','darkgreen','green','lime','seagreen',
          'mediumseagreen','springgreen','mintcream','mediumspringgreen','mediumaquamarine','aquamarine','turquoise',
          'lightseagreen','mediumturquoise','azure','lightcyan','paleturquoise','darkslategrey','darkslategray','teal',
          'darkcyan','cyan','aqua','darkturquoise','cadetblue','powderblue','lightblue','deepskyblue','skyblue',
          'lightskyblue','steelblue','aliceblue','dodgerblue','lightslategrey','lightslategray','slategrey','slategray',
          'lightsteelblue','cornflowerblue','royalblue','ghostwhite','lavender','midnightblue','navy','darkblue',
          'mediumblue','blue','slateblue','darkslateblue','mediumslateblue','mediumpurple','rebeccapurple','blueviolet',
          'indigo','darkorchid','darkviolet','mediumorchid','thistle','plum','violet','purple','darkmagenta',
          'magenta','fuchsia','orchid','mediumvioletred','deeppink','hotpink','lavenderblush','palevioletred','crimson',
          'pink','lightpink']
#'k','w','r','y','g','c','b','m'
def wheel(g):
    for i in range(len(colors)):
        pencolor("black")
        fillcolor(colors[i])
        begin_fill()
        if g == 1:
            forward(10); left(360/len(colors))
            for a in range(4):
                right(90); forward(10)
            end_fill()
        elif g==2:
            forward(10*0.75); left((360*1.25)/len(colors))
            for a in range(4):
                right(90); forward(10*0.75)
            end_fill()
def printColors():
    i = len(colors) - 2
    while i != 0:
        print(f"{i:<3} {colors[i]:<20}")
        i = i - 1
    print("0",colors[0])

printColors()
"""
speed = "fastest"
hideturtle()

forward(100)
#wheel(1)
fillcolor("black")
begin_fill()
circle(200)
end_fill()
left(90); forward(10); right(90)
wheel(2)
#"""
