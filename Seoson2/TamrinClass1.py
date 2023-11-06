class Person:
    count=0
    def __init__(self,name,family):
        self.__name=name
        self.__family=family
        Person.count+=1
    def __str__(self):
        return self.__name+"\t\t"+self.__family  


person1=Person("alireza","jahangard")
print(str(person1))
print(Person.count)

        