#heihei123456780 2021/11/1
#扫雷
from random import randrange
def normalized(minefield,rolnumber,colnumber):#初始化雷区
    for i in range (0,rolnumber+3):
        minefield.append([])
        for j in range (0,colnumber+3):
            minefield[i].append([0,0])
            j=j+1
        i=i+1
def generatemine(minefield,minenumber,rolnumber,colnumber):#生成雷
    a=0
    while a<minenumber:
        x=randrange(1,rolnumber+2)
        y=randrange(1,rolnumber+2)
        if minefield[x][y][0]!=9:
           minefield[x][y][0]=9
           a=a+1
def check_neighbour_mine(minefield,rolnumber,colnumber):#计算周边雷数
    i,j=1,1
    for i in range (1,rolnumber+2):
        for j in range (1,colnumber+2):
            if minefield[i][j][0]!=9 :
                minefield[i][j][0]=(minefield[i-1][j-1][0]+minefield[i-1][j][0]+minefield[i-1][j+1][0]+minefield[i][j-1][0]+minefield[i][j+1][0]+minefield[i+1][j-1][0]+minefield[i+1][j][0]+minefield[i+1][j+1][0])//9
            j=j+1
        i=i+1
def display(minefield,rolnumber,colnumber):#显示雷区
    i,j=0,0
    for i in range (0,rolnumber+2):
        for j in range (0,colnumber+2):               
               if (i==0 or j==0 )and not(i==0 and j==0)and(i<11 and j<11):
                   print(i+j-1,"",end='|')
               elif (i==0 or j==0)and not(i==0 and j==0):
                   print(i+j-1,end='|')
               elif i==0 and j==0:
                   print("  ",end="|")
               else:
                   if minefield[i][j][1]==0: 
                       print(" ","",end='|')
                   elif minefield[i][j][1]==1:
                       if minefield[i][j][0]!=9:
                           print(minefield[i][j][0],"",end='|')
                       else:
                           print('*',"",end='|')
                   elif minefield[i][j][1]==2:
                       print('!',"",end='|')                     
               j=j+1
        else:
            print('')
        i=i+1
def dig(minefield,x,y,rolnumber,colnumber,first):#选择地块后的处理
    i,j=1,1
    global safe
    if minefield[x][y][0]==9 and minefield[x][y][1]!=2 :
        if first:
            minefield [x][y][0]=0
            for i in range (0,rolnumber+2):
                for j in range (0,colnumber+2):
                    if minefield [i][j][0]!=9:
                        minefield[i][j][0]=0
                    j=j+1
                i=i+1
            generatemine(minefield,1,rolnumber,colnumber)
            while minefield[x][y][0]==9:
                c=1
                d=1
                while minefield[c][d][0]!=9:
                    c=random.randrange(1,rolnumber+2)
                    d=random.randrange(1,rolnumber+2)
                minefield[c][d][0]=0
                generatemine(minefield,1,rolnumber,colnumber)        
            check_neighbour_mine(minefield,rolnumber-1,colnumber-1)
            minefield[x][y][1]=1
        else:
            for i in range (1,rolnumber+2):
                for j in range (1,colnumber+2):
                    minefield[i][j][1]=1
                    j=j+1
                i=i+1
            safe=False
    elif minefield[x][y][0]!=0 and minefield[x][y][1]!=2:
        minefield[x][y][1]=1
    elif minefield[x][y][0]==0 and minefield[x][y][1]==0 and not (x==0 or y==0 or x+1>rolnumber+1 or y+1>rolnumber+1)and minefield[x][y][1]!=2:
        minefield[x][y][1]=1
        dig(minefield,x+1,y+1,rolnumber,colnumber,False)
        dig(minefield,x+1,y,rolnumber,colnumber,False)
        dig(minefield,x+1,y-1,rolnumber,colnumber,False)
        dig(minefield,x,y+1,rolnumber,colnumber,False)
        dig(minefield,x,y-1,rolnumber,colnumber,False)
        dig(minefield,x-1,y+1,rolnumber,colnumber,False)
        dig(minefield,x-1,y,rolnumber,colnumber,False)
        dig(minefield,x-1,y+1,rolnumber,colnumber,False)
