import random 
from termcolor import *
import pyfiglet





namecom=pyfiglet.figlet_format("BUIDING 262 (V 0,01)")
print(colored(namecom,color="yellow"))
print(colored('the MORFX Game',color="yellow"))
print('************************************')
print(colored('hello , wellcome to Building 262 game \n type start for run game or type help for game instructions ....',color="blue"))

rungame = input(colored('start or run / help / exit  :',color='red'))

if rungame == 'start' or rungame == 'run':
    print(colored('wellcome to the building 262 GAME ',color='blue'))
elif rungame == 'morfx':
    print('----------------------------')
    print(colored('Secret mood \n wow you are great \n ok but dont try again enter cheat cod :) \n ok end game see you later ;)',color='red'))
    print('----------------------------')
    input()
    exit()
elif rungame == 'help':
    print('************************************')
    print(colored('for select in a game 1 or 2 , just enter pg1 or playg1 and game 2 enter  pg2 or playg2  \n** cheat cod , just for game 1 and dont run to game 2 **\n Each stage has a certain score\n  Every 3 stages you will receive a key to go through the rest of the game\n  The keys can not be used in the last step\n  Use lowercase letters to write the answers \n write (help) at each step fpr quidance(except fpr the first stage(first question))',color='green'))
    print('************************************')
    input()
    exit()

elif rungame == 'exit':
    print(colored('see you later :)',color='red'))
    input()
    exit()

else:
    print(colored('just type start , come on run again',color='red'))
    input()
    exit()

# escape key

escapekey = []


# game cod
# score
score = 0

# menu
while(1):
    print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
    menu = input(colored('menu:\n play game 1(playg1 or pg1) / play game 2 (playg2 or pg2) \n creativ / write / exit : ',color='blue'))

    if menu == 'write':
        while(90):
            cheatpage = input()
            if cheatpage == 'keycheat':
                escapekey.append(1)
                escapekey.append(1)
                escapekey.append(1)
            
                continue
            elif cheatpage =='scorecheat':
                score+=100
                continue
            elif cheatpage =='exit' or cheatpage =='out':
                print("out cheat page ...")
                break
            else:
                print(colored('wrong!',color='red'))
                continue
    elif menu == 'playg2' or menu == 'pg2':


        while (1):
            name=input(colored('enter your name:',color='yellow'))

            number=random.randint(0,10)


            
            print(colored( f'hello {name} , you are stuck in room that has only one door and the code for that door is a number between 1 and 10 \n if you guess the code wrong , the room will explode \n otherwise you will survive ... ',color='blue'))
            print('****************************')
            print(colored('ok , now enter number ....',color='yellow'))


            guess_player=0

            while guess_player < 5:
                while(33):
                    try :
                        
                        usernumber=int(input(colored('--->',color='green')))
                    except ValueError :
                        print(colored('just type number ...',color='red'))
                        continue
                    else:
                        guess_player+=1
                        break
                

                if usernumber > number :
                    print(colored('the number entered is larger than the orgnal number ',color='blue'))
                elif usernumber < number :
                    print(colored('the number entered is smaller than the orgnal number ',color="green")) 
                elif usernumber == number:
                    break
                
            if usernumber == number:
                print(colored (f'the number of your efforts is {guess_player} and true number is {str (number)}',color='yellow'))
                print(colored('find true number and open the door now you free go :)',color='green'))
                break
            else:
                print(colored('the number of your attempts was excessive \n the room exploded :(',color='red'))
                print(colored(f'the number of your efforts is {guess_player} and true number is {str (number)}',color="yellow"))
                print(colored('you died ...',color='red'))
                break




    elif menu == 'playg1' or menu == 'pg1':
        print(colored('ok , lets go :)',color='blue'))
        break
    elif menu == 'creativ':
        print(colored('creat by :\n mohammad reza farjoo  ( *MORF X* )\n instagram:\n mmdfarjoo \n github :\n mmdfarjoo \n MORF X present',color='yellow'))
        continue
    elif menu == 'exit':
        print(colored('see you later :)',color='yellow'))
        exit()
        input()


