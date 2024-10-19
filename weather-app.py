# Requirements
"""
brotlicffi==1.1.0.0
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
idna==3.7
pycparser==2.22
requests==2.32.3
simplejson==3.19.2
urllib3==2.2.2
"""

import requests, shutil, os, sys

class utils:
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def term(self,n):
        width, height = shutil.get_terminal_size()
        if n == 'width':
            return width
        elif n == 'height':
            return height
        else:
            return False

    def txt(self,text):
        top, side, width = self.border()

        # Calculate padding
        text_length = len(text)
        total_padding = (width - text_length - 2)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        
        middle = f'|{" " * left_padding}{text}{" " * right_padding}|'
        if len(middle) < width:
            middle += ' ' * (width - len(middle))
        
        return middle

    def border(self):
        width = self.term('width')
        top = '-' * width
        side = f'|{" " * (width - 2)}|'

        return top, side, width
    
    def borderText(self,text):
        top, side, width = self.border()
        print(f'\n{top}\n{side}\n{self.txt(text)}\n{side}\n{top}')

    def padding(self,text):
        top, side, width = self.border()

        text_length = len(text)
        total_padding = (width - text_length - 2)
        left_padding = total_padding // 2
        opt = input(f'{" " * left_padding}{text} ')

        return opt

class design:
    def welcome(self):
        # Welcome box on top
        top, side, width = u.border()
        
        print(f'\n{top}\n{side}\n{u.txt('Weather CLI')}\n{side}\n{top}')

    def greet(self):
        '''
        Simple greet menu
        
        Simple greet with option menu, making easy to navigate.
        '''
        u.clear()

        self.welcome()

        top, side, width = u.border()

        print(f'{top}\n{side}\n{u.txt('1) Location')}\n{u.txt('2) Support')}\n{u.txt('3) About us')}\n{u.txt('4) FAQ')}\n{u.txt('5) Buy me a coffee')}\n{u.txt('6) Quit')}\n{side}\n{top}')

        opt = u.padding('Choose operation: ')
        
        return opt

    def city(self):
        '''
        Simple city selection menu.
        '''
        u.clear()
        top, side, width = u.border()
        
        # First Screen
        u.borderText(' Location: ')
        city = u.padding('  City: ')

        u.clear()
        
        # Create the content string and calculate padding
        u.borderText(f'  City: {city}')
        
        return city

class options:
    def support(self):
        '''
        Support page.
        
        Option menu for different types of support.
        '''
        top, side, width, = u.border()
        u.clear()

        print(f'\n{top}\n{side}\n{u.txt('Welcome to the support section.')}\n{u.txt('How can we assist you today?')}\n{side}\n{top}')
        
        print(f'{top}\n{side}\n{u.txt('1) The weather app is not accurate or not working')}\n{u.txt('2) Other Bugs')}\n{u.txt('3) Suggest other improvements')}\n{u.txt('4) Previous menu')}{u.txt('5) Quit')}\n{side}\n{top}')

        opt = u.padding('Choose operation: ')

        match opt:
            case '1':
                u.clear()
                u.borderText("If there are any issues with the weather app or it's accuracy, open issue request on our github.")
                u.padding('Type anything to exit: ')

            case '2':
                u.clear()
                u.borderText("If there are any bugs you want to report, open issue/pull request on our github.")    
                u.padding('Type anything to exit: ')

            case '3':
                u.clear()
                u.borderText("If there is anything you want to suggest us, make a pull request on our github.")
                u.padding('Type anything to exit: ')

    def aboutus(self):
        '''
        Simple info about us.
        '''
        top, side, width = u.border()
        u.clear()

        print(f'\n{top}\n{side}\n{u.txt("This is a small testing project of weather app inside a terminal.")}\n{u.txt('This is app is still in beta, and you may encounter some bugs.')}\n{side}\n{top}')

        u.padding('type anything to exit: ')

    def faq(self):
        '''
        FAQ page.
        '''
        top, side, width, = u.border()
        u.clear()

        print(f'\n{top}\n{side}')
        print(f'''{u.txt('Q: How do I get weather information using this application?')}
{u.txt('A: Select the "Weather" option from the menu, enter your city name when prompted,')}
{u.txt('and it will display the current weather information for that city.')}
{side}
{u.txt('Q: What should I do if the weather information is inaccurate or not updating?')}
{u.txt('A: If you notice inaccuracies or issues with the weather data, please open issue request on our github.')}
{u.txt('Our team will investigate and address the problem promptly.')}
{side}
{u.txt('Q: How can I contact customer support?')}
{u.txt('A: For support inquiries, please email us at support@example.com or')}
{u.txt('visit example.com/support to submit a support ticket.')}
{side}
{u.txt('Q: Can I suggest new features or improvements?')}
{u.txt('A: Yes! We welcome your suggestions and feedback. Please open pull request on out github.')}
{u.txt('Your feedback helps us improve our service.')}
{side}
{u.txt('Q: Is there a way to contribute or support the development of this application?')}
{u.txt('A: If you enjoy using our application, you can support us by buying us a coffee!')}
{u.txt('Select the "Buy me a coffee" option from the menu to learn more.')}
{u.txt('If you want to contribute to the project, start by creating pull request for new feature!')}
{side}
{u.txt('Q: How often is the weather data updated?')}
{u.txt('A: The weather data is updated regularly from reliable sources.')}
{u.txt('However, specific update frequencies may vary based on data sources and availability.')}
{side}
{u.txt('Q: Can I customize the settings or preferences in the application?')}
{u.txt('A: Currently, the application provides basic weather information.')}
{u.txt('We are working on adding customization features in future updates.')}
{side}
{u.txt('Q: Is the weather information provided reliable?')}
{u.txt('A: We strive to provide accurate and reliable weather information.')}
{u.txt('However, please note that weather forecasts are subject to change based on meteorological conditions.')}
{side}
{u.txt('Q: What platforms does this application support?')}
{u.txt('A: Our application is designed to run on various platforms, including Windows, macOS, and Linux.')}
{u.txt('Ensure you have Python installed to use it.')}
{side}
{u.txt('Q: How can I quit the application?')}
{u.txt('A: Select the "Quit" option from the menu to exit the application gracefully.')}
''')
        print(f'{side}\n{top}')
        u.padding('Type anything to exit: ')

    def coffee(self):
        '''
        Buy coffee page.
        '''
        u.clear()
        u.borderText("If you enjoy using this program, consider supporting us at buymeacoffe.com/NiGu")
        u.padding('Type anything to exit: ')

