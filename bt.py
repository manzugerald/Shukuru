#Defining the node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#Defining the operators
def operator(c):
    if (c == '+' or c == '-' or c == '*' or c == '/'):
        return True
    else:
        return False
#Constructing the tree
def constructTree(expression):
    if len(expression) == 1:
        return Node(expression)
    elif expression[0] != '(':
        return Node(expression)
    else:
        op = -1
        cnt = 0
        for i in range(1, len(expression) - 1):
            if expression[i] == '(':
                cnt += 1
            elif expression[i] == ')':
                cnt -= 1
            elif cnt == 0 and operator(expression[i]):
                op = i
                break
        if op == -1:
            return constructTree(expression[1:-1])
        else:
            node = Node(expression[op])
            node.left = constructTree(expression[1:op])
            node.right = constructTree(expression[op+1:-1])
            return node

#Using infix / inorder
def infix(node):
    if node is not None:
        if node.left is not None or node.right is not None:
            print('(', end='')
        infix(node.left)
        print(node.data, end='')
        infix(node.right)
        if node.left is not None or node.right is not None:
            #print(')', end='')
            return

#Function to evaluate the expression
def evaluate(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return int(node.data)
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.data == '+':
        return left_val + right_val
    elif node.data == '-':
        return left_val - right_val
    elif node.data == '*':
        return left_val * right_val
    elif node.data == '/':
        return left_val / right_val


while True:
    expression = input('Type the expression to evaluate: ')
    root = constructTree(expression)
    #infix(root)
    print('The Expression "', expression,'" Evaluates to :', evaluate(root))


if __name__ == '__main__':
    main()

