# -*- coding: utf-8 -*-
import random
import sys
def dice(min,max):
    return random.randint(min,max)
    
min=1
max=6
menashi=0


player=int(input('プレイヤー数を入力してください:'))
score=[0]*player
parent=1
print('プレイヤー%sが親です。'%parent)


for i in range(player):
    turn=i+1
    print('プレイヤー%sの人がサイコロを振ります。'%turn)
    while True:
        dice_roll1=dice(min,max)
        print('1個目の目:%s'%dice_roll1)
        dice_roll2=dice(min,max)
        print('2個目の目:%s'%dice_roll2)
        dice_roll3=dice(min,max)
        print('3個目の目:%s'%dice_roll3)
        print('です。')

        if dice_roll1==1 and dice_roll2==1 and dice_roll3==1:
            print('役:ピンゾロ')
            score[i]=13
            if(turn==parent):
                print('親の即勝ちです')
                sys.exit()
            else:
                break
             
        elif dice_roll1==dice_roll2 and dice_roll2==dice_roll3:
            print('役:アラシ')
            score[i]=7+dice_roll1
            break

        elif dice_roll1==dice_roll2 or dice_roll2==dice_roll3 or dice_roll3==dice_roll1:
            if dice_roll1==dice_roll2:
                print('役:デメ%s'%dice_roll3)
                score[i]=dice_roll3
                break
            elif dice_roll2==dice_roll3:
                print('役:デメ%s'%dice_roll1)
                score[i]=dice_roll1
                break
            else:
                print('役:デメ%s'%dice_roll2)
                score[i]=dice_roll2
                break

        elif dice_roll1+dice_roll2+dice_roll3==15:
            print('役:シゴロ')
            score[i]=7
            if(turn==parent):
                print('親の即勝ちです')
                sys.exit()
            else:
                break

        elif dice_roll1+dice_roll2+dice_roll3==6:
            print('役:ヒフミ')
            score[i]=-1
            if(turn==parent):
                print('親の即負けです')
                sys.exit()
            else:
                break

        else:
            print('役:クズ')
            menashi=menashi+1
            if menashi==3:
                print('メナシ')
                score[i]=0
                menashi=0
                if(turn==parent):
                    print('親の即負けです')
                    sys.exit()
                else:
                    break
            else:
                print('もう一回サイコロを振ります。')

                
    if(turn!=parent):
        if(score[i]==score[parent-1]):
            print('引き分けです')
        elif(score[i]<score[parent-1]):
            print('親の勝ちです')
        else:
            print('プレイヤー%sの勝ちです'%turn)
