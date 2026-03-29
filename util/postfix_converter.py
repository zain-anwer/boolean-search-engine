def convert_to_postfix(tokens):

    # precedence: NOT > AND > OR
    
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1, '(': 0}
    output_queue = []
    operator_stack = []

    for token in tokens:
       
        token_upper = token.upper()
        
        if token_upper in precedence:
            
            while operator_stack and precedence[operator_stack[-1]] >= precedence[token_upper]:
                output_queue.append(operator_stack.pop())
            
            operator_stack.append(token_upper)
        
        elif token == '(':
            operator_stack.append(token)
        
        elif token == ')':
        
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            
            # removing opening brackett

            operator_stack.pop()
        
        else:
            
            # if its a search term
            output_queue.append(token.lower())

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue