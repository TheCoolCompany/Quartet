# This is a game of Cards
import random as r
Two0 = 2
Two1 = 2
Two2 = 2
Two3 = 2
Three0 = 3 
Three1 = 3
Three2 = 3
Three3 = 3
Four0 = 4
Four1 = 4
Four2 = 4
Four3 = 4
five0 = 5
five1 = 5
five2 = 5
five3 = 5
six0 = 6
six1 = 6
six2 = 6
six3 = 6
seven0 = 7
seven1 = 7
seven2 = 7
seven3 = 7
eight0 = 8
eight1 = 8
eight2 = 8
eight3 = 8
nine0 = 9
nine1 = 9
nine2 = 9
nine3 = 9
ten0 = 10
ten1 = 10
ten2 = 10
ten3 = 10
jack0 = 11
jack1 = 11
jack2 = 11
jack3 = 11
queen0 = 12
queen1 = 12
queen2 = 12
queen3 = 12
King0 = 12
King1 = 12
King2 = 12
King3 = 12
Ace0 = 13
Ace1 = 13
Ace2 = 13
Ace3 = 13
player1 = []
player2 = []

def shuffle(p):
    p = []
    doc = [Two0, Two1, Two2, Two3, Three0, Three1, Three2, Three3,Four0,Four1,Four2,Four3,five0,five1,five2,five3,six0,six1,six2,six3,seven0,seven1,seven2,seven3,eight0,eight1,eight2,eight3,nine0,nine1,nine2,nine3,ten0,ten1,ten2,ten3,jack0,jack1,jack2,jack3,queen0,queen1,queen2,queen3,King0,King1,King2,King3,Ace0,Ace1,Ace2,Ace3]
    x = r.randint(0, len(doc) - 1)
    for i in range(26):
        p.append(doc[x])
        del doc[x]
        x = r.randint(0, len(doc) - 1)
    return p
    
player1 = shuffle(player1)
player2 = shuffle(player2)

def play():
    i = 0 
    p = shuffle(player1)
    p1 = shuffle(player2)
    Tie = []
    T = False
    c = 0
    while p[i] != None and p1[i] != None:
        print("Round", c)
        print(len(p1), len(p))
        c += 1
        try:
            if p[i] < p1[i]:
                if T == False:
                    print("player1:", p[i], "player2", p1[i], "Player 1 has lost, Player 2 has won this round")
                    p1.append(p[i])
                    p1.append(p1[i])
                    p.pop(i)
                    p1.pop(i)
                else:
                    print("player1:", p[i], "player2", p1[i], "Player 1 has lost, Player 2 has won this round and the Tie")
                    p1.append(p[i])
                    p1.append(p1[i])
                    p1.extend(Tie)
                    p.pop(i)
                    p1.pop(i)
                    Tie.clear()
                    T = False
            elif p[i] > p1[i]:
                if T == False:
                    print("player1:", p[i], "player2", p1[i], "Player 2 has lost, Player 1 has won this round")
                    p.append(p[i])
                    p.append(p1[i])
                    p.pop(i)
                    p1.pop(i)
                else:
                    print("player1:", p[i], "player2", p1[i], "Player 2 has lost, Player 1 has won this round")
                    p.append(p[i])
                    p.append(p1[i])
                    p.extend(Tie)
                    p.pop(i)
                    p1.pop(i)
                    Tie.clear()
                    T = False
            elif p[i] == p1[i]:
                print("It was a tie get ready for the next round", p[i], p1[i])
                Tie.append(p[i])
                Tie.append(p1[i])
                T = True
                p.pop(i)
                p1.pop(i)
        except TypeError:
            if [] in p:
                p.remove([])
            else:
                p1.remove([])
    return p, p1

play()


print(player1, player2, len(player1))
