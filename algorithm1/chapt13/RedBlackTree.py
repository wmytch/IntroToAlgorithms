def RBInsertFixup(T,z): #z is red
    while z.p.color==RED:
        if z.p == z.p.p.left:
            y=z.p.p.right
            if y.color==RED:      
                z.p.color=BLACK
                y.color=BLACK
                z.p.p.color=RED
                z=z.p.p #here this time of iteration must be ended in advance 
            elif z==z.p.right: #y.color=black 
                z=z.p
                LeftRotate(T,z)
            z.p.color=BLACK #y.color=black && z is left child
            z.p.p.color=RED
            RightRotate(T,z.p.p)
        else
            y=z.p.p.left
            if y.color==RED:
                z.p.color=BLACK
                y.color=BLACK
                z.p.p.color=RED
                z=z.p.p
            elif z==z.p.left:
                z=z.p
                RightRotate(T,z)
            z.p.color=BLACK
            z.p.p.color=RED
            LeftRotate(T,z.p.p)
    T.root.color=BLACK
           
