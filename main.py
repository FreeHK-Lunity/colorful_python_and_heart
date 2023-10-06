from colorama import  Back, Style
# https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
print(Back.GREEN + 'The text with Green background')
print(Style.DIM + 'The text is DIM now')
pause = input("Press any key to continue...")
print(Style.RESET_ALL)
color1 = '\033[91m'  # Red
color2 = '\033[94m'  # Blue
reset_color = '\033[0m'  # Reset to default color
color3 = '"\u001b[33m' # Yellow
color4 = '"\u001b[34m' # Blue

# Create the string with two distinct colors
text = f"{color1}Hello {color2}world!{reset_color}"
print(text)
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
'''
print
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