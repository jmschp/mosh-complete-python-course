# 10 Private Members

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("JavaScript")
cloud.add("JAVASCRIPT")

print(cloud["PYTHON"])
# We get the value for the tag Python that it is 4

# print(cloud.tags["PYTHON"])
# Here we get an error because we are acessing the underling dictonary of the class and there we do not have the "PYTHON" tag with capital letters
# To fix we need to hide this atribute from the outside of the class by prefixing it with y=two underscores "__tags"

print(cloud.__dict__)