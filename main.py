dict = {}
def input_error(func):
    def inner(string):
        try:
             result = func(string)
        except ValueError:
            return f'You typed irrelevant information. Give me name and phone, please'
        except KeyError:
            return f'You spelled an incorrect username or it has not been added earlier. Try command "add ..."'
        except IndexError:
            return f'You typed an incorrect index or it has not been added earlier. Try command "add ..."'
        
        return result

    
    return inner




   



def greeting():
    return f'How can I help you?'
@input_error

def add(string):
    index = string.find(' ')
    new_string = string[index+1:]
    new_index = new_string.find(' ')
    if new_index == -1:
        raise ValueError
    
    dict[new_string[:new_index]] = new_string[new_index+1:]

    return f'Contact has been added succesfully'

   

@input_error
def change(string):
    index = string.find(' ')
    new_string = string[index+1:]
    new_index = new_string.find(' ')
    if new_index == -1:
        raise ValueError
    
    if new_string[:new_index] in dict:
        dict[new_string[:new_index]] = new_string[new_index+1:]
    else:
        raise KeyError
    
    return f'Contact has been changed succesfully'
    
    
@input_error
def phone(string):
    index = string.find(' ')
    new_string = string[index+1:]
    
    return dict[new_string]
    
    

def show_all():
    return dict

def goodbye():
    return f'Good bye!'

def main():
    while True:
        string = input('<3 <3 <3 ')
        if string.lower() == 'hello':
            print(greeting())          
        elif 'add' in string.lower():
            print(add(string))
        elif 'change' in string.lower():
            print(change(string))
        elif 'phone' in string.lower():
            print(phone(string))
        elif string.lower() == 'show all':
            print(show_all())
        elif string.lower() == 'good bye' or string.lower() == 'close' or string.lower() == 'exit':
            print(goodbye())
            break
        else:
            print('Unknown command, please try again')
      
      
    return 
