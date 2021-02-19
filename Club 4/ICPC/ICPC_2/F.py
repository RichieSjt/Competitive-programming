word = input()
scorep1 = 0
wp1 = 0
scorep2 = 0
wp2 = 0
flip = False
win = False

for char in word:
    if not win:
        if char == "S":
            if flip:
                scorep2 += 1
            else:
                scorep1 += 1
        
        if char == "R":
            flip = not flip
            if flip:
                scorep2 += 1
            else:
                scorep1 += 1

        ############################
        #       Score check        #
        ############################
        if scorep1 == 10 or scorep2 == 10:
            if scorep1 == 10:
                wp1 += 1
                #Reset points
                scorep1 = 0
                scorep2 = 0
            elif scorep2 == 10:
                wp2 += 1
                #Reset points
                scorep1 = 0
                scorep2 = 0
        elif scorep1 >= 5 or scorep2 >= 5:
            if (scorep1 - scorep2) >= 2:
                wp1 += 1
                #Reset points
                scorep1 = 0
                scorep2 = 0
            elif (scorep2 - scorep1) >= 2:
                wp2 += 1
                #Reset points
                scorep1 = 0
                scorep2 = 0
        ############################
        #       Score check        #
        ############################
            
        if char == "Q":
            if wp1 < 2 and wp2 < 2:
                print(str(wp1), "(" + str(scorep1) + ("*" if not flip else "") + ")", 
                        "-", str(wp2), "(" + str(scorep2) + ("*" if flip else "")+ ")")
            else:
                if wp1 == 2 :
                    print ("2 (winner) -", wp2)
                    win = True
                elif wp2 == 2:
                    print (wp1, "- 2 (winner)")
                    win = True