#the  ways thast i can create a constans in python


#in 1st way i can use the Uppercase Variables

MY_CONSTANT = 50



#in 2nd way i can uses the classes by define constants  within a class attributes

class Constants:
    MY_CONSTANT = 50

value = Constants.MY_CONSTANT
print(value)



#in 3rd way i can use named tuples thats created objects with named fields by define it as collection of related constans

from collections import namedtuple

MyConstants = namedtuple('MyConstants', ['CONSTANT_1', 'CONSTANT_2'])
constants = MyConstants(CONSTANT_1=50, CONSTANT_2='MAMO')

value1 = constants.CONSTANT_1
value2 = constants.CONSTANT_2

print(value1)
print(value2)


#in 4th way i can use enumaration thast allows you to create enumerations, which are sets of symbolic names (members)
# bound to unique, constant values. This is a more structured way to define constants

from enum import Enum

class MyEnum(Enum):
    CONSTANT_1 = 50
    CONSTANT_2 = 'MAMO'

value1 = MyEnum.CONSTANT_1.value
value2 = MyEnum.CONSTANT_2.value

print(value1)
print(value2)


#in 5th way i can use frozenn sets that's are immutable sets, and you can use them to create collections of constants

MY_CONSTANT_SET = frozenset({50, 'MAMo'})

# Access the constants
value1 = 50  in MY_CONSTANT_SET
value2 = 'MAMO' in MY_CONSTANT_SET

