# Libraries
from minerpy import Site

print(r'''
              $$\                                                   
              \__|                                                  
$$$$$$\$$$$\  $$\ $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$  _$$  _$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
$$ / $$ / $$ |$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$ /  $$ |$$ |  $$ |
$$ | $$ | $$ |$$ |$$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$ |  $$ |
$$ | $$ | $$ |$$ |$$ |  $$ |\$$$$$$$\ $$ |      $$$$$$$  |\$$$$$$$ |
\__| \__| \__|\__|\__|  \__| \_______|\__|      $$  ____/  \____$$ |
                                                $$ |      $$\   $$ |
                                                $$ |      \$$$$$$  |
                                                \__|       \______/ 
''')

print('Enter Website')
usrInput = input('> ')

while(True):
    print("""
        1> Show URL
        2> Test Connection
        3> Get 'robot.txt'
        4> Get Source Code
        5> Get Links
        6> Get Text
        7> Get Response Time
        8> Check For Certifications
        9> Check For Cookies 
    """)

    usrAction = int(input('> '))

    usrSiteClass = Site(usrInput)

    if usrAction == 1:
        print(f'Website: {usrSiteClass.show()}')
    elif usrAction == 2:
        usrSiteClass.connection()
    elif usrAction == 3:
        print(usrSiteClass.getRobots())
    elif usrAction == 4:
        print(usrSiteClass.sourceCode())
    elif usrAction == 5:
        count = 1
        for links in usrSiteClass.getLinks():
            print(f'{count}. {links}')
            count+=1
    elif usrAction == 6:
        print(usrSiteClass.getText())
    elif usrAction == 7:
        print(usrSiteClass.certCheck())
    elif usrAction == 8:
        print(usrSiteClass.getResponseTime())
    elif usrAction == 9:
        print(usrSiteClass.checkForCookies())
    else:
        print("Invalid Command!")
        exit()