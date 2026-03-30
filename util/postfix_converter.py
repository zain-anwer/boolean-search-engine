def convert_to_postfix(tokens):

    # precedence: NOT > AND > OR
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1, '(': 0}
    output_queue = []
    operator_stack = []

    for token in tokens:
       
        token_upper = token.upper()
        
        # Check for '(' first so it doesn't trigger the precedence loop
        
        if token == '(':
            operator_stack.append(token)
        
        elif token == ')':
        
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            
            # removing opening brackett
            if operator_stack:
                operator_stack.pop()
        
        elif token_upper in precedence:
            
            while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence[token_upper]:
                output_queue.append(operator_stack.pop())
            
            operator_stack.append(token_upper)
        
        else:
            
            # if its a search term
            output_queue.append(token.lower())

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue