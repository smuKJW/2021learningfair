def cal(no,menu,toping):
    print("번호표는 %d번입니다~" % no)
    price1 = menud[int(menu)]
    price2 = topingd[int(toping)]
    price3 = price1+price2
    print('가격은' + str(price3) + '입니다')



menud = {1:3900, 2:4800, 3:6000,4:5100,5:4600,6:5500,7:6700,8:5800}
topingd = {1:600,2:600,3:1200,4:1000,5:700,6:0}


jumoon = 0
while True:
    jumoon = jumoon + 1
    print("========================================")
    print("어서오세요. 서브밀입니다~!")
    print(
"#############%#############%########################%%%#*+++========+**#%%%####################################################\n"
"#############%#############%#############%%######%#*+=====================+*%%#################################################\n"
"#############%##############%#############%####%*+============================*%%##############################################\n"
"#############%##############%############%%##%*==========+***######**+==========+%%#%##########################################\n"
"##############%############%%#############%%*========*#%@%%%%#######%%%%#*========+%%##########################%%%#############\n"
"###%%%#*****#%%#############%############%%+======+%@%%%%#############%##%%#*=======%%############%#%%%%#######.    +%#########\n"
"##%+.         :#%###*##%%###%%%%%%##%%%%%#======+@%%##%%%%%%%%######%%%%%%%%%@*======%%%%#########::::::%#####*     +%#########\n"
"#%              =%%=    =%##%::::=%#=+++*:=====#@%##%#**#**+++#%###%====:==*%::...        =%####%=      =%####+     .%#######%#\n"
"#:      **=      =%+    =%##%.    %+            .+%#%.         %%#%=       :@             +%####%        %%##%+     .%#######%#\n"
"#:      =*%@=.:..=@*    :@%%%:    %*    .++=.     +%%=         .@%#        .@.    #@%@@@@@%%%%%%=   .    =@%#%*     :%%%##%%###\n"
"##          .:*@@%%#    =@%%%+    %#    :@#*:     #%%:    .*    +@         .@     ...     %%##%#    %.    #%#%*     =%####%####\n"
"#%#.            =%%%    =@%%%*    %#            :@@%%:     @.    :    *     @             #%#%%    =@*     @%%*     :%%##%%####\n"
"##%@*:           .@%    :@%%%+    %#     ===.     .%@:     @%        *#     @     :+====++%##%.    ===     *%%*     :@%%%%%%%%#\n"
"#%%%@@@%*+.       +@     @%%@=    %#    .@@@@      :@.     @%+       @#     @     +%**####%%%+              @%+     .%###%%%%%#\n"
"#..    =@%%@+     =@=    .*+:    .@%     .         %@     .@%@:     @%@     @             :@@      .::.     *@+              *@\n"
"#       +##*.     %@@           :@%@          .:=#@%@. ...=@%%%=:::#@%@=:::.%.......      :@+     @%%%@.     %=              *%\n"
"#%.              #%#%%=      .=#@%#%*###%+=====#@%%#%%%%@%%%%%%%%%%%#%%%%%%%%%%======*@@%%%%*++++#%#####=:...+:              *%\n"
"#%%+           +@%###%%%%##%@%%%%%%#%%%%%%=======#%%%%#%%%%%%%%%%%%%%%%%##%%%+=====:*@%#####%%%%%%%#####%%%%%%######*******++#%\n"
"#%#%%%**+++*#%@%%#%###%#%%%%%%%%%%%%%%%%%%@*=======#%%%%%%%%%%%%%%%%#%%%%%#+=======%@%###########%%###########%%%%%%%%%%%%%%%%%\n"
"#%###%%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%%%%%%%%%+:======+#%%%%%%%%%%%%%%%%#+========#@%%############%%############%%#########%#%%%\n"
"#%#%#####%##%#%%#%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%*==========+**##****+==========*%@%%%%######%#####%%##########%%%%#%%%%%%%%%#%%%\n"
"#%#%%####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+========================*#@@%%##%%############%%#%#######%%%%%%%%%%%%%%%%%%%\n"
"#%%%#%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+=============++*#%@%%%##%%#%%############%%#%#%#%##%%%%%%#%%%%%%%%%%%%%\n"
"#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%%%####%%@@@@%#####%%%%%%%%##%#########%%#%#####%%%%%%%%%%%%%%%%%%%%%\n")


    a = int(input("주문을 원하시면 '1'을 입력해주세요."))

    if  a != 1 :
        break
    print()
    print("메뉴를 선택해주세요.")
    print()
    print('1. 브리또(3900\)\n'
          '2. 브리또+음료(4800\)\n'
          '3. 브리또+음료+감튀(6000\)\n'
          '4. 브리또+감튀(5100\)\n'
          '5. 점보 브리또(4600\)\n'
          '6. 점보+음료(5500\)\n'
          '7. 점보+음료+감튀(6700\)\n'
          '8. 점보+감튀(5800\)\n')
    print()
    menu = {'1': '브리또',
             '2': '브리또+음료',
             '3': '브리또+음료+감튀',
             '4': '브리또+감튀',
             '5': '점보 브리또',
             '6': '점보+음료',
             '7': '점보+음료+감튀',
             '8': '점보+감튀'}

    mymenu = input(str(list(menu.keys())) + "숫자로 선택해주세요.")
    
    print("세트<%s>번, <%s>를 선택하셨습니다." % (mymenu, menu[mymenu]))
    print()

    print("고기를 선택해주세요.")       
    print()
    print('1. 치킨\n'
          '2. 소고기\n'
          '3. 돼지갈비\n'
          '4. 치킨+소고기\n'
          '5. 치킨+돼지갈비\n'
          '6. 소고기+돼지갈비\n'
          '7. 소세지\n')
    print()

    meat = {'1': '치킨',
           '2': '소고기',
           '3': '돼지갈비',
           '4': '치킨+소고기',
           '5': '치킨+돼지갈비',
           '6': '소고기+돼지갈비',
           '7': '소세지'}

    mymeat = input(str(list(meat.keys())) + "숫자로 선택해주세요.")
    print("<%s>번, <%s>를 선택하셨습니다." % (mymeat, meat[mymeat]))
    print()


    print("매운맛의 정도를 선택해주세요.")
    print()
    print('1. 안 매운맛\n'
          '2. 약간 매운맛\n'
          '3. 매운맛\n'
          '4. 아주 매운맛\n'
          '5. 폭탄 매운맛\n')

    print()

    spicy = {'1': '안 매운맛',
             '2': '약간 매운맛',
             '3': '매운맛',
             '4': '아주 매운맛',
             '5': '폭탄 매운맛'}

    myspicy = input(str(list(spicy.keys())) + "숫자로 선택해주세요.")
    print("<%s>번, <%s>를 선택하셨습니다." % (myspicy, spicy[myspicy]))
    print()

    print("토핑을 선택해주세요.")
    print()
    print('1. 치즈1장(600\)\n'
          '2. 감자튀김(600\)\n'
          '3. 피자치즈(1200\)\n'
          '4. 새우튀김(1000\)\n'
          '5. 할라피뇨(700\)\n'
          '6. 선택 안 함(0\)\n')
    
    toping = {'1': '치즈1장',
              '2': '감자튀김',
              '3': '피자치즈',
              '4': '새우튀김',
              '5': '할라피뇨', 
              '6': '선택 안 함'}
    mytoping = input(str(list(toping.keys())) + "숫자로 선택해주세요.")
    print("<%s>번, <%s>를 선택하셨습니다." % (mytoping, toping[mytoping]))
    print()


    if mymenu == '1' or  mymenu == '4' or mymenu == '5' or mymenu == '8':
        cal(jumoon,mymenu,mytoping)      
                                                             
     
    else:
        print("음료를 선택해주세요.")
        print()
        print('1. 콜라\n'
              '2. 제로콜라\n'
              '3. 사이다\n'
              '4. 오렌지 환타\n'
              '5. 포도 환타\n')
        print()

        drink = {'1': '콜라',
                 '2': '제로콜라',
                 '3': '사이다',                 
                 '4': '오렌지 환타',
                 '5': '포도 환타'}
        mydrink = input(str(list(drink.keys())) + "숫자로 선택해주세요.")
        print("<%s>번, <%s>를 선택하셨습니다." % (mydrink, drink[mydrink]))
        cal(jumoon,mymenu,mytoping)

