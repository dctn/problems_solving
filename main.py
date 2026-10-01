is_exit = False
global_variables = {}
while not is_exit:
    input_str = input("Enter a cmd (or 'exit' to quit): ").lower()
    input_list = input_str.split(" ")
    if input_list[0] == 'exit':
        is_exit = True
        
    elif input_list[0] == 'set':
        global_variables[input_list[1]] = input_list[2]
        
    elif input_list[0] == 'get':
        if input_list[1] in global_variables:
            print(global_variables[input_list[1]])
        else:
            print(None)
            
    elif input_list[0] == 'unset':
        if input_list[1] in global_variables:
            del global_variables[input_list[1]]
        else:
            print(None)
            
    elif input_list[0] == 'count':
        num = input_list[1]
        count = 0
        for val in global_variables.values():
            if num == val:
                count +=1
        print(count)        
        