class api:
    def get_weather(self,city):
        '''
        Fetch city info from API.
        
        Get data from API and display according to users choice.
        '''
        # Define url and API
        key = '' # Your API goes here
        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
        
        # Define get function
        response = requests.get(url)
        data = response.json()
        
        while True:
            # Terminal Menu
            print()
            top, side, width = u.border()

            print(f'{top}\n{side}\n{u.txt('Option Menu:')}\n{side}\n{u.txt('1) Location')}\n{u.txt('2) Condition')}\n{u.txt('3) All info')}\n{u.txt('4) Previous menu')}\n{u.txt('5) Quit')}\n{side}\n{top}')
            
            opt = u.padding('Choose option:')
            
            match opt:
                case '1':
                    u.clear()
                    top, side, width = u.border()

                    d.welcome()

                    print(f'{top}\n{side}')
                    for key, value in data['location'].items():
                        if key == 'name':
                            print(u.txt(value))
                        print(u.txt(f'{key}: {value}'))
                    print(f'{side}\n{top}')
                    
                case '2':
                    u.clear()
                    d.welcome()

                    print(f'{top}\n{side}')
                    for key, value in data['current'].items():
                        if key == 'pressure_mb':
                            break
                        print(u.txt(f'{key}: {value}'))
                    print(f'{side}\n{top}')
                
                case '3':
                    u.clear()
                    d.welcome()

                    print(f'{top}\n{side}')
                    print(f'{u.txt('Location: ')}\n{side}')

                    for key, value in data['location'].items():
                        if key == 'name':
                            print(u.txt(value))
                        print(u.txt(f'{key}: {value}'))
                    
                    print(f'{side}\n{u.txt('Condition: ')}\n{side}')
                    for key, value in data['current'].items():
                        if key == 'pressure_mb':
                            break
                        print(u.txt(f'{key}: {value}'))

                    print(f'{side}\n{top}')
                
                case '4':
                    break
            
                case '5':
                    sys.exit()
            
        return data

u = utils()
d = design()
o = options()
a = api()

# clear the console screen
u.clear()

# main loop for user interaction
while True:
    # display greeting and menu options, and get user choice
    # process user choice
    match d.greet():
        case '1':
            # option 1: Get weather information for a city
            a.get_weather(d.city())

        case '2':
            # option 2: Display support information
            o.support()

        case '3':
            # option 3: Display information about the team
            o.aboutus()

        case '4':
            # option 4: Display frequently asked questions
            o.faq()

        case '5':
            # option 5: Support the developer by buying coffee
            o.coffee()

        case '6':
            # option 6: exit the program
            u.clear()
            sys.exit()  # exit the program
