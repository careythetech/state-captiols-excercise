from capitals import states



def main (states): #program im running
    
    name = input('Enter Your name: ')
    print('Hello ' + name + "!") # this request user to do something.
    # looping through each state dictonary in the list of states
    for state in states:
        # add 'correct' and 'incorrect' keys to the selected state
        state['correct'] = 0
        state['incorrect'] = 0
        state['total'] = 0
        # print the name key of the selected state
        print(state['name']) 
        # request input from user and storing input
        answer = input('What is the capital of state?: ')
        # if user answer is the same type and value as the capital value
        # for the selected state
        if answer == state['capital']:
            # prints correct
            print('correct')
            # Increment the value of the state key 'correct' by 1
            state['correct'] += 1
        else:
            print('wrong answer')
            state['incorrect'] += 1
        state['total'] += 1
        # print('You have answered this question correctly {0} times out of {1}'.format( state['correct'], state['total'] ) ) 
        print(f'You have answered this question correctly {state['correct']} times out of {state['total']}') 
        

            


    
main (states)