print(colored('ok , answer the question and open the way ...',color='yellow'))

print('-----------------------------------------------')
# soal 1


print('----------------------')
print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
print('----------------------')




while(1):
    try:
        qone = int(input(colored(' 262 + 313 ?:',color='yellow')))

        if qone == 575:
            print(colored('easy , but good  lets go to two...',color='blue'))
            score += 1

        else:
            print(colored('the mistake ! ',color='blue'))
            score -= 1
        break
    except:
        print('just number ....')
        continue

# soal 2
while(3):

    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')
    qtwo = input(colored('the last season of the years ?:',color="yellow"))

    if qtwo == 'winter':
        print(colored('it was a good answer',color="blue"))
        score += 1
        break

    elif qtwo == 'help':
        print(colored('white seeds ',color="blue"))
        continue
    elif qtwo == 'key':
        if len(escapekey) == 0:
            print('----------------------')
            print('you dont have a key...')
            print('----------------------')
            continue
        else:
            print(colored('do not be so lazy :/',color="blue"))
            escapekey.pop()
            score += 1
            break

    else:
        print(colored('the mistake!',color="blue"))
        score -= 1
        break

# soal 3
while(4):
    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')
    qtree = input(colored('which door do you open ? Right or Left ?:',color="yellow"))
    if qtree == 'left' or qtree == 'l':
        print(colored(' oh , fine a key  \n you are very lucky',color="blue"))
        score += 1
        escapekey.append(1)
        break
    elif qtree == 'help':
        print(colored('you are lucky?',color="blue"))
        continue
    elif qtree == 'key':
        if len(escapekey) == 0:
            print('----------------------')
            print('you dont have a key...')
            print('----------------------')
            continue
        else:
            print(colored('you only need one chance :)',color="blue"))
            escapekey.pop()
            score += 1
            break
    else:
        print(colored('OH , luck was not with you:(',color="blue"))
        score -= 1
        break

# soal 4
while(5):
    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')
    charecter = {char for char in 'hello world'}
    print(colored(charecter,color="yellow"))
    qfour = input(colored('arrange the words and get the password...:',color="yellow"))
    if qfour == 'hello world':
        print(colored('nice',color="blue"))
        score += 1
        break
    elif qfour == 'help':
        print(colored('the first word printed in programming ...',color="blue"))
        continue
    elif qfour == 'key':
        if len(escapekey) == 0:
            print('----------------------')
            print('you dont have a key...')
            print('----------------------')
            continue
        else:
            print(colored('the answer is "hello world"',color="blue"))
            escapekey.pop()
            score += 1
            break
    else:
        print(colored('the mistake',color="blue"))
        score -= 1
        break

# soal 5
while(6):
    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')
    qfive = input('whats creator linux os first name ?')
    if qfive == 'bill gates' or qfive == 'linus':
        print(colored('easy ...',color="blue"))
        score += 1
        break
    elif qfive == 'help':
        print(colored('main rival bill gates',color="blue"))
        continue
    elif qfive == 'key':
        if len(escapekey) == 0:
            print('----------------------')
            print('you dont have a key...')
            print('----------------------')
            continue
        else:
            print(colored('the creator linux os first name is  /**linus**/',color="yellow"))
            escapekey.pop()
            score += 1
            break
    else:
        print(colored('the mistake',color="blue"))
        score -= 1
        break

# soal 6

while(7):
    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')
    qsix = input(
        colored('fine the password \n with each blow , a line comes down to me...:',color="yellow"))
    if qsix == 'enter':
        print(colored('very best...',color="blue"))
        score += 1
        escapekey.append(1)
        break

    elif qsix == 'help':
        print(colored('means to send ...',color="blue"))
        continue

    elif qsix == 'key':
        if len(escapekey) == 0:
            print('----------------------')
            print('you dont have a key...')
            print('----------------------')
            continue
        else:
            print(colored('the password is "enter"',color="blue"))
            escapekey.pop()
            score += 1
            break
    else:
        print(colored('the mistake',color="blue"))
        score -= 1
        break

# soal7

