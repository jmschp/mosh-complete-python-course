 # 13 Stacks

 # Data structurare Stack, like a stack of books, the last book on top of the stack is the first to be removed.
 # LIFO Last In - First Out

 # A good example would be a browser back page

browsing_session = []
browsing_session.append(1)
#browsing_session.append(2)
# browsing_session.append(3)
# browsing_session.append(4)
print(browsing_session)
browsing_session.pop()
print(browsing_session)

# browsing_session[-1]
if not browsing_session: # If the Stack is empty we can not go back any more 
    print("disable")

