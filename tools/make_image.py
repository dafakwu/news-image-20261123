from PIL import Image, ImageDraw, ImageFont
import math
W=H=1024
im=Image.new('RGB',(W,H),'#F4F1E8'); d=ImageDraw.Draw(im)
NAVY='#10263A'; INK='#182A38'; MUTED='#465963'; RED='#C84D36'; GOLD='#E2B54B'; BLUE='#397A91'; GREEN='#477966'; WHITE='#FFFEFA'; LINE='#D6D2C8'
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; condensed='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def F(sz,b=True,cond=False): return ImageFont.truetype(condensed if cond else (font if b else regular),sz)
def txt(x,y,s,sz,fill=INK,b=True,cond=False): d.text((x,y),s,font=F(sz,b,cond),fill=fill)
# Masthead
d.rectangle((0,0,1024,136),fill=NAVY)
txt(30,13,'THE WORLD ON',19,'#D9E3E3')
txt(30,37,'MONDAY 23 NOVEMBER 2026',38,WHITE)
d.line((30,91,994,91),fill='#526878',width=2)
txt(31,101,'A DAY OF REVERSALS, PRESSURE & LOSS',15,'#D9E3E3',False)
# tile data
stories=[
('USA / TECH','NVIDIA REHIRES JENSEN HUANG','Board reversal lifts shares; founder returns.','chip'),
('EUROPE','EU: 22ND RUSSIA SANCTIONS PACKAGE','New measures target banks, crypto and tankers.','eu'),
('LIBYA / UKRAINE','UKRAINE DRONES HIT RUSSIAN SHIPS OFF LIBYA','Corvette sunk at Benghazi; Libya seeks UN probe.','ship'),
('CLIMATE','COP31 ENDS WITHOUT A DEAL','Fossil fuel dispute leaves island states dismayed.','earth'),
('MIDDLE EAST','IRAN VOWS TO FIGHT US BLOCKADE','Ship attacks in Strait of Hormuz at record pace.','tanker'),
('SECURITY / SPACE','REPORT: RUSSIA PLANS NUCLEAR SATELLITE','NATO raises alarm over a possible space weapon.','sat'),
('ASIA','INDONESIA FACTORY FIRE: 24 DEAD','Dozens remain missing after the factory blaze.','fire'),
('SOUTH ASIA','INDIA PLEDGES $1.62BN TO NEPAL','Flood recovery pledge comes during PM visit.','nepal'),
('LATIN AMERICA','MEXICO: 16 KILLED IN SINALOA','Clashes follow a major cartel arrest.','mexico')]
colors=[RED,'#315A82',RED,GREEN,'#A85A35','#59627B',RED,'#A67824','#477966']