while(8):
    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')

    qseven = input(colored(
        'do you see a homeless person (A number is deducted from the key (-key)), help or not? y/n :',color="yellow"))

    if qseven == 'yes' or qseven == 'y':
        if len(escapekey) == 0:
            print('----------------------')
            print('you dont have a key...')
            print('----------------------')
            continue
        else:
            print(colored('gives you a piece of paper with a number written on it (1342)',color="blue"))
            escapekey.pop()
            score += 1
            break
    elif qseven == 'help':
        print(colored('helping the needy is a good thing :)',color="blue"))
        continue
    else:
        print(colored('ok ,, we continue on our way',color="blue"))
        break
# soal 8
while(9):
    print('----------------------')
    print(colored( f'you are key : {escapekey} and score :{score}',color='blue'))
    print('----------------------')
    qeight = int(input(colored('choose one of 5 doors:',color="yellow")))

    if qeight == 3:
        print(colored('arrange',color="blue"))
        charecter2 = {char for char in 'morfx'}
        print(colored("charecter2",color="yelloe"))
        qeightq = (input(colored('--->',color="blue")))
        if qeightq == 'morfx':
            print(colored('very good',color="blue"))
            score += 1
            break
        elif qeightq == 'help':
            print(colored('company creat :)',color="yellow"))
        elif qeightq == 'key':
            if len(escapekey) == 0:
                print('----------------------')
                print('you dont have a key...')
                print('----------------------')
                continue
            else:
                print(colored('the password is "morfx"',color="blue"))
                escapekey.pop()
                score += 1
                break
        else:
            print(colored('the mistake',color="blue"))
            score -= 1
            break

    elif qeight == 'help':
        print(colored('you should be lucky :)',color="blue"))
        continue
    elif qeight == 5:
        keycod = input(colored('enter the password:',color="yellow"))
        if keycod == 1342:
            print(colored('you know how to play well',color="blue"))
            score += 2
            break
        elif keycod == 'key':
            if len(escapekey) == 0:
                print('----------------------')
                print('you dont have a key...')
                print('----------------------')
                continue
            else:
                print(colored('the password is "1342"',color="blue"))
                escapekey.pop()
                score += 1
                break
        else:
            print(colored('the mistake',color="blue"))
            score -= 1
            break
    elif (qeight == 1 or qeight == 2) or qeight == 4:
        print(colored('ahhh , very unlucky',color="blue"))
        score -= 1
        break
    else:
        print(colored('just number 1 ,2 ,3 ,4 ,5 ',color="blue"))

# soal 9

print('----------------------')
print(colored( f'key : {escapekey} score :{score}',color='blue'))
print('----------------------')
print(colored('there are up to 10 wires\n but only (one) of these wires deactivates the bomb in the building \n the order of the wires is indicated by color \n you only have (1) chance \n you can not use the key :) ',color="yellow"))
print('----------------------')
print(colored('the color of the wires : \n yellow // orange // blue // green // red // \n purple // gray // cyan // brown// white //',color="yellow"))
while(10):
    qnine = input(colored('take on:',color="blue"))
    if qnine == 'yellow':
        print(colored('the bomb was defused \n you are free \n thank you for playing',color="yellow"))
        score += 1
        print(colored( f' score : {score}',color="yellow"))
        input()
        break

    elif qnine == 'help':
        print(colored('i can not do anything anymore :(',color="blue"))
        continue

    elif qnine == 'key':
        print(colored('you can not use the key at this stage',color="blue"))
        continue
    else:
        print(colored('oh no , you cut the wrong wire\n you were killed',color="yellow"))
        input()
        exit()




# If you are watching the game code now
# , if you want you can change it and increase the features
# , but
# , in the Creator section
# , keep my name and my company and add your name
# , thank you

# اگر کد های بازی را هم اکنون داری تماشا میکنی
# ، اگر میخواهی میتوانی در آن تغییر ایجاد کنی و امکانات‌ را افزایش دهی
# ، اما
# ، در قسمت خالق ، نام من و کمپانی من را همچنان نگهدار و نام خودت را اضافه کن
# ، ممنون
