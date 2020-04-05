def con_or_vow(ch) :

    if ( ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' ) :
        return 0
    else :
        return 1

def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0

    for i in range ( 0 , len(string) ) : 
        #print "Kevin ",kevin
        #print "Stuart ",stuart
        #print string[i]

        if ( not con_or_vow(string[i]) ) :
            kevin += ( len(string)-i )
        else :
            stuart += ( len(string)-i )
    
    if ( kevin > stuart ) :
        print "Kevin",kevin
    elif ( kevin < stuart ) :
        print "Stuart",stuart
    else :
        print "Draw"
