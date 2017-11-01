# So we left off talking about recursive functions, specifically, we left off
 #talking about the one that follows:

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

# If I define a nasty nested list, say...

nastyNestedList = [ [['a', 'b', 'c'], ['d', 'e', 'f']],
                    [[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]],
                    [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z'] ]

# Damn, that's nasty.
# However, it will still work! When I run this:

flattenedList = flatten(nastyNestedList)

# I very quickly get:

if (flattenedList == ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'and', 'z']):
    print("Line 25: A properly flattened list")

# But you know that.. You want to know why, so let's talk about that.

S = []

# Let's say that we have an empty lsit, obviously  

if S == []:
    print("Line 34: Is going to return an empty list")

# and that will always happen, so the deepest levels of recursion always return
 #a completely empty list... How do we deal with that?  Well think back to what
 #we went over earlier.. We were getting these dictionaries (possibly empty)
 #and all we did was combine them with the one we had... In this case, we say:

# if isinstance(S[0], list):
#     return flatten(S[0]) + flatten(S[1:])
# return S[:1] + flatten(S[1:])

# The first part if statement and return statement pair say basically:
 #"If the first thing in this list is a list, dive deeper into that inner list"
 #and thus we call flatten on the first bit (flatten(S[0])).  We still have
 #work to do, however, so we ALSO have to recurse on the rest of it.. We're just
 #being less specfic as to what to do, because if we keep calling flatten(S[1:])
 #then eventually every element of the list will become the first element, which
 #we do very specific work on (diving deeper into).
# However, not all first elements are lists.. Specifically when we dive down far
 #enough to get to "a" as the first element of a list we're parsing.. 
 #Specifically the list:
 
firstListParsed = ['a', 'b', 'c']

# But since the first element is no londer a list, the second return statement
 #comes into play:

# return S[:1] + flatten(S[1:])

# Where it takes the first element, and front-appends it to the rest of the list
 #(which we have to assume will be properly parsed for us).  So when the second
 #part of the return statement returns:
 
# flatten(S[1:])

# We will have:

secondPartWillReturn = ['b', 'c']

# Then we front-append

print("Line 75: " + str(['a'] + secondPartWillReturn))

# To get:

if (['a'] + secondPartWillReturn == ['a', 'b', 'c']):
    print("Line 80: A properly connected sub portion of the list")
    
# But that was pretty pointless since we already had ['a', 'b', 'c'] in the code
 #already... However I think it gets the point across as to what happens in this
 #example.  Just to be sure, let's map the recursions:
 
# For reference: [ [['a', 'b', 'c'], ['d', 'e', 'f']],
#                  [[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]],
#                  [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z'] ]

indent = ""
def flatten(S):
    global indent
    indent += "\t"
    print(indent + "So, we have: " + str(S) + ".. Ask if it's empty, and it ", end='')
    if S == []:
        print("is!  We return '[]'")
        indent = indent[:-1]
        return S
    else:
        print("isn't.  We continue..")
    
    print(indent + "Is the first element a list? (isinstance(S[0], list)) ", end='')
    if isinstance(S[0], list):
        print("Yes! It is: " + str(S[0]) + " Now recurse twice on that, and the rest of the list: " + str(S[1:]))
        newList = flatten(S[0]) + flatten(S[1:])
        print(indent + "And now we have " + str(newList))
        indent = indent[:-1]
        return newList
    else:
        print("No. It isn't...")
    
    print(indent + "So now we know the first element is a real thing, not a list. We can now form: " + str(S[:1]) + '+' + str(flatten(S[1:])))
    newList = S[:1] + flatten(S[1:])
    print(indent + "And now we have " + str(newList))
    indent = indent[:-1]
    return newList
    
flatten(nastyNestedList)

# Which shows a nice indented flow of the function, as follows:
# So, we have: [[['a', 'b', 'c'], ['d', 'e', 'f']], [[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]], [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z']].. Ask if it's empty, and it isn't.  We continue..
# Is the first element a list? (isinstance(S[0], list)) Yes! It is: [['a', 'b', 'c'], ['d', 'e', 'f']] Now recurse twice on that, and the rest of the list: [[[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]], [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z']]
# 	So, we have: [['a', 'b', 'c'], ['d', 'e', 'f']].. Ask if it's empty, and it isn't.  We continue..
# 	Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['a', 'b', 'c'] Now recurse twice on that, and the rest of the list: [['d', 'e', 'f']]
# 		So, we have: ['a', 'b', 'c'].. Ask if it's empty, and it isn't.  We continue..
# 		Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 			So, we have: ['b', 'c'].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 				So, we have: ['c'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				So now we know the first element is a real thing, not a list. We can now form: ['c']+[]
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				And now we have ['c']
# 			So now we know the first element is a real thing, not a list. We can now form: ['b']+['c']
# 				So, we have: ['c'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				So now we know the first element is a real thing, not a list. We can now form: ['c']+[]
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				And now we have ['c']
# 			And now we have ['b', 'c']
# 		So now we know the first element is a real thing, not a list. We can now form: ['a']+['b', 'c']
# 			So, we have: ['b', 'c'].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 				So, we have: ['c'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				So now we know the first element is a real thing, not a list. We can now form: ['c']+[]
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				And now we have ['c']
# 			So now we know the first element is a real thing, not a list. We can now form: ['b']+['c']
# 				So, we have: ['c'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				So now we know the first element is a real thing, not a list. We can now form: ['c']+[]
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				And now we have ['c']
# 			And now we have ['b', 'c']
# 		And now we have ['a', 'b', 'c']
# 		So, we have: [['d', 'e', 'f']].. Ask if it's empty, and it isn't.  We continue..
# 		Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['d', 'e', 'f'] Now recurse twice on that, and the rest of the list: []
# 			So, we have: ['d', 'e', 'f'].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 				So, we have: ['e', 'f'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: ['f'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					So now we know the first element is a real thing, not a list. We can now form: ['f']+[]
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					And now we have ['f']
# 				So now we know the first element is a real thing, not a list. We can now form: ['e']+['f']
# 					So, we have: ['f'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					So now we know the first element is a real thing, not a list. We can now form: ['f']+[]
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					And now we have ['f']
# 				And now we have ['e', 'f']
# 			So now we know the first element is a real thing, not a list. We can now form: ['d']+['e', 'f']
# 				So, we have: ['e', 'f'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: ['f'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					So now we know the first element is a real thing, not a list. We can now form: ['f']+[]
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					And now we have ['f']
# 				So now we know the first element is a real thing, not a list. We can now form: ['e']+['f']
# 					So, we have: ['f'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					So now we know the first element is a real thing, not a list. We can now form: ['f']+[]
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					And now we have ['f']
# 				And now we have ['e', 'f']
# 			And now we have ['d', 'e', 'f']
# 			So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 		And now we have ['d', 'e', 'f']
# 	And now we have ['a', 'b', 'c', 'd', 'e', 'f']
# 	So, we have: [[[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]], [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z']].. Ask if it's empty, and it isn't.  We continue..
# 	Is the first element a list? (isinstance(S[0], list)) Yes! It is: [[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]] Now recurse twice on that, and the rest of the list: [[[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z']]
# 		So, we have: [[['h', 'i', 'j']], ['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]].. Ask if it's empty, and it isn't.  We continue..
# 		Is the first element a list? (isinstance(S[0], list)) Yes! It is: [['h', 'i', 'j']] Now recurse twice on that, and the rest of the list: [['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]]
# 			So, we have: [['h', 'i', 'j']].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['h', 'i', 'j'] Now recurse twice on that, and the rest of the list: []
# 				So, we have: ['h', 'i', 'j'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: ['i', 'j'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: ['j'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['j']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['j']
# 					So now we know the first element is a real thing, not a list. We can now form: ['i']+['j']
# 						So, we have: ['j'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['j']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['j']
# 					And now we have ['i', 'j']
# 				So now we know the first element is a real thing, not a list. We can now form: ['h']+['i', 'j']
# 					So, we have: ['i', 'j'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: ['j'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['j']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['j']
# 					So now we know the first element is a real thing, not a list. We can now form: ['i']+['j']
# 						So, we have: ['j'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['j']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['j']
# 					And now we have ['i', 'j']
# 				And now we have ['h', 'i', 'j']
# 				So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 			And now we have ['h', 'i', 'j']
# 			So, we have: [['k', 'l', 'm'], [['n', 'o', 'p'], ['q', 'r', 's']]].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['k', 'l', 'm'] Now recurse twice on that, and the rest of the list: [[['n', 'o', 'p'], ['q', 'r', 's']]]
# 				So, we have: ['k', 'l', 'm'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: ['l', 'm'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: ['m'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['m']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['m']
# 					So now we know the first element is a real thing, not a list. We can now form: ['l']+['m']
# 						So, we have: ['m'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['m']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['m']
# 					And now we have ['l', 'm']
# 				So now we know the first element is a real thing, not a list. We can now form: ['k']+['l', 'm']
# 					So, we have: ['l', 'm'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: ['m'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['m']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['m']
# 					So now we know the first element is a real thing, not a list. We can now form: ['l']+['m']
# 						So, we have: ['m'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['m']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['m']
# 					And now we have ['l', 'm']
# 				And now we have ['k', 'l', 'm']
# 				So, we have: [[['n', 'o', 'p'], ['q', 'r', 's']]].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) Yes! It is: [['n', 'o', 'p'], ['q', 'r', 's']] Now recurse twice on that, and the rest of the list: []
# 					So, we have: [['n', 'o', 'p'], ['q', 'r', 's']].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['n', 'o', 'p'] Now recurse twice on that, and the rest of the list: [['q', 'r', 's']]
# 						So, we have: ['n', 'o', 'p'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: ['o', 'p'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: ['p'].. Ask if it's empty, and it isn't.  We continue..
# 								Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								So now we know the first element is a real thing, not a list. We can now form: ['p']+[]
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								And now we have ['p']
# 							So now we know the first element is a real thing, not a list. We can now form: ['o']+['p']
# 								So, we have: ['p'].. Ask if it's empty, and it isn't.  We continue..
# 								Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								So now we know the first element is a real thing, not a list. We can now form: ['p']+[]
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								And now we have ['p']
# 							And now we have ['o', 'p']
# 						So now we know the first element is a real thing, not a list. We can now form: ['n']+['o', 'p']
# 							So, we have: ['o', 'p'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: ['p'].. Ask if it's empty, and it isn't.  We continue..
# 								Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								So now we know the first element is a real thing, not a list. We can now form: ['p']+[]
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								And now we have ['p']
# 							So now we know the first element is a real thing, not a list. We can now form: ['o']+['p']
# 								So, we have: ['p'].. Ask if it's empty, and it isn't.  We continue..
# 								Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								So now we know the first element is a real thing, not a list. We can now form: ['p']+[]
# 									So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 								And now we have ['p']
# 							And now we have ['o', 'p']
# 						And now we have ['n', 'o', 'p']
# 						So, we have: [['q', 'r', 's']].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['q', 'r', 's'] Now recurse twice on that, and the rest of the list: []
# 							So, we have: ['q', 'r', 's'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: ['r', 's'].. Ask if it's empty, and it isn't.  We continue..
# 								Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 									So, we have: ['s'].. Ask if it's empty, and it isn't.  We continue..
# 									Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									So now we know the first element is a real thing, not a list. We can now form: ['s']+[]
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									And now we have ['s']
# 								So now we know the first element is a real thing, not a list. We can now form: ['r']+['s']
# 									So, we have: ['s'].. Ask if it's empty, and it isn't.  We continue..
# 									Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									So now we know the first element is a real thing, not a list. We can now form: ['s']+[]
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									And now we have ['s']
# 								And now we have ['r', 's']
# 							So now we know the first element is a real thing, not a list. We can now form: ['q']+['r', 's']
# 								So, we have: ['r', 's'].. Ask if it's empty, and it isn't.  We continue..
# 								Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 									So, we have: ['s'].. Ask if it's empty, and it isn't.  We continue..
# 									Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									So now we know the first element is a real thing, not a list. We can now form: ['s']+[]
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									And now we have ['s']
# 								So now we know the first element is a real thing, not a list. We can now form: ['r']+['s']
# 									So, we have: ['s'].. Ask if it's empty, and it isn't.  We continue..
# 									Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									So now we know the first element is a real thing, not a list. We can now form: ['s']+[]
# 										So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 									And now we have ['s']
# 								And now we have ['r', 's']
# 							And now we have ['q', 'r', 's']
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['q', 'r', 's']
# 					And now we have ['n', 'o', 'p', 'q', 'r', 's']
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				And now we have ['n', 'o', 'p', 'q', 'r', 's']
# 			And now we have ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
# 		And now we have ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
# 		So, we have: [[[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']], ['z']].. Ask if it's empty, and it isn't.  We continue..
# 		Is the first element a list? (isinstance(S[0], list)) Yes! It is: [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']] Now recurse twice on that, and the rest of the list: [['z']]
# 			So, we have: [[['t', 'u', 'v'], ['w'], ['x']], ['y'], ['and']].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) Yes! It is: [['t', 'u', 'v'], ['w'], ['x']] Now recurse twice on that, and the rest of the list: [['y'], ['and']]
# 				So, we have: [['t', 'u', 'v'], ['w'], ['x']].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['t', 'u', 'v'] Now recurse twice on that, and the rest of the list: [['w'], ['x']]
# 					So, we have: ['t', 'u', 'v'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: ['u', 'v'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: ['v'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							So now we know the first element is a real thing, not a list. We can now form: ['v']+[]
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							And now we have ['v']
# 						So now we know the first element is a real thing, not a list. We can now form: ['u']+['v']
# 							So, we have: ['v'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							So now we know the first element is a real thing, not a list. We can now form: ['v']+[]
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							And now we have ['v']
# 						And now we have ['u', 'v']
# 					So now we know the first element is a real thing, not a list. We can now form: ['t']+['u', 'v']
# 						So, we have: ['u', 'v'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: ['v'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							So now we know the first element is a real thing, not a list. We can now form: ['v']+[]
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							And now we have ['v']
# 						So now we know the first element is a real thing, not a list. We can now form: ['u']+['v']
# 							So, we have: ['v'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							So now we know the first element is a real thing, not a list. We can now form: ['v']+[]
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							And now we have ['v']
# 						And now we have ['u', 'v']
# 					And now we have ['t', 'u', 'v']
# 					So, we have: [['w'], ['x']].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['w'] Now recurse twice on that, and the rest of the list: [['x']]
# 						So, we have: ['w'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['w']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['w']
# 						So, we have: [['x']].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['x'] Now recurse twice on that, and the rest of the list: []
# 							So, we have: ['x'].. Ask if it's empty, and it isn't.  We continue..
# 							Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							So now we know the first element is a real thing, not a list. We can now form: ['x']+[]
# 								So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 							And now we have ['x']
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['x']
# 					And now we have ['w', 'x']
# 				And now we have ['t', 'u', 'v', 'w', 'x']
# 				So, we have: [['y'], ['and']].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['y'] Now recurse twice on that, and the rest of the list: [['and']]
# 					So, we have: ['y'].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					So now we know the first element is a real thing, not a list. We can now form: ['y']+[]
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					And now we have ['y']
# 					So, we have: [['and']].. Ask if it's empty, and it isn't.  We continue..
# 					Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['and'] Now recurse twice on that, and the rest of the list: []
# 						So, we have: ['and'].. Ask if it's empty, and it isn't.  We continue..
# 						Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						So now we know the first element is a real thing, not a list. We can now form: ['and']+[]
# 							So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 						And now we have ['and']
# 						So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 					And now we have ['and']
# 				And now we have ['y', 'and']
# 			And now we have ['t', 'u', 'v', 'w', 'x', 'y', 'and']
# 			So, we have: [['z']].. Ask if it's empty, and it isn't.  We continue..
# 			Is the first element a list? (isinstance(S[0], list)) Yes! It is: ['z'] Now recurse twice on that, and the rest of the list: []
# 				So, we have: ['z'].. Ask if it's empty, and it isn't.  We continue..
# 				Is the first element a list? (isinstance(S[0], list)) No. It isn't...
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				So now we know the first element is a real thing, not a list. We can now form: ['z']+[]
# 					So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 				And now we have ['z']
# 				So, we have: [].. Ask if it's empty, and it is!  We return '[]'
# 			And now we have ['z']
# 		And now we have ['t', 'u', 'v', 'w', 'x', 'y', 'and', 'z']
# 	And now we have ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'and', 'z']
# And now we have ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'and', 'z']

# If you have any questions, don't hesitate to ask!

# And the other thing, about the speed of slicing strings... I found myself
 #needing to parse a lot of text, and I decided that the bible was an
 #appropriate work for this project, so I found myself doing the following:
