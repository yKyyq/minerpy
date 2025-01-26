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

print("""
    1> Show URL
    2> Test Connection
    3> Get 'robot.txt'
    4> Get Source Code
    5> Get Links
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