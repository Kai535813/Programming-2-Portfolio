for bottles in range(99,-1,-1):

    if bottles > 2:
        print(bottles, "bottles of root beer on the wall,", bottles, "bottles of root beer. Take one down and pass it around,", bottles -1, "bottles of root beer on the wall," )
    elif bottles == 2:
        print(bottles, "bottles of root beer on the wall,", bottles, "bottles of root beer. Take one down and pass it around,", bottles -1, "bottle of root beer on the wall,")
        
    elif bottles == 1:
        print(bottles, "bottle of root beer on the wall,", bottles, "bottle of root beer. Take one down and pass it around, now there is no more beer on the wall!" )
    
    elif bottles <= 0:
        print("No more bottles of beer on the wall, no more bottles of beer, now you can stop drinking! YAY! ")