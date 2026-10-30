import sys,json,io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
atlas,manifest,out=sys.argv[1:4]
rows=list(map(float,sys.argv[4].split(","))) if len(sys.argv)>4 else [0,.25,.5,.75,1]
im=Image.open(atlas).convert('RGB'); cards=json.load(open(manifest))
assert len(cards)==8
pdfmetrics.registerFont(TTFont('Card','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
c=canvas.Canvas(out,pagesize=(297*mm,210*mm));c.setTitle('Expressions françaises - 8 cartes prototypes')
w,h,g=52*mm,(52*16/9)*mm,4*mm
sx=(297*mm-4*w-3*g)/2; sy=(210*mm-2*h-g)/2
for i,(num,label) in enumerate(cards):
 col=i%4;row=i//4;x=sx+col*(w+g);y=210*mm-sy-(row+1)*h-row*g
 ac=i%2;ar=i//2
 c.setFillColor(HexColor('#ffffff'));c.setStrokeColor(HexColor('#245561'));c.setLineWidth(.7);c.roundRect(x,y,w,h,3*mm,fill=1,stroke=1)
 tile=im.crop((int(ac*im.width/2),int(rows[ar]*im.height),int((ac+1)*im.width/2),int(rows[ar+1]*im.height)))
 if i==0 and len(sys.argv)>5: tile=Image.open(sys.argv[5]).convert('RGB')
 if num==1: tile=tile.crop((int(tile.width*.16),0,tile.width,int(tile.height*.95)))
 if num==96: tile=tile.crop((int(tile.width*.14),0,int(tile.width*.90),tile.height))
 c.drawImage(ImageReader(tile),x+2*mm,y+18*mm,width=w-4*mm,height=h-20*mm,mask='auto',preserveAspectRatio=True,anchor="c")
 text=f'{num}. {label}';size=12;hs=90
 lines=simpleSplit(text,'Card',size,(w-5*mm)/(hs/100))
 while len(lines)>2 and hs>75:
  hs-=1;lines=simpleSplit(text,'Card',size,(w-5*mm)/(hs/100))
 c.setFillColor(HexColor('#183e49'));c.setFont('Card',size)
 for j,line in enumerate(lines):
  t=c.beginText();t.setTextOrigin(x+w/2-pdfmetrics.stringWidth(line,'Card',size)*(hs/100)/2,y+9*mm+(len(lines)-1)*5.5-j*12);t.setFont('Card',size);t.setHorizScale(hs);t.textOut(line);c.drawText(t)
 c.setStrokeColor(HexColor('#8d999b'));c.setLineWidth(.35)
 for xx in (x,x+w):
  for yy in (y,y+h):
   dx=-1 if xx==x else 1;dy=-1 if yy==y else 1
   c.line(xx+dx*mm,yy,xx+dx*2*mm,yy);c.line(xx,yy+dy*mm,xx,yy+dy*2*mm)
c.setFillColor(HexColor('#486068'));c.setFont('Helvetica',7)
c.drawCentredString(148.5*mm,7*mm,'PROTOTYPE | 52 x 92.44 mm | Imprimer a 100 % | 8 cartes')
c.save()
