# 09 Making Custom Containers

# Cointainer are data structure like lists, dictionary tuples and so on. 

# We are going to create a custom container type
# In this example its going to be to keep track of the several tag on a blog.

class TagCloud:
    def __init__(self): # For this example we are going to use a dictonary
        self.tags = {} # We are inicializing an empty dictonary

    def add(self, tag): # Implementing a method to add tags to the dictionary. If the tag exits it will be incremented by one.
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag): # Implmenting a magic method to get the value of a tag, if that taf does not exist it will return 0
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count): # Implmenting a magic method to set the the value for a certain key, in our case tag
        self.tags[tag.lower()] = count

    def __len__(self): # Implmenting a magic method to get the number of tags
        return len(self.tags)

    def __iter__(self): # Implmenting a magic method to make our object iterable
        return iter(self.tags)

cloud = TagCloud()
print(cloud)

cloud.add("python")
cloud.add("JavaScript")
print(cloud.tags)

cloud.add("python")
cloud.add("JavaScript")
print(cloud.tags)

cloud["Java"] = 5
cloud["C++"] = 2
print(cloud.tags)

print(len(cloud))

for tag in cloud:
    print(tag)

for tag, count in cloud.tags.items():
    print(tag, count)

for tag in cloud:
    print(tag, cloud[tag])