def draw_icon(kind,cx,cy):
    # large, high contrast illustration field (~120 px tall)
    d.ellipse((cx-66,cy-53,cx+66,cy+53),fill='#E9EEF0')
    if kind=='chip':
        d.rounded_rectangle((cx-42,cy-35,cx+32,cy+35),radius=9,fill='#315A58',outline=INK,width=3)
        d.rounded_rectangle((cx-31,cy-23,cx+21,cy+23),radius=5,fill=GOLD,outline='#7A6227',width=2)
        txt(cx-28,cy-8,'NVIDIA',12,INK,True,True)
        for q in [-30,-10,10,30]:
            d.line((cx+q,cy-47,cx+q,cy-35),fill=INK,width=4); d.line((cx+q,cy+35,cx+q,cy+47),fill=INK,width=4)
        for q in [-22,0,22]:
            d.line((cx-54,cy+q,cx-42,cy+q),fill=INK,width=4); d.line((cx+32,cy+q,cx+54,cy+q),fill=INK,width=4)
        d.line((cx+40,cy-28,cx+53,cy-43),fill=RED,width=5); d.polygon([(cx+51,cy-50),(cx+56,cy-39),(cx+45,cy-41)],fill=RED)
    elif kind=='eu':
        d.ellipse((cx-48,cy-45,cx+48,cy+45),fill='#315A82',outline=WHITE,width=3)
        for a in range(0,360,30):
            px=cx+31*math.cos(math.radians(a)); py=cy+29*math.sin(math.radians(a)); d.regular_polygon((px,py,4),5,rotation=-90,fill=GOLD)
        d.rectangle((cx-24,cy+2,cx+24,cy+35),fill='#C6D1D5',outline=INK,width=3)
        d.polygon([(cx-29,cy+2),(cx,cy-17),(cx+29,cy+2)],fill='#788E97',outline=INK)
        d.rectangle((cx-10,cy+13,cx+10,cy+35),fill='#315A82')
        d.rounded_rectangle((cx-11,cy-13,cx+11,cy+8),radius=4,fill=RED,outline=WHITE,width=2)
        d.arc((cx-8,cy-26,cx+8,cy-5),180,360,fill=INK,width=4)
    elif kind=='ship':
        d.polygon([(cx-58,cy+8),(cx+57,cy+8),(cx+38,cy+35),(cx-38,cy+35)],fill='#344D60',outline=INK)
        d.rectangle((cx-23,cy-18,cx+25,cy+8),fill='#E8E5D9',outline=INK,width=2)
        d.rectangle((cx-9,cy-34,cx+10,cy-18),fill=RED,outline=INK,width=2)
        d.line((cx-58,cy+40,cx+58,cy+40),fill=BLUE,width=4)
        d.line((cx-53,cy+48,cx-25,cy+45,cx,cy+49,cx+25,cy+45,cx+53,cy+49),fill=BLUE,width=3)
        d.ellipse((cx+38,cy-43,cx+57,cy-25),outline=RED,width=4); d.line((cx+47,cy-25,cx+28,cy-6),fill=RED,width=4)
        d.ellipse((cx-50,cy-14,cx-35,cy-4),fill='#315A82'); d.polygon([(cx-47,cy-1),(cx-32,cy-1),(cx-35,cy+7),(cx-49,cy+7)],fill='#315A82')
        d.polygon([(cx+4,cy-3),(cx+11,cy-18),(cx+18,cy-4),(cx+27,cy+2),(cx+12,cy+1)],fill=WHITE)
    elif kind=='earth':
        d.ellipse((cx-45,cy-45,cx+45,cy+45),fill='#5B9A9B',outline=INK,width=3)
        d.polygon([(cx-29,cy-25),(cx-10,cy-33),(cx+1,cy-21),(cx-7,cy-9),(cx-21,cy-10)],fill='#477966')
        d.polygon([(cx+10,cy+1),(cx+31,cy-8),(cx+26,cy+18),(cx+9,cy+31),(cx+1,cy+18)],fill='#477966')
        d.line((cx-38,cy+3,cx-17,cy-2,cx-4,cy+8),fill=WHITE,width=4)
        # broken gavel and red rejection mark
        d.line((cx+10,cy-33,cx+36,cy-47),fill='#6F4736',width=7); d.line((cx+7,cy-38,cx+20,cy-26),fill=GOLD,width=9); d.line((cx+27,cy-53,cx+41,cy-39),fill=GOLD,width=9)
        d.line((cx+26,cy-27,cx+49,cy-4),fill=RED,width=6); d.line((cx+49,cy-27,cx+26,cy-4),fill=RED,width=6)
        txt(cx-25,cy+18,'COP31',12,WHITE,True,True)
    elif kind=='tanker':
        d.polygon([(cx-60,cy+12),(cx+60,cy+12),(cx+45,cy+34),(cx-42,cy+34)],fill='#344D60',outline=INK)
        d.rectangle((cx-26,cy-9,cx+33,cy+12),fill='#A85A35',outline=INK,width=2); d.rectangle((cx+26,cy-22,cx+43,cy+12),fill=WHITE,outline=INK,width=2)
        d.line((cx-66,cy+42,cx+66,cy+42),fill=BLUE,width=4)
        d.polygon([(cx-59,cy-35),(cx-32,cy-50),(cx-17,cy-35)],fill='#687B82'); d.polygon([(cx+20,cy-38),(cx+49,cy-53),(cx+64,cy-38)],fill='#687B82')
        d.polygon([(cx-2,cy-46),(cx+7,cy-31),(cx+2,cy-31),(cx+9,cy-14),(cx-8,cy-34),(cx-2,cy-34)],fill=GOLD,outline=RED)
    elif kind=='sat':
        d.rectangle((cx-19,cy-20,cx+19,cy+20),fill=GOLD,outline=INK,width=3)
        d.polygon([(cx-60,cy-26),(cx-25,cy-18),(cx-25,cy+18),(cx-60,cy+26)],fill='#527F99',outline=INK); d.polygon([(cx+25,cy-18),(cx+60,cy-26),(cx+60,cy+26),(cx+25,cy+18)],fill='#527F99',outline=INK)
        for q in [-42,-31,39,50]: d.line((cx+q,cy-21,cx+q,cy+21),fill='#9EC0CF',width=2)
        d.line((cx,cy-20,cx+15,cy-39),fill=INK,width=3); d.ellipse((cx+10,cy-46,cx+20,cy-36),fill=RED)
        # radiation trefoil on central body
        d.ellipse((cx-11,cy-11,cx+11,cy+11),fill=INK)
        for a in (90,210,330):
            p1=(cx+5*math.cos(math.radians(a)),cy+5*math.sin(math.radians(a))); p2=(cx+11*math.cos(math.radians(a-24)),cy+11*math.sin(math.radians(a-24))); p3=(cx+11*math.cos(math.radians(a+24)),cy+11*math.sin(math.radians(a+24))); d.polygon([p1,p2,p3],fill=GOLD)
        d.ellipse((cx-2,cy-2,cx+2,cy+2),fill=GOLD)
    elif kind=='fire':
        d.rectangle((cx-43,cy-6,cx+43,cy+36),fill='#687B82',outline=INK,width=3); d.polygon([(cx-50,cy-6),(cx,cy-31),(cx+50,cy-6)],fill='#394C57',outline=INK)
        for q in [-26,0,26]: d.rectangle((cx+q-7,cy+4,cx+q+7,cy+18),fill=GOLD,outline=INK,width=1)
        d.rectangle((cx-7,cy+18,cx+8,cy+36),fill='#344D60')
        d.polygon([(cx-18,cy-5),(cx-28,cy-22),(cx-17,cy-39),(cx-7,cy-20),(cx+1,cy-48),(cx+16,cy-22),(cx+13,cy-5)],fill=RED,outline='#8D3026')
        d.polygon([(cx-5,cy-7),(cx-9,cy-20),(cx,cy-33),(cx+8,cy-16),(cx+6,cy-7)],fill=GOLD)
        d.ellipse((cx+23,cy-49,cx+49,cy-36),fill='#7D8788'); d.ellipse((cx+34,cy-59,cx+59,cy-45),fill='#9AA2A1')
    elif kind=='nepal':
        d.polygon([(cx-57,cy+20),(cx-30,cy-22),(cx-13,cy+2),(cx+5,cy-46),(cx+31,cy+20)],fill='#547F86',outline=INK)
        d.polygon([(cx+1,cy+20),(cx+34,cy-25),(cx+62,cy+20)],fill='#426A76',outline=INK)
        d.polygon([(cx-36,cy-12),(cx-30,cy-22),(cx-23,cy-12)],fill=WHITE); d.polygon([(cx-1,cy-34),(cx+5,cy-46),(cx+12,cy-34)],fill=WHITE); d.polygon([(cx+27,cy-15),(cx+34,cy-25),(cx+41,cy-15)],fill=WHITE)
        d.polygon([(cx-60,cy+27),(cx-32,cy+22),(cx-7,cy+28),(cx+18,cy+22),(cx+61,cy+27),(cx+61,cy+45),(cx-60,cy+45)],fill='#4C8BA0')
        d.ellipse((cx-18,cy-5,cx+20,cy+33),fill=GOLD,outline='#8A6828',width=2); txt(cx-12,cy+1,'$',23,INK,True)
    else:
        # Mexico silhouette and location pin
        d.polygon([(cx-44,cy-43),(cx-14,cy-47),(cx+9,cy-35),(cx+19,cy-18),(cx+8,cy-3),(cx+20,cy+9),(cx+12,cy+27),(cx+1,cy+46),(cx-11,cy+30),(cx-15,cy+12),(cx-31,cy+4),(cx-48,cy-8)],fill='#5F8976',outline=INK)
        d.ellipse((cx-3,cy-35,cx+14,cy-18),fill=RED,outline=WHITE,width=2); d.polygon([(cx,cy-22),(cx+11,cy-22),(cx+4,cy-8)],fill=RED); d.ellipse((cx+2,cy-31,cx+9,cy-24),fill=WHITE)

