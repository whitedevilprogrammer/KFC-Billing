# billing for KFC
file = open('menu.txt','r+')
al = file.readlines()
Item = []
Price = []
p = 0
count = 0
for oneS in al:# item and prize pireekuthu! print menu
     print(oneS)

second_file = open('password.txt','r')
lines = second_file.readlines()
#print(lines[0])

while True:
     on = 0
     users = str(input('Enter your order :'))
     if users == 'stop':
          break
     if users == lines[0].strip() :#or 'ellalan'== lines[0].strip() :
          print('User name is Correct')
          user = str(input('Enter your Password :'))
          if user == lines[1].strip():# or 'ellalan14'== lines[1].strip():
               print('Your password is Correct !\nYou access to change menu item!')
                # this place create the addeding item or removing item ! with if condition
               print('Enter the Name \nadding item \nremoving item \nchange price only')
               change = str(input("Enter your options 'adding item or removing item or change price only':"))
               if change.strip().lower() == 'adding item':
                    print('Burgers\nChicken\nRice Bowlz\nSnacks\nDrinks')
                    checking = ['Burgers', 'Chicken', 'Rice Bowlz', 'Snacks', 'Drinks']
                    userc = str(input('which category you add the item for Menu: Enter name :'))
                    for w in checking:
                         #print('for loop 1')
                         # print('check',w.lower())
                         # print('user',user.strip().lower())
                         if userc.strip().lower() == w.strip().lower():
                              for p in range(len(checking)):
                                   try:
                                        if userc.strip().lower() == checking[p].lower():
                                             find = checking[p + 1]
                                             print(find)
                                             for a in range(len(al)):
                                                  print(al[a])
                                                  if find.lower() == al[a].strip().lower():
                                                       enter = str(input("you category '{}'Enter your adding item :".format(
                                                            userc.title())))
                                                       # if find.lower() == 'no':
                                                       # file.write('\n' + enter)
                                                       # break
                                                       enterp = str(input("Enter your Price Example(400.00):"))

                                                       al.insert(a, enter.title() + '     Rs ' + enterp.strip() + '\n')
                                                       files = open('menu.txt', 'w')
                                                       for l in al:
                                                            files.write(l)
                                                       files.close()
                                                       print('Successfully Added Your Item ')
                                                       break
                                             break

                                   except:
                                        print('except')
                                        enter = str(input(" you category '{}'Enter your adding item :".format(userc.title())))
                                        enterp = str(input("Enter your Price Example(400.00):"))
                                        file.write(enter.title() + '     Rs ' + enterp.strip() + '\n')
                                        print('Successfully Added Your Item ')
                                        break

                                   # print(al[a])
                              for b in range(len(al)):
                                   print(al[b])
                              break
                         if userc.strip().lower() != w.strip().lower():
                              print('Not available:{} This category for Menu'.format(userc.strip()))
                              break
               elif change.lower().strip() == 'removing item':
                    userR = str(input('Enter your removing item :'))
                    for oneS in al:  # item and prize pireekuthu!
                         # print(oneS)
                         for j in range(len(oneS)):
                              if oneS[j] == 'R':
                                   if oneS[j + 1] == 's':
                                        ok = oneS[:j].lower().strip().split('(', 1)
                                        if userR.lower().strip() == ok[0].strip():
                                             print('yes')
                                             al.remove(al[count])
                                             files = open('menu.txt', 'w')
                                             for l in al:
                                                  files.write(l)
                                             files.close()
                                             print('Successfully Removing Your Item')
                                             break

                         count += 1
               elif change.lower().strip() == 'change price only':
                    userR = str(input("Enter your 'Change price only' item name :"))
                    for oneS in al:  # item and prize pireekuthu!
                         # print(oneS)
                         for j in range(len(oneS)):
                              if oneS[j] == 'R':
                                   if oneS[j + 1] == 's':
                                        ok = oneS[:j].lower().strip().split('(', 1)
                                        if userR.lower().strip() == ok[0].strip():
                                             change1 = str(input("Item name : '{}' Enter Change the price Example(400.00):".format(userR)))
                                             print('yes',oneS[j + 2:].strip())
                                             #print(oneS[:j])
                                             al.insert(count,oneS[:j] + 'Rs ' +  change1 + '\n')
                                             al.pop(count + 1)
                                             for oneS in al:  # item and prize pireekuthu! print menu
                                                  print(oneS)
                                             files = open('menu.txt', 'w')
                                             for l in al:
                                                  files.write(l)
                                             files.close()
                                             userR = 'jjjjj'
                                             break

                         count += 1
          else:
               print('Your password is Worng !')
     if users == lines[0].strip():
          break

     for oneS in al:# item and prize pireekuthu!
          #print(oneS)
          for j in range(len(oneS)):
               if oneS[j] == 'R':
                    if oneS[j+1]== 's':
                         ok = oneS[:j].lower().strip().split('(',1)
                         if users.lower().strip() == ok[0].strip():
                              Item.append(users)
                              Price.append(float(oneS[j+2:]))
                              p += float(oneS[j+2:-1])
                              on = 1
     if on == 0:
          print(users,'This object is not in menu list or empty')

def bill():
     s = ' '
     print('')
     print('Your Bill')
     print('----------------------------------------------')
     print('---------------------KFC----------------------')
     print('Item                                     price')
     for count in range(len(Item)):
          n = (-len(Item[count]))+46
          n = (n - len(str(Price[count]))) - 3
          print(Item[count],s*n,"{:.2f}".format(Price[count]))
     m = -5 + 46
     m = (m - len(str(p))) - 3
     print('----------------------------------------------')
     print('Total',s*m,"{:.2f}".format(p))
     print('----------------------------------------------')
if users != lines[0].strip():
     bill()
file.close()
