




print("""                                                                                        

      .-------------------.
     /--"--.------.------/|
     |Kodak|__Ll__| [==] ||
     |     | .--. | "'"" ||
     |     |( () )|      ||
     |     | `--' |      |/
     `-----'------'------'

 ___      ___   _______  __   __  _______    __   __  _______  _______  _______  ______   
|   |    |   | |       ||  | |  ||       |  |  |_|  ||       ||       ||       ||    _ |  
|   |    |   | |    ___||  |_|  ||_     _|  |       ||    ___||_     _||    ___||   | ||  
|   |    |   | |   | __ |       |  |   |    |       ||   |___   |   |  |   |___ |   |_||_ 
|   |___ |   | |   ||  ||       |  |   |    |       ||    ___|  |   |  |    ___||    __  |
|       ||   | |   |_| ||   _   |  |   |    | ||_|| ||   |___   |   |  |   |___ |   |  | |
|_______||___| |_______||__| |__|  |___|    |_|   |_||_______|  |___|  |_______||___|  |_|
         

""")

def helpText(helpChoice):    
    if helpChoice == 1:
        print("\n\n")
        print("-" * 70)
        print("Step 1: Choose your current lighting. ")
        print("Step 2: Choose your ISO settings.")
        print("Step 3: Program will display ideal settings.")
        print("Step 4: You can choose to change the Aperture or Shutter Speed \n        setting and re calculate results.")
        print("-" * 70)
        print("\n\n")
        
    elif helpChoice == 2:
        print("""  _____  _____  ____  
 |_   _|/ ____|/ __ \ 
   | | | (___ | |  | |
   | |  \___ \| |  | |
  _| |_ ____) | |__| |
 |_____|_____/ \____/ 
                      """)
        print("\nISO in photography refers to the sensitivity of your camera's sensor to light.\n\nA lower ISO number indicates lower sensitivity,\nmeaning the sensor requires more light to produce a properly exposed image.\nConversely, a higher ISO number indicates higher sensitivity, allowing the sensor to capture images in \nlower light conditions but potentially introducing more digital noise or graininess to the photo.\n\nPhotographers often adjust ISO settings based on the available light and desired image quality.\n\n")            
                      
    elif helpChoice == 3:
        print("""
                               _                     
     /\                       | |                    
    /  \    _ __    ___  _ __ | |_  _   _  _ __  ___ 
   / /\ \  | '_ \  / _ \| '__|| __|| | | || '__|/ _ \ 
  / ____ \ | |_) ||  __/| |   | |_ | |_| || |  |  __/
 /_/    \_\| .__/  \___||_|    \__| \__,_||_|   \___|
           | |                                       
           |_|                                       
""")
        print("Aperture in photography refers to the opening in the lens through\nwhich light passes to reach the camera's sensor or film.\n\nThe aperture is measured in f-stops, denoted by numbers\nsuch as f/2.8, f/4, f/5.6, and so on.\nA lower f-stop number represents a larger aperture opening,\nallowing more light to enter the camera,\n\nA higher f-stop number indicates a smaller aperture opening,\nletting in less light.\n\nIn addition to controlling the amount of light,\nthe aperture also influences depth of field.\nA wider aperture (lower f-stop number) creates a shallow depth of field,\nwhere only a small portion of the image is in focus while the background is blurred\nA smaller aperture (higher f-stop number) creates a deeper depth of field,\nresulting in more of the scene being in focus.\n\n")
    elif helpChoice == 4:
        print("""
   _____  _             _    _                 _____                         _ 
  / ____|| |           | |  | |               / ____|                       | |
 | (___  | |__   _   _ | |_ | |_  ___  _ __  | (___   _ __    ___   ___   __| |
  \___ \ | '_ \ | | | || __|| __|/ _ \| '__|  \___ \ | '_ \  / _ \ / _ \ / _` |
  ____) || | | || |_| || |_ | |_|  __/| |     ____) || |_) ||  __/|  __/| (_| |
 |_____/ |_| |_| \__,_| \__| \__|\___||_|    |_____/ | .__/  \___| \___| \__,_|
                                                     | |                       
                                                     |_|                       
""")
        print("Shutter speed in photography refers to the amount of time that the camera's shutter remains open\nto allow light to reach the camera's sensor or film.\n\nShutter speed is typically measured in fractions of a second,\nsuch as 1/100, 1/250, or 1/1000 of a second,\nalthough longer exposures in seconds or even minutes are also possible.\n\nA fast shutter speed (e.g., 1/1000 or faster) captures fast-moving subjects without blurring,\nA slow shutter speed (e.g., 1/30 or slower) can create motion blur.\n\n")

def helpMenu():
    print("\nWhat do you want to learn about? ")
    print("1. Program Usage")
    print("2. ISO")
    print("3. Aperture")
    print("4. Shutter Speed \n")
    helpChoice = getUserInput("Enter your choice: ", 4)
    helpText(helpChoice)

def getUserInput(prompt,limit):
    valid = True
    while valid:
        print("Press 'm' to return to Main Menu.")
        userInput = input(prompt)   
        if userInput.isdigit():
        
            userInput = int(userInput)
            if userInput > 0 and userInput <= limit:
                valid = False
            else:
                print("Option does not exist! \n")
                
        elif userInput == 'm':
            valid = False
        else:
            print("Please enter a valid option! \n")            
    return userInput          
    
    
    
    
