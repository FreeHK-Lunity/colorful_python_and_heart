from colorama import  Back, Style
# https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
import re
import time

color1 = '\033[38;2;255;0;0m'
color1 = '\033[38;2;255;0;0m'
color3 = '\033[38;2;255;255;0m'
color4 = '\033[38;2;0;255;255m'

def brighter(color):
  r, g, b = [int(c) for c in color[7:-1].split(';')]
  r = min(r + 50, 255)
  g = min(g + 50, 255)
  b = min(b + 50, 255)
  return f"\033[38;2;{r};{g};{b}m"

def darker(color, gradient):
  r, g, b = [int(c) for c in color[7:-1].split(';')]
  r = max(int(r - (r * gradient)), 0)
  g = max(int(g - (g * gradient)), 0)
  b = max(int(b - (b * gradient)), 0)
  return f"\033[38;2;{r};{g};{b}m"



def smd(color1,color3,color4):
  print(color1)
  print(color3)
  print(color4)
  heart_py = f'''














              {color1}******       ******                    {color3}.::::::::::.                                        
            {color1}**********   **********                {color3}.::``::::::::::.  
          {color1}************* *************              {color3}:::..::::::::::: 
        {color1}*****************************             {color3}````````::::::::
         {color1}*****************************     {color3}.::::::::::::::::::::::: {color4}iiiiiii,
         {color1}*****************************   {color3}.:::::::::::::::::::::::::: {color4}iiiiiiiii. 
          {color1}***************************    {color3}::::::::::::::::::::::::::: {color4}iiiiiiiiii 
            {color1}***********************      {color3}::::::::::::::::::::::::::: {color4}iiiiiiiiii
              {color1}*******************        {color3}:::::::::: {color4},,,,,,,,,,,,,,,,,iiiiiiiiii 
                {color1}***************          {color3}:::::::::: {color4}iiiiiiiiiiiiiiiiiiiiiiiiiii   
                  {color1}***********            {color3}`::::::::: {color4}iiiiiiiiiiiiiiiiiiiiiiiiii` 
                    {color1}*******                {color3}`:::::: {color4}iiiiiiiiiiiiiiiiiiiiiii`   
                      {color1}***                         {color4} iiiiiiii,,,,,,,,   
                       {color1}*                           {color4}iiiiiiiiiii''iii 
                                                   {color4}`iiiiiiiiii..ii`
                                                     {color4}`iiiiiiiiii`
                                                     \033[0m
  '''
  return heart_py




list_color_R = [color1,darker(color1,.25), darker(color1,.50), darker(color1,.75),darker(color1,.75), darker(color1,.50), darker(color1,.25),color1]
list_color_Y = [color3,darker(color3,.25), darker(color3,.50), darker(color3,.75),darker(color3,.75), darker(color3,.50), darker(color3,.25),color3]
list_color_B = [color4,darker(color4,.25), darker(color4,.50), darker(color4,.75),darker(color4,.75), darker(color4,.50), darker(color4,.25),color4]



# for i in list_color_B:
#   print(i)
#   print(f"{i}Hello World")
#   time.sleep(0.5)
# print(smd(color1,color3,color4))

while True:
  for item1, item2, item3 in zip(list_color_R, list_color_Y, list_color_B):
    print(smd(item1,item2,item3))
    time.sleep(0.5)

# print(heart_py)
'''

            .::::::::::.                                   
          .::``::::::::::.                                 
          :::..:::::::::::                                 
          ````````::::::::                                 
  .::::::::::::::::::::::: iiiiiii,                        
.:::::::::::::::::::::::::: iiiiiiiii.                      
::::::::::::::::::::::::::: iiiiiiiiii                      
::::::::::::::::::::::::::: iiiiiiiiii                      
:::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii                      
:::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii                      
`::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`                      
  `:::::: iiiiiiiiiiiiiiiiiiiiiii`                         
          iiiiiiii,,,,,,,,                                 
          iiiiiiiiiii''iii                                 
          `iiiiiiiiii..ii`                                 
            `iiiiiiiiii` 




              ******       ******
            **********   **********
          ************* *************
         *****************************
         *****************************
         *****************************
          ***************************
            ***********************
              *******************
                ***************
                  ***********
                    *******
                      ***
                       *

            
              ******       ******                    .::::::::::.                                        
            **********   **********                .::``::::::::::.  
          ************* *************              :::..::::::::::: 
         *****************************             ````````::::::::
         *****************************     .::::::::::::::::::::::: iiiiiii,
         *****************************   .:::::::::::::::::::::::::: iiiiiiiii. 
          ***************************    ::::::::::::::::::::::::::: iiiiiiiiii 
            ***********************      ::::::::::::::::::::::::::: iiiiiiiiii
              *******************        :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii 
                ***************          :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii   
                  ***********            `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii` 
                    *******                `:::::: iiiiiiiiiiiiiiiiiiiiiii`   
                      ***                          iiiiiiii,,,,,,,,   
                       *                           iiiiiiiiiii''iii 
                                                   `iiiiiiiiii..ii`
                                                     `iiiiiiiiii`
'''


'''
Here is a list of values that you can try:
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''