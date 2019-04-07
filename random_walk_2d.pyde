a=800
x=0
y=0
off=a/30.0
def setup():
    size(a,a)
    background(0)
    stroke(255)
    strokeWeight(2)
     
    line(0,(a+0.0)/2,width,(a+0.0)/2)
    line((a+0.0)/2,0,(a+0.0)/2,width)
    translate(width/2,height/2)
    stroke(0,0,255)
    strokeWeight(10)
    point(0,0)
    

def draw():
    background(0)
    stroke(255)
    strokeWeight(2)
    line(0,(a+0.0)/2,width,(a+0.0)/2)
    line((a+0.0)/2,0,(a+0.0)/2,width)
    global x
    global y
    translate(width/2,height/2)
    stroke(0,0,255)
    strokeWeight(10)
    point(0,0)
    
    stroke(255,0,0)
    point(x,y)
    
    b=random(1)
    if b<0.5:
        if b<0.25:
            print(-1,0)
            x=x-off
        else:
            print (+1,0)
            x=x+off
    else:
        if b<0.75:
            y=y-off
        else:
             y=+off
    
    
    if x>a/2 or x<-a/2:
        x=0
    if y>a/2 or y<-a/2:
        y=0
    
    
