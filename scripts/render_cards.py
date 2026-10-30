import json,math,sys
from pathlib import Path
from PIL import Image,ImageChops
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import numpy as np
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
manifest=json.loads((ROOT/'manifest.json').read_text())
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('Card',FONT))
def lines_for(text):
 words=text.split();width=50.2*mm
 if pdfmetrics.stringWidth(text,'Card',12)*.9<=width:return [text],90
 candidates=[]
 for j in range(1,len(words)):
  lines=[' '.join(words[:j]),' '.join(words[j:])]
  widths=[pdfmetrics.stringWidth(l,'Card',12) for l in lines]
  candidates.append((max(widths),abs(widths[0]-widths[1]),lines))
 _,_,lines=min(candidates,key=lambda x:(x[0],x[1]))
 hs=min(90,width/max(pdfmetrics.stringWidth(l,'Card',12) for l in lines)*100)
 return lines,hs

def build(items,out,title):
 c=canvas.Canvas(str(out),pagesize=(297*mm,210*mm));c.setTitle(title);c.setAuthor('Expressions françaises')
 w,h,g=54.2*mm,98*mm,4*mm
 sx=(297*mm-5*w-4*g)/2;sy=(210*mm-2*h-g)/2
 stats=[]
 for start in range(0,len(items),10):
  for j,item in enumerate(items[start:start+10]):
   idx=item['id'];col=j%5;row=j//5;x=sx+col*(w+g);y=210*mm-sy-(row+1)*h-row*g
   c.setFillColor(HexColor('#ffffff'));c.setStrokeColor(HexColor('#245561'));c.setLineWidth(.7)
   c.roundRect(x,y,w,h,3*mm,fill=1,stroke=1)
   im=Image.open(ROOT/'assets'/f'{idx:03}.png').convert('RGB')
   a=np.asarray(im)
   yy,xx=np.where(a.min(2)<230)
   if len(xx):
    pad=4
    im=im.crop((max(0,int(xx.min())-pad),max(0,int(yy.min())-pad),min(im.width,int(xx.max())+pad+1),min(im.height,int(yy.max())+pad+1)))
   text=f"{idx}. {item['text']}";lines,hs=lines_for(text)
   if hs<65: raise ValueError(f'Card {idx}: text needs layout review, horizontal scale {hs:.1f}%')
   line_height=14
   text_height=len(lines)*line_height
   gap=3.5*mm
   available_height=h-12*mm-text_height-gap
   scale=min((w-4*mm)/im.width,available_height/im.height)
   dw,dh=im.width*scale,im.height*scale
   effective_ppi=min(im.width/(dw/72),im.height/(dh/72))
   group_height=dh+gap+text_height
   group_bottom=y+(h-group_height)/2
   c.drawImage(ImageReader(im),x+(w-dw)/2,group_bottom+text_height+gap,width=dw,height=dh,mask='auto')
   c.setFillColor(HexColor('#183e49'))
   ascent=pdfmetrics.getAscent('Card')/1000*12
   base=group_bottom+text_height-ascent
   for k,line in enumerate(lines):
    t=c.beginText();t.setFont('Card',12);t.setHorizScale(hs)
    t.setTextOrigin(x+w/2-pdfmetrics.stringWidth(line,'Card',12)*hs/200,base-k*line_height)
    t.textOut(line);c.drawText(t)
   stats.append({'id':idx,'lines':len(lines),'horizontal_scale':round(hs,1),'pixels':im.size,'effective_ppi':round(effective_ppi), 'needs_higher_resolution':effective_ppi<300})
   c.setStrokeColor(HexColor('#8d999b'));c.setLineWidth(.35)
   for xx in (x,x+w):
    for yy in (y,y+h):
     dx=-1 if xx==x else 1;dy=-1 if yy==y else 1
     c.line(xx+dx*.2*mm,yy,xx+dx*.8*mm,yy);c.line(xx,yy+dy*.2*mm,xx,yy+dy*.8*mm)
  c.showPage()
 c.save();return stats
if __name__=='__main__':
 out=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else ROOT/'Board_game_150_expressions.pdf'
 ids=[item['id'] for item in manifest]
 if len(ids)!=len(set(ids)): raise ValueError('Duplicate card IDs')
 stats=build(manifest,out,'150 expressions françaises - Cartes illustrées')
 (ROOT/'layout_checks.json').write_text(json.dumps(stats,indent=2))
 print(out);print('Cards:',len(stats),'pages:',math.ceil(len(stats)/10),'min horizontal scale:',min(s['horizontal_scale'] for s in stats))

