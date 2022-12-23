import math
import cv2
from cvzone.HandTrackingModule import HandDetector
name = "laika"
version = "alpha"
creator = "Au0_error"
msg1 = '''
hello user this is a small ia for you. I can help you whit your homework, research and leaflet for the medicinal (just type the name of meficinal)
'''
msg2 = '''
i'm sorry but i can't resolve youre question
'''
print(msg1)
while True:
 init = input('-->')
 if (init == "math"):
  print("what do you have need?")
  oper = input('operation(+,-,/,*,rad)--->')
  if (oper == "+"):
    s = x+y
    x = input('first num:')
    y = input('second num:')
    print(s)
  if (oper == "-"):
   sot = x-y
   x = input('first num:')
   y = input('second num:')
   print(sot)
  if (oper == "*"):
    molt = x*y 
    x = input('first num')
    y = input('second num')
    print(molt)
  if (oper == "/"):
     div = x/y
     rest = x%y
     x = input('first num')
     y = input('second num')
     print(div, "rest: ", rest )
  if (oper == "rad"):
    quad = math.sqrt(x)
    x = input('number:')
    print(quad)
 if (init == "phisic"):
   print("ok, i can help you!!")
   ph = input('relativity,inverse,direct,quadratic,costant,ohm-->')
   if (ph == "relativity"):
    relativity = "E=mc^2"
    E = m*A
    A = c*c
    c = 299792458
    print("relativity")
    m = input('insert mass~~>')
    print("energy is:", E)
   if (ph == "inverse"):
    inversek = x*y
    inversex = k*y
    inversey = x/k
    domain = input('what do you need to calcolate?:')
    if (domain == "x"):
       y = input('y:')
       k = input('k:')
       print(inversex)
    if (domain == "y"):
     x = input('x:')
     k = input('k:')
     print(inversey)
    if (domain == "k"):
     x = input('x:')
     y = input('y:')
     print(inversek)
   if (ph == "direct"):
    directk = x/y
    directx = k*y
    directy = x/k
    domai = input('what do you need to calcolate?:')
    if (domai == "x"):
     y = input('y:')
     k = input('k:')
     print(directx)
    if (domai == "y"):
      x = input('x:')
      k = input('k:')
      print(directy)
    if (domai == "k"):
      x = input('x:')
      y = input('y:')
      print(directk)
   if (ph == "quadratic"):
     X = x*x
     quadraticx = math.sqrt(X)
     quadraticy = k*X
     quadratick = y/X
     doma = input('what do you need to calcolate?:')
     if (doma == "x"):
        y = input('y:')
        k = input('k:')
        print(quadraticx)
     if (doma == "y"):
      x = input('x:')
      k = input('k:')
      print(quadraticy)
     if (doma == "k"):
        x = input('x:')
        y = input('y:')
        print(quadratick)
   if (ph == "costant"):
     cons = '''
     "light speed = 299792458"
     "pi greek = 3.14"
     "exetended: 3,14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 06286 20899 86280 34825 34211 70679"
     "gravitation accelleration = 9,80665"
     "proton charge = +1,6022x10^-19 or +1,6022E-19"
     "electron charge = -1,6022x10^-19 or -1,6022E-19"
     "gas costant = 8.314"
     "costant of boltzmann = 1,3806x10-23 or 1,380E-23"
     '''
     print(cons)
   if (ph == "ohm"):
    V = i*r
    I = v/r
    R = v/i
    print("what do you want calcolate?")
    var = input('R/I/V~~>')
    if (var == R):
       v = input('voltage=')
       i = input('ampere=')
       print(R)
    if (var == I):
       r = input('resistence=')
       v = input('voltage=')
       print(I)
    if (var == V):
       r = input('resistence=')
       i = input('ampere=')
       print(V)
 if (init == "chemestry"):
     elementlist = '''
    h = "hydrogen"  
    he = "helium" 
    li = "litium"
    be = "berillium"
    b = "barium"
    c = "carbon"
    n = "nitrogen"
    o = "oxygen"
    f = "florine"
    ne = "neon"
    na = "sodium"
    mg = "magnesium"
    al = "alluminium"
    si = "silicon"
    p = "phosphorus"
    s = "sulphur"
    cl = "chlorine"
    ar = "argon"
    k = "potassium"
    ca = "calcium"
    sc = "scandium"
    ti = "titanium"
    v = "vanadium"
    cr = "chromium"
    mn = "manganese"
    fe = "iron"
    co = "cobalt"
    ni = "nickel"
    cu = "copper"
    zn = "zinc"
    ga = "gallium"
    ge = "germanium"
    As = "arsenic"
    se = "selenium"
    br = "bromine"
    kr = "kripton"
    rb = "rubidium"
    sr = "stronzium"
    y = "yttrium"
    zr = "zirconium" 
    nb = "niobium"
    mo = "molybdenum"
    tc = "technetium"
    ru = "ruthenium"
    rh = "rhodium"
    pd = "palladium"
    ag = "silver"
    cd = "cadmium"
    In = "indium"
    sn = "tin"
    sb = "antimony"
    te = "tellurium"
    i = "iodine"
    xe = "xenon"
    cs = "caesium"
    ba = "barium"
    la = "lanthanum"
    hf = "hafnium"
    ta = "tantalium"
    w = "tungsten"
    re = "renium"
    os = "osmium"
    ir = "iridium"
    pt = "platinum"
    au = "gold"
    hg = "mercury"
    tl = "thallium"
    pb = "lead"
    bi = "bismuth"
    po = "polonium"
    at = "astatine"
    rn = "radon"
    fr = "francium"
    ra = "radium"
    ac = "actinium"
    rf = "rutherfordium"
    db = "dubnium" 
    sg = "seaborgium"
    bh = "bohrium"
    hs = "hassium"
    mt = "meitnerium"
    ds = "darmstadium"
    rg = "roentegenium"
    cn = "copernicium"
    uut = "unutrium"
    fl = "flerovium"
    uup = "ununpentium"
    lv = "livermonium"
    uus = "ununseptium"
    uuo = "ununoctium"
    '''
     print(elementlist)
 if (init == "med"):
    print("coming soon")
 if (init == "move"):
    detector =HandDetector(detectionCon = 0.8, maxHands = 2)
    video = cv2.VideoCapture(1)
    while True:
     ret, frame = video.read()
     hands, img = detector.findHands(frame)
     cv2.imgshow("Frame", frame)
     ciccio = cv2.waitKey(1)
     if (ciccio == ord('q'))
      break 
    video.relase()
    cv2.destroyAllWindows()
