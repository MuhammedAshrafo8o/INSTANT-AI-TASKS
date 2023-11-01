# Sessionn '3' Task
## 1- How to make user enter only digits or only chars
```python
def get_valid_input(value):
    while True:
        user_input = input(value)
        if user_input.isdigit() or user_input.isalpha(): 
            return user_input
        else:
            print("Please enter only numbers or only characters.")


user_input = get_valid_input("Please enter only numbers or only characters.")
print("You entered:", user_input)
```

___
---

## 2- what is the different between the framework and the library ?
| S.no | Framewok | Library |
| ---- | -------- | ------- |
|1 -   |It comprises of lot of APIs , compilers , support programs , libraries etc. | It is a collection of helper modules , classes , objects , functions , pre-written code , etc. |
|2 -|It is difficult to replace frameworks.	|A library is easy to be replaced with another library.|
|3 -|A framework development requires a lot of code that decrease performance and increase the load time.|Building a library requires less code , so there is better performance and fast load time.|
|4 -|Including framework smoothly into an existing project is impossible.|Libraries can be integrated easily into existing projects to add some specific functionality.|
|5 -|Its example are AngularJS , Spring , NodeJS , etc.|Its example are JQuery , React JS , etc. |

---
---

## 3 - The OOD with Example 
### Object-Oriented Design (OOD) is a programming paradigm that uses objects to model real-world entities and their interactions within a software system. Objects are instances of classes, and they encapsulate both data (attributes or properties) and the methods (functions or behaviors) that operate on that data. OOD promotes concepts like encapsulation, inheritance, and polymorphism, which can make code more modular, maintainable, and understandable

```python
# Define a class for the Vehicle
class Vehicle:
    # Constructor to initialize the attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the vehicle
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is now running.")
        else:
            print(f"{self.year} {self.make} {self.model} is already running.")

    # Method to stop the vehicle
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has been stopped.")
        else:
            print(f"{self.year} {self.make} {self.model} is already stopped.")

# Create instances (objects) of the Vehicle class
car1 = Vehicle("Toyota", "Camry", 2022)
car2 = Vehicle("Honda", "Civic", 2023)

# Interact with the objects
car1.start()
car2.start()

car1.stop()

```
### Object-Oriented Design allows us to encapsulate the properties and behaviors of a "Vehicle" into a single entity (the object) and provides a clear and structured way to work with objects. This approach is scalable, making it easy to add more functionality and additional classes (e.g., "Truck," "Motorcycle") to represent different types of vehicles in a larger system.

---
---

## 4- How to solve the problem of Fragmentation ?
### Memory Fragmentation:
1. **Memory Allocation Algorithms:** Use memory allocation algorithms that minimize fragmentation. For example, buddy memory allocation, memory paging, and segmentation can help reduce external memory fragmentation.

1. **Memory Pools:** Implement memory pools or object pools, which pre-allocate memory for specific purposes and reuse memory blocks, reducing both external and internal fragmentation.

1. **Compact Memory:** Periodically, compact memory to reclaim fragmented memory blocks by moving allocated objects to contiguous memory areas.

---
---

## 5-  What is the different between Function and Method ?
* **Function:** A Function is a reusable piece of code. It can have input data on which it can operate (i.e. arguments) and it can also return data by having a return type. It is the concept of procedural and functional programming languages.

* **Method:** The working of the method is similar to a function i.e. it also can have input parameters/arguments and can also return data by having a return type but has two important differences when compared to a function.

| Function | Method |
| -------- | ------ |
|It is called by its own name/independently. | It is called by its object’s name/referenced. |
|As it is called independently it means the data is passed explicitly or externally. | As it is called dependently which means the data is passed implicitly or internally. |


---
---

## 6- How can i access element in the set ?
1. #### i can access the element by direct search like search by the value that i want like this:
    ```python
    my_set = {1, 2, 3, 4, 5}

    # Check if an element is in the set
    element = 3
    if element in my_set:
        print(f"{element} is in the set.")
    else:
        print(f"{element} is not in the set.")
    ```
1. ### or i can convert the set to the list to search by index or possition
    ```python
    my_set = {1, 2, 3, 4, 5}

    # Check if an element is in the set
    element = 3
    if element in my_set:
        print(f"{element} is in the set.")
    else:
        print(f"{element} is not in the set.")  
    ```

    ### Notes:
    **you cannot directly access elements by their index or position because sets are unordered and do not have indices like lists or tuples. However, you can convert the set to a list or another ordered data structure to access elements by their position.**

---
---

## 7- How can i use Do While in python?
**there is no Do While In python but we will write the code that has the same work**
```python
i = 1
while True:
    print("now the number is",i)
    i += 1

    if i > 6:
        break;

```
___
___


