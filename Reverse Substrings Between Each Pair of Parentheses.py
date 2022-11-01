class Solution:
    def reverseParentheses(self, s: str) -> str:
    
        stack, buffer = [], ''
      
        for ch in s:
            if ch != ')':
                stack.append(ch)               

            else:
                buffer = ''
                while stack[-1] != '(':
                    buffer+= stack.pop()
                stack.pop()
                    
                for ss in buffer:
                    stack.append(ss)

            # remove the # below to see a trace of the stack and buffer
            #print('\tch: ',ch, '\tbuffer: ', buffer, '\tstack: ', stack)

        return ''.join(stack)