def check(minefield,minenumber,rolnumber,colnumber,count):#检查是否打开所有没有雷的格子
     i,j=1,1
     count=0
     for i in range (1,rolnumber+2):
        for j in range (1,colnumber+2):
            if minefield[i][j][1]==1:
                count=count+1
            j=j+1
        i=i+1
     if count==rolnumber*colnumber-minenumber:
        return True
     else:
        return False
def restart(minefield,rolnumber,colnumber):#重玩
    for i in range (0,rolnumber+2):
        for j in range (0,colnumber+2):
            minefield[i][j][1]=0
            j=j+1
        i=i+1

play='y'
while play=='y'or play=='r':
  safe=True
  first=False
  if play=='y':
      minefield=[]
      a=input('请输入雷区的行数与列数，二者用逗号分隔，且小于100 ')
      a=a.split(',')
      while True:
          try:
            while int(a[0])>100 or int(a[1])>100:
                print('请输入小于100的数')
                a=input('请输入雷区的行数与列数，二者用逗号分隔，且小于100 ')
                a=a.split(',')
            break
          except Exception:
               a=input('请输入雷区的行数与列数，二者用逗号分隔，且小于100 ')
               a=a.split(',')
      normalized(minefield,int(a[0])-1,int(a[1])-1)
      b=input('请输入雷数，必须小于雷区大小 ')
      while True:
        try:
          b=int(b)
          while b>(int(a[0]))*(int(a[1])):
              print('请输入小于雷区大小的雷数')
              b=int(input('请输入雷数，必须小于雷区大小 '))
          break
        except Exception:
              b=input('请输入雷数，必须小于雷区大小 ')
      generatemine(minefield,b,int(a[0])-1,int(a[1])-1)
      check_neighbour_mine(minefield,int(a[0])-1,int(a[1])-1)
      first=True
  display(minefield,int(a[0])-1,int(a[1])-1)
  while safe==True:
      d=0
      c=input('请输入要操作的行数与列数，以及要进行的操作（1=开挖，2=标记，3=开挖以输入坐标点为中心3x3范围内未标记的点,4=清除标记），用逗号分隔 ')
      c=c.split(',')
      while True:
          try:
             while int(c[0])>int(a[0])+2 or int(c[1])>int(a[1])+2 or int(c[2])>5:
                 print('输入超过范围')
                 c=input('请输入要操作的行数与列数，以及要进行的操作（1=开挖，2=标记，3=开挖以输入坐标点为中心3x3范围内未标记的点,4=清除标记,），用逗号分隔 ')
                 c=c.split(',')
             break
          except Exception:
                 c=input('请输入要操作的行数与列数，以及要进行的操作（1=开挖，2=标记，3=开挖以输入坐标点为中心3x3范围内未标记的点,4=清除标记,），用逗号分隔 ')
                 c=c.split(',')
      if int(c[2])==1:
          dig(minefield,int(c[0])+1,int(c[1])+1,int(a[0]),int(a[1]),first)
      elif int(c[2])==2:
          if minefield[int(c[0])+1][int(c[1])+1][1]==0:            
              minefield[int(c[0])+1][int(c[1])+1][1]=2
          else:
              print('不能标记已开挖或已标记的点')
      elif int(c[2])==4:
          minefield[int(c[0])+1][int(c[1])+1][1]=1
      elif int(c[2])==3:
          dig(minefield,int(c[0])+1,int(c[0])+1,int(a[0]),int(a[1]),first)
          dig(minefield,int(c[0])+2,int(c[0])+2,int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0])+2,int(c[0])+1,int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0])+2,int(c[0]),int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0])+1,int(c[0])+2,int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0])+1,int(c[0]),int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0]),int(c[0])+2,int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0]),int(c[0])+1,int(a[0]),int(a[1]),False)
          dig(minefield,int(c[0]),int(c[0]),int(a[0]),int(a[1]),False)
      display(minefield,int(a[0])-1,int(a[1])-1)
      if check(minefield,b,int(a[0]),int(a[1]),d):
         print('已清理所有地雷')
         break
      first=False
  else:
      print('踩雷了')
  play=input('是否继续游戏，继续游戏输入y，重玩输入r')
  if play=='r':
      restart(minefield,int(a[0]),int(a[1]))