def chooseLighting():
    print("\n")
    print("1.  Bright full sun, no clouds. Objects cast shadows with sharp edges")
    print("2.  Slight overcast, still bright, Shadows with soft edges")
    print("3.  Overcast. Diffused light. Shadows have barely detectable edges")
    print("4.  Heavy overcast. Objects cast barely visible shadows")
    
    print("5.  Not bright not dark")
    print("6.  Greyish sky")
    
    print("7.  Rainy Day with solid grey sky")
    print("8.  Dark thunder clouds")
    
    print("9.  Well lit indoor area")
    print("10. Typical indoor lighting ")
    print("11. Dimly lit indoor lighting")
    
    print("12. Streets at night\n")
    choice = getUserInput("Choose the option that best represents your lighting: ",12)
    return choice
  



  
def setISO():
    print("\n")
    ISO = getUserInput("Enter your ISO: ", 1600)
    return ISO

def get_nearest_shutter_speed_index(iso_value):
    shutter_speeds = [1, 2, 4, 8, 15, 30, 60, 125, 250, 500, 1000]

    nearest_diff = float('inf')
    nearest_index = None

    for i in range(len(shutter_speeds)):
        speed = shutter_speeds[i]
        diff = abs(speed - iso_value)
        if diff < nearest_diff:
            nearest_diff = diff
            nearest_index = i
    
    return shutter_speeds, nearest_index

def ShutterSpeedSelection():
    print("\n")
    print("1. 1")
    print("2. 1/2")
    print("3. 1/4")
    print("4. 1/8")
    print("5. 1/15")
    print("6. 1/30")
    print("7. 1/60")
    print("8. 1/125")
    print("9. 1/250")
    print("10. 1/500")
    print("\n")
    ssChoice = getUserInput("Enter you shutter speed: ",10)
    ssIndex = ssChoice - 1 
    return ssIndex
    
def ApertureSelection():
    print("1. f2")
    print("2. f2.8")
    print("3. f4")
    print("4. f5.6")
    print("5. f8")
    print("6. f11")
    print("7. f16")
    apertureChoice = getUserInput("Enter your Aperture: ", 7)
    aIndex = apertureChoice  - 1 
    return aIndex 

def calculateSetting(light,ISO):

    shutter, index = get_nearest_shutter_speed_index(ISO)
    apertureList = [2, 2.8, 4, 5.6, 8, 11, 16, 22]
    print("\n\n")
    print("-" * 40)
    if light == 1:
        aperture = 6
        
    elif light == 2:
        aperture = 5
        
    elif light == 3:
        aperture = 4 
        
    elif light == 4:
        aperture = 3   
        
    elif light == 5:
        aperture = 3  
        index -= 1
        
    elif light == 6:
        aperture = 2  
        index -= 1   
        
    elif light == 7:
        aperture = 2
        index -= 2        
        
    elif light == 8:
        aperture = 2
        index -=3         
        
    elif light == 9:
        aperture = 1  
        index -=3  
        
    elif light == 10:
        aperture = 1  
        index -=4        
        
    elif light == 11:
        aperture = 1  
        index -=5        
        
    elif light == 12:
        aperture = 1  
        index -=6     
        
    if index < 0:
        print("\n\nTOO DARK!")
    elif index > len(shutter):
        print("\n\nTOO BRIGHT!")
        
    else:
        print(f"ISO:                {ISO}")    
        print(f"Aperture:           f{apertureList[aperture]}")
        print(f"Shutter speed:      1/{shutter[index]}")
   
    print("-" * 40)
    print("\n\n")
        
    menuChoice = ''
    while menuChoice != 'm':        
        print("1. Set Shutter Speed")
        print("2. Set Aperture \n")
        
        menuChoice = getUserInput("Enter your next action: ",2)
        print("\n\n")    
        if menuChoice == 1:
            ssIndex = ShutterSpeedSelection()
            ssStop = ssIndex - index
            if aperture - ssStop < 0:
                print("\n\nTOO DARK!")
            elif aperture - ssStop > len(apertureList):
                print("\n\nTOO BRIGHT!")
            else:
                print("-" * 40)
                print(f"ISO:                {ISO}") 
                print(f"Aperture:           f{apertureList[aperture-ssStop]}")
                print(f"Shutter speed:      1/{shutter[ssIndex]}")
                print("-" * 40)
                
        elif menuChoice == 2:
            aIndex = ApertureSelection()
            aStop = aIndex - aperture
            if index-aStop < 0:
                print("\n\nTOO DARK!")
            elif index-aStop > len(shutter):
                print("\n\nTOO BRIGHT!")
            else:
                print("-" * 40)
                print(f"ISO:                {ISO}") 
                print(f"Aperture:           f{apertureList[aIndex]}")
                print(f"Shutter speed:      1/{shutter[index-aStop]}")
                print("-" * 40)
        print("\n\n")    
 
def mainMenu():
    running = True
    while running:
        print("=" * 40 )
        print("Main menu \n ")
        print("1. Choose Lighting ")
        print("2. Help")
        print("3. Quit \n")
        print("===================================== \n ")

        userChoice = getUserInput("Enter your choice: ",3)
        if userChoice == 1:
            lightingChoice = chooseLighting()
            ISOchoice = setISO()
            calculateSetting(lightingChoice,ISOchoice)
        elif userChoice == 2:    
           helpMenu()
        elif userChoice == 3:
            running = False
    
mainMenu()