# Rows are 270 px high, leaving a 12 px gutter and a 22 px date strip.
for i,(tag,head,sub,icon) in enumerate(stories):
    row,col=divmod(i,3); x=24+col*325; y=150+row*282; w=313; h=270
    d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=WHITE,outline=LINE,width=2)
    tag_w=min(210,d.textbbox((0,0),tag,font=F(12))[2]+18)
    d.rounded_rectangle((x+12,y+11,x+12+tag_w,y+37),radius=5,fill=colors[i]); txt(x+19,y+15,tag,12,WHITE)
    draw_icon(icon,x+w//2,y+91)
    # Fit every full requested headline onto two bold lines, starting at 32px.
    words=head.split(); max_w=w-28; head_size=30
    while True:
        lines=[]; line=''
        for word in words:
            trial=(line+' '+word).strip()
            if d.textbbox((0,0),trial,font=F(head_size,True,True))[2] > max_w:
                if line: lines.append(line)
                line=word
            else: line=trial
        if line: lines.append(line)
        if len(lines)<=2 or head_size<=18: break
        head_size-=1
    for j,l in enumerate(lines): txt(x+14,y+151+j*27,l,head_size,INK,True,True)
    # Keep supporting copy to two lines and readable at the 300px review size.
    sub_size=19; subfont=F(sub_size,False)
    words=sub.split(); sl=[]; line=''
    for word in words:
        trial=(line+' '+word).strip()
        if d.textbbox((0,0),trial,font=subfont)[2] > max_w:
            if line: sl.append(line)
            line=word
        else: line=trial
    if line: sl.append(line)
    if len(sl)>2:
        sub_size=18; subfont=F(sub_size,False); sl=[]; line=''
        for word in words:
            trial=(line+' '+word).strip()
            if d.textbbox((0,0),trial,font=subfont)[2] > max_w:
                if line: sl.append(line)
                line=word
            else: line=trial
        if line: sl.append(line)
    sub_y=y+218 if len(lines)==1 else y+218
    for j,l in enumerate(sl[:2]): txt(x+14,sub_y+j*22,l,sub_size,MUTED,False)
# Date footer strip
d.rectangle((0,1002,1024,1024),fill=NAVY)
txt(25,1004,'NINE STORIES  •  ONE MONDAY  •  23 NOVEMBER 2026',11,WHITE)
im.save('entry.png',format='PNG',optimize=True)
