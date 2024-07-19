_NULL = ''

_COLON = """




::::::
::::::
::::::



::::::
::::::
::::::


"""
_ZERO = """ 
     0000000000     
   00::::::::::00   
 00::::::::::::::00 
0:::::::0000:::::::0
0::::::0    0::::::0
0:::::0      0:::::0
0:::::0      0:::::0
0:::::0 0000 0:::::0
0:::::0 0000 0:::::0
0:::::0      0:::::0
0:::::0      0:::::0
0::::::0    0::::::0
0:::::::0000:::::::0
 00::::::::::::::00 
   00::::::::::00   
     0000000000    
"""

_ONE = """
    11111111111    
   1::::::::::1    
  1:::::::::::1    
 111111:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1    
      1:::::::1   
  11111:::::::11111 
  1:::::::::::::::1 
  11111111111111111 
"""

_TWO = """
 222222222222222    
2:::::::::::::::22  
2::::::222222:::::2 
2222222     2:::::2 
            2:::::2 
            2:::::2 
         2222::::2  
    22222::::::22   
  22::::::::222     
 2:::::22222        
2:::::2             
2:::::2             
2:::::2       222222
2::::::2222222:::::2
2::::::::::::::::::2
22222222222222222222
"""

_THREE = """
 3333333333333333   
3::::::::::::::::33 
3::::::333333::::::3
3333333      3:::::3
             3:::::3
             3:::::3
    333333333:::::3 
    3::::::::::::3  
    333333333:::::3 
             3:::::3
             3:::::3
             3:::::3
3333333      3:::::3
3::::::333333::::::3
3::::::::::::::::33 
 3333333333333333  
 """

_FOUR = """
        444444444  
       4::::::::4  
      4:::::::::4  
     4::::44::::4  
    4::::4 4::::4  
   4::::4  4::::4  
  4::::4   4::::4  
 4::::444444::::4444
 4:::::::::::::::::4
 4444444444:::::4444
           4::::4  
           4::::4  
           4::::4  
        444::::::444
        4::::::::::4
        444444444444
"""

_FIVE = """
5555555555555555555 
5:::::::::::::::::5 
5:::::::::::::::::5 
5:::::5555555555555 
5:::::5             
5:::::5             
5:::::55555555555   
5::::::::::::::::5  
5555555555555:::::5 
             5:::::5
             5:::::5
5555555      5:::::5
5::::::555555::::::5
 55::::::::::::::55 
   55::::::::::55   
     5555555555   
"""

_SIX = """
         66666666   
        6::::::6    
       6::::::6     
      6::::::6      
     6::::::6       
    6::::::6        
   6::::::6         
  6::::::::66666    
 6::::::::::::::66  
 6::::::66666:::::6 
 6:::::6     6:::::6
 6:::::6     6:::::6
 6::::::66666::::::6
  66:::::::::::::66 
    66:::::::::66   
      666666666     
"""

_SEVEN = """
77777777777777777777
7::::::::::::::::::7
7::::::::::::::::::7
777777777777:::::::7
           7::::::7 
          7::::::7  
         7::::::7   
        7::::::7    
       7::::::7     
      7::::::7      
     7::::::7       
    7::::::7        
   7::::::7         
  7::::::7          
 7::::::7           
77777777          
"""

_EIGHT = """
     8888888888     
   88::::::::::88   
 88::::::::::::::88 
8::::::888888::::::8
8:::::8      8:::::8
8:::::8      8:::::8
 8:::::888888:::::8 
  8::::::::::::::8  
 8:::::888888:::::8 
8:::::8      8:::::8
8:::::8      8:::::8
8:::::8      8:::::8
8::::::888888::::::8
 88::::::::::::::88 
   88::::::::::88   
     8888888888    
"""

_NINE = """
      999999999     
    99:::::::::99   
  99:::::::::::::99 
 9::::::99999::::::9
 9:::::9     9:::::9
 9:::::9     9:::::9
  9:::::99999::::::9
   99::::::::::::::9
     99999::::::::9 
          9::::::9  
         9::::::9   
        9::::::9    
       9::::::9     
      9::::::9      
     9::::::9       
    99999999       
"""

NUMBERS_DICT = {
    '1': _ONE, '2': _TWO, '3': _THREE,
    '4': _FOUR, '5': _FIVE, '6': _SIX,
    '7': _SEVEN, '8': _EIGHT, '9': _NINE,
    'null': _NULL, '0': _ZERO, ':': _COLON,
}