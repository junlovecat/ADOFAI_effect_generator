import sys
import os
def renameFilter(filterName):
    if filterName == 'VD':return 'VHS'
    if filterName == 'LED':return 'LED'
    if filterName == 'RAIN':return 'Rain'
    if filterName == 'BLI':return 'Blizzard'
    if filterName == 'PXS':return 'PixelSnow'
    if filterName == 'COM':return 'Compression'
    if filterName == 'PIX':return 'Pixelate'
    if filterName == 'WAV':return 'Waves'
    if filterName == 'STA':return 'Static'
    if filterName == 'GRA':return 'Grain'
    if filterName == 'MOT':return 'MotionBlur'
    if filterName == 'FIS':return 'Fisheye'
    if filterName == 'ABE':return 'Aberration'
    if filterName == 'DRA':return 'Drawing'
filename=input('type the name of the file> ')
if '.adofai' in filename:pass
else:filename+='.adofai'
tilenumber=input('tile number> ')
startoffset=input('starting angle> ')
finaloffset=input('final angle> ')
startvalue=input('start value> ')
endvalue=input('end value> ')
count=input('count> ')
filtername=input('''filtername
VHS LED Rain Blizzard Pixelsnow Compression Pixelate Waves Static Grain MotionBlur Fisheye Aberration Drawing
> ''')
t1=float(startoffset)
t2=float(finaloffset)
x1=float(startvalue)
x2=float(endvalue)
n=int(count)
f=open(filename,'rt',encoding='utf-8')
FILE=[]
while True:
    line=f.readline()
    if not line:break
    else:FILE.append(line)
for x in range(0,2):del FILE[len(FILE)-1]
strength=[]
angle=[]
for i in range(n):
    strength.append(x1+(x2-x1)*i/(n-1))
    angle.append(t1+(t2-t1)*i/(n-1))

FILE.append(f'\t\t{{ "floor": {tilenumber}, "eventType": "SetFilter", "filter": "{filtername}", "enabled": "Enabled", "intensity": {str(strength[0])}, "disableOthers": "Disabled", "angleOffset": {str(angle[0])}, "eventTag": "" }},\n')
for i in range(1, n):
    FILE.append(f'\t\t{{ "floor": {tilenumber}, "eventType": "SetFilter", "filter": "{filtername}", "enabled": "Enabled", "intensity": {str(strength[i])}, "disableOthers": "Disabled", "angleOffset": {str(angle[i])}, "eventTag": "" }},\n')
FILE.append('\t]\n')
FILE.append('}\n')
g=open('DONE.adofai', 'wt', encoding='utf-8')
g.write(''.join(FILE))
g.close()
print('Open DONE.adofai for final')
os.system('pause')
