def setup():
    size(800, 800)
    
    global radius
    global secondsRadius
    global minutesRadius
    global hoursRadius
    global clockDiameter
    global cx
    global cy
    
    r = width/2
    secondsRadius = r * 0.6
    minutesRadius = r * 0.45
    hoursRadius = r * 0.3
    clockDiameter = r * 1.5
    cx = width/2
    cy = height/2
    

def draw():
    background('#000000')
    fill('#FFFFFF')
    noStroke()
    ellipse(cx, cy, clockDiameter, clockDiameter)
    
    s = map(second(), 0, 60, 0, TWO_PI) - HALF_PI
    m = map(minute() + norm(second(), 0, 60), 0, 60, 0, TWO_PI) - HALF_PI
    h = map(hour() + norm(minute(), 0, 60), 0, 24, 0, QUARTER_PI) - HALF_PI
    
    stroke('#FF0000');
    strokeWeight(2);
    line(cx, cy, cx + cos(s) * secondsRadius, cy + sin(s) * secondsRadius);
    
    stroke('#00FF00');
    strokeWeight(4);
    line(cx, cy, cx + cos(m) * minutesRadius, cy + sin(m) * minutesRadius);
    
    stroke('#0000FF');
    strokeWeight(8);
    line(cx, cy, cx + cos(h) * hoursRadius, cy + sin(h) * hoursRadius);
    
    stroke('#000000')
    strokeWeight(15)
    point(cx, cy)
    