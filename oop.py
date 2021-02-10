# OOP
# Class
class BigObject:
    pass


print(type(BigObject))

# We instantiate an object from our class. So <obj1> is an Instance of <BigObject> Class.
obj1 = BigObject()

print(type(obj1))
print("###################################")


class PlayerCharacter:
    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # Attributes
        self.name = name
        self.age = age

    def run(self):
        print("RUN")
        return self


player1 = PlayerCharacter("Haika", 21)
player2 = PlayerCharacter("Hejar", 22)

print(player1)
print(player1.name)
print(player1.age)
print(player1.run())

print("###################################")

print(player2)
print(player2.name)
print(player2.age)
print(player2.run())

print("###################################")

print(help(player1))

print("###################################")


class PlayerCharacter2:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # Attributes (Dynamic Attribute) and (There is no change for our attribute)
        self.name = name
        self.age = age

    def run(self):
        print("RUN")
        return self


player3 = PlayerCharacter2("Darling", 16)

print(player3)
print(player3.membership)

print(PlayerCharacter2.membership)

print("###################################")


class PlayerCharacter3:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        if self.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    def run(self):
        print("RUN")
        return self


player4 = PlayerCharacter3("XBox", 20)

print(player4.membership)
print(player4.name)


class PlayerCharacter4:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter4.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is great {self.name} :)")


player5 = PlayerCharacter4("Heisenberg", 52)

print(player5.membership)
print(player5.name)
print(player5.shout())

print("###################################")


class PlayerCharacter5:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter5.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    def shout(self):
        # Does this works? No, It doesn't. Why? Because name is not a class object attribute. It's defined in our constructor or init function.
        print(f"My name is great {PlayerCharacter5.name} :)")
        # Output : AttributeError: type object 'PlayerCharacter5' has no attribute 'name'. If we had membership instead of name, it would work properly and if we wanted this to work we should use PlayerCharacter5 in our shout function instead of self.


player6 = PlayerCharacter5("Jon Snow", 24)

print(player6.membership)
print(player6.name)
# print(player6.shout())
# Error: Output : AttributeError: type object 'PlayerCharacter5' has no attribute 'name'.

print("###################################")


class PlayerCharacter6:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object. Also here we can have default parameters. And if we forget to instantiate our object like player7, we don't get error. Remember that these are default parameters and if we instantiate our object our parameters will replace of default parameters.
    def __init__(self, name="Elly", age=0):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter5.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age


player7 = PlayerCharacter6()

print(player7.name)
print(player7.age)

print("###################################")


class PlayerCharacter7:

    # We can have safegurds like lie 175 to perhaps make sure that we receive right data type in order to create an object.
    def __init__(self, name="Elly", age=0):
        if age > 18:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age


player8 = PlayerCharacter7()

# print(player8.name)
# print(player8.age)

# We will get this error because of line 175. AttributeError: 'PlayerCharacter7' object has no attribute 'name'.

# We have age equals to 19 and then we don't get error like top.
player9 = PlayerCharacter7(age=19)

print(player9.name)
print(player9.age)

print("###################################")

# Given the below class:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Cati', 4)
cat2 = Cat('Odi', 3)
cat3 = Cat('Lucy', 6)


# 2 Create a function that finds the oldest cat

def oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


print(f"The oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old.")


print("###################################")


class PlayerCharacter8:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter8.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is great {self.name} :)")

    # It's like class object attribute.
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player10 = PlayerCharacter8("Kubal", 34)
print(player10.adding_things(5, 9))

# We also can use class method without instantiate an object like bottom.
print(PlayerCharacter8.adding_things(5, 1))

print("###################################")


class PlayerCharacter9:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter9.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is great {self.name} :)")

    # It's like class object attribute. We can also use cls to instantiate an object with this class method like bottom.

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)


player11 = PlayerCharacter9.adding_things(5, 6)

print(player11.name)
print(player11.age)

print("###################################")


class PlayerCharacter10:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter10.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is great {self.name} :)")

    # It's like class object attribute. We can also use cls to instantiate an object with this class method like bottom.

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    # It's exact like class method, except we don't have access to the cls or class, so we can't instantiate a class with it.
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player12 = PlayerCharacter10("Latina", 23)

print(player12.adding_things2(2, 1))

# We also can use static method without instantiate an object like bottom.
print(PlayerCharacter10.adding_things2(5, 6))


print("###################################")


class PlayerCharacter11:
    # Class Object Attribute (Static Attribute)
    membership = True

    # Constructor Method Or Init Method And It called automatically called, everytime we instantiate an object.
    def __init__(self, name, age):
        # We can use PlayerCharacter4 instead of self here like this too.
        if PlayerCharacter11.membership:
            # Attributes (Dynamic Attribute) and (There is no change for our attribute)
            self.name = name
            self.age = age

    # What is self?
    def shout(self):
        return self

    # What is cls?
    @classmethod
    def adding_things(cls, num1, num2):
        return cls

    # It's exact like class method, except we don't have access to the cls or class, so we can't instantiate a class with it.
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player13 = PlayerCharacter11("Latina", 23)

print(f"self in player13 is{player13.shout()}")
print(f"player13 is{player13}")
print(f"cls in player13 is {player13.adding_things(2, 3)}")
print(f"PlayerCharacter11 is {PlayerCharacter11}")

# Important: So cls is our class and self is our object that was instantiated by our class.

# Note that if we return cls.name or cls.age on line 345, we will get error, because our actual class don't access to them. But cls has acces to an attribute like membership or our static class and .... that our actual class has access too.

print("###################################")

# Instance vs. Static vs. Class Methods in Python: The Important Differences

# Before We Begin: Understanding Decorator Patterns
# Decorators are simply functions. You can write them yourself, or use those included in libraries, or the Python standard library.

# Like any function, decorators perform a task. The difference here is that decorators apply logic or change the behavior of other functions. They are an excellent way to reuse code, and can help to separate logic into individual concerns.


class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print("Hello World!")

    @staticmethod
    def example_function():
        """ This method is decorated! """
        print("I'm a decorated function!")


de = DecoratorExample()
de.example_function()

# Decorators have to immediately precede a function or class declaration. They start with the @ sign, and unlike normal methods, you don't have to put parentheses on the end unless you are passing in arguments.

# It's possible to combine multiple decorators, write your own, and apply them to classes as well, but you won't need to do any of that for these examples.

print("###################################")

"""

1) Instance Methods in Python

Instance methods are the most common type of methods in Python classes. These are so called because they can access unique data of their instance. If you have two objects each created from a car class, then they each may have different properties. They may have different colors, engine sizes, seats, and so on.

Instance methods must have self as a parameter, but you don't need to pass this in every time. Self is another Python special term. Inside any instance method, you can use self to access any data or methods that may reside in your class. You won't be able to access them without going through self.

Finally, as instance methods are the most common, there's no decorator needed. Any method you create will automatically be created as an instance method, unless you tell Python otherwise.

"""


class InstanceExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print("Hello World!")
        self.name = "Decorator_Example"

    def example_function(self):
        """ This method is an instance method! """
        print("I'm an instance method!")
        print("My name is " + self.name)


de2 = InstanceExample()
de2.example_function()

# The name variable is accessed through self. Notice that when example_function is called, you don't have to pass self in---Python does this for you.

print("###################################")


"""

2) Static Methods in Python

Static methods are methods that are related to a class in some way, but don't need to access any class-specific data. You don't have to use self, and you don't even need to instantiate an instance, you can simply call your method:

"""


class StaticExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print("Hello World!")

    @staticmethod
    def example_function():
        """ This method is a static method! """
        print("I'm a static method!")


StaticExample.example_function()


# The @staticmethod decorator was used to tell Python that this method is a static method.

# Static methods are great for utility functions, which perform a task in isolation. They don't need to (and cannot) access class data. They should be completely self-contained, and only work with data passed in as arguments. You may use a static method to add two numbers together, or print a given string.

print("###################################")


"""

3) Class Methods in Python

Class methods are the third and final OOP method type to know. Class methods know about their class. They can't access specific instance data, but they can call other static methods.

Class methods don't need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by Python.

Class methods are created using the @classmethod decorator.

"""


class ClassExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print("Hello World!")

    @classmethod
    def example_function(cls):
        """ This method is a class method! """
        print("I'm a class method!")
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print("Hello!")


de3 = ClassExample()
de3.example_function()


# Class methods are possibly the more confusing method types of the three, but they do have their uses. Class methods can manipulate the class itself, which is useful when you're working on larger, more complex projects.


"""

When to Use Each Method Type?

Even if you only write tiny scripts for fun, learning another OOP feature of Python is a great skill to know, and can help to make your code easier to troubleshoot, and easier to reuse in the future.

In summary:

1) Instance Methods: The most common method type. Able to access data and properties unique to each instance.

2) Static Methods: Cannot access anything else in the class. Totally self-contained code.

3) Class Methods: Can access limited methods in the class. Can modify class specific details.

"""


print("###################################")


# 4 Pillars of OOP :


# 1) Encapsulation

"""

Encapsulation is binding of data and functions that manipulate that data and we encapsulate it into one big object. So that we keep everything in this box that users or code or other machines can interact with. With Encapsulation we packaged these data and function up into a blueprint, so that when other people see our code, they know  hey this is an entire object that we can interact with. Using this way We're combining things, packaging things up into those instances, into those boxes that can be useful. Note that when we create an object, for example a string, because of the Encapsulation, we have all these functionality available to us, all these method that we can access. (I mean when we write for example <"hello".> and then after <.> we will access to those methods.). Also remember that if for example our bottom class doesn't had any actions like speak and run and just had attributes like name and age, well in that case, it's kind of dictionary, and it's kind of useless. So that our class should have attributes and methods together. At the bottom we see that without actions and methods our class and dictionary are almost same and useing our class here is kind of useless.

Examlpe of our class without any methods: 

class EncapsulationExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = EncapsulationExample("Haika", 21)

print(a.name) # Haika
print(a.age)  # 21

Examlpe of dictionary: 

b = {'name': 'Haika', 'age': 21}

print(b['name']) # Haika
print(b['age'])  # 21

"""


class EncapsulationExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old.")


a = EncapsulationExample("Haika", 21)

a.speak()


print("###################################")


# 2) Abstraction

"""

Abstraction means hiding of information or abstraction away information and giving access to only what's necessary. In bottom example, abstraction can be seen in our speak method in lines 590 and 591. When we do b.speak() in line 596, we're seeing abstraction in action, because when I click Run, I get the result, but when I call speak method, I don't really care how speak is implemented, It's abstracted away from us. All I know is that b has access to the speak method and I can use it.

"""


class AbstractionExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old.")


b = AbstractionExample("Haika", 21)

b.speak()


print("###################################")


# Public and Private variables :


class PrivacyExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old.")


c = PrivacyExample("Haika", 21)

c.speak()

c.speak = "This is bad."

# print(c.speak())
# TypeError: 'str' object is not callable

print(c.speak)


print("###################################")


"""

In the top code we saw that we modified our speak method and it is a string now, and we can't call it, because it's modified to a string and when we print that, we can see the change. The idea behind abstraction is that we hide away information and only give access to things that a user is concerned about. So ideally we shouldn't have access to __init__(), We shouldn't be able to modify run or speak function and modify name and age. So can we make a private variable in our class? So, some languages allow us to have private variables. For example in a language like Java, we can actually say <private name or private age> and say that these attributes are private and we won't able to access and modify them. But in python there is no true privacy, no true private variables. So how do we get arround this? Well, what we would do is write underscore (_) before our variables. Now does this give any special power? No, This is just a convention as a python programmer, We determind that, hey if we see underscore in our code, that most likely means that this should be a private variable. 

"""


class PrivacyExample2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old.")


d = PrivacyExample2("Haika", 21)

d.speak()


print("###################################")


"""

    But if I try to overwrite and modify this (line 682) and then click run, this still modifies. That's becaise like I sead there is no true privacy. And this underscore means that you shouldn't touch and modify this variable. But you can still be bad and do somthing like bottom. So if you ever want to keep a method or attribute private, you just put an underscore before it, but it's no gurantee.

"""


class PrivacyExample3:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old.")


e = PrivacyExample3("Haika", 21)

e.speak()

e.speak = "This is bad."

print(e.speak)


print("###################################")


# 3) Inheritance


"""

Inheritance allows us new objects to take on the properties of existing objects. So you can inherit classes.

We want to create a new game and have different types of users. So we have users that can be wizards, users that can be archers. But all these users have some common functionality and each on of the subusers like wizards, archers and ... have some common shared functionality but then again different attacks.

We have a User class that has a sign_in method. You might be wondering and ask, where is the __init_ method here? Shouldn't we have that __init__ method that gets run first? Well, we could, but if we don't have any variables or attributes that we want to assign to the user, well in that case we wouldn't need an __init__ method. Note that we up until now define our classes without brackets, but here we saw that we can do that. And we will see that if we want our class to inherit from another class we need these brackets, so now, we know that we can define our class this way too.

Now we want to create a bunch of subclasses like Wizard and Archer. Ideally all these wizards and archers are users as well. Our users have multiple forms. They can be archers, they can be wizards and .... But all of them have to be signed in first.

User:
    Wizard
    Archer

How can we make sure that all of these users or classes also have access to sign_in method? Well, we can use inheritance. And how do we do inheritance? It's quite easily. All we do is in the brackets pass the parent calss (User class in here) that we want to inherit from like bottom.

The idea of inheritance is really really powerlful. And the key here is that we a parent class (User) and children classes (Wizard and Archer). Sometime these children classes are called subcalsses or drived classes, because they're subclasses of parent (User) or drived from the parent class (User).



Python gives us a useful tool to check if something is an instance of a class and it's called isinstance. isinstance is a built in function in Python.

Syntax:

isinstance(instance, class)

"""


class User():
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: Arrows left: {self.num_arrows}")


wizard1 = Wizard("Merlin", 55)
archer1 = Archer("Robin", 33)

wizard1.sign_in()
archer1.sign_in()

wizard1.attack()
archer1.attack()


print("###################################")


print(isinstance(wizard1, Wizard))

print(isinstance(wizard1, Archer))

print(isinstance(wizard1, User))
# Wizard class is a subclass of User class. So technically yes, wizard1 is an instance of User.

print(isinstance(wizard1, object))
# When we write wizard1. , we see a lot of methods with __ . Where to these Dunder methods (methods that start with __ ) come from? Remember that everything in Python is an object and everything in Python inherits from the base object class that Python comes with and it's called object. So they are from object class.


print("###################################")


# 4) Polymorphism


"""

What polymorphism means? poly means many and morphism means form. So it meand many forms.

This idea of polymorphism refers to the way in which object classes can share the same method name but those method names can act differently based on what object calls in.

For example at the bottom Wizard1 has a special meaning to it's attack versus Archer1. They're different. So although they share the same method names, because of objects that's calling it, the output is going to be different.

"""


class User1():
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard1(User1):
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Archer1(User1):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: Arrows left: {self.num_arrows}")


wizard2 = Wizard1("Merlin", 85)
archer2 = Archer1("Robin", 125)


def player_attack(char):
    char.attack()


player_attack(wizard2)
player_attack(archer2)

# Another way to demonstrate this is using for loop like bottom:

for char in [wizard2, archer2]:
    char.attack()

# We saw that we have two different outputs even though we're calling the same method. It's because of the different objects. And it's a really powerfull concept, because we're able to customize this according to our specific needs.

print("###################################")


"""

Let's say that the User2 had a attack method and this default attack method prints "do nothing". Even if we run this (line 866), if I click run, it's going to overwrite whatever the original or default attack was, because we already have that method in our Wizard2 class.

Let's say we wanted to have both User2 and Wizard2 run the attack method. How can we do this? We can say User2.attack(self) in our attack method in Wizard2 class (Line 855) and because we accept the User2 as our parameter in here (Line 849). We will talk about Line 855 more, a little bit later.

So polymorphism allows us to have many forms. It is the ability to redefine methods for these drived classes (Wiazar2 and Archer2) and an object that get instantiated can behave in different forms, in different ways based on polymorphism and this is useful because we are able to modify our classes to our specific needs, but also not have to repeat ourselves in case we want to use something like attack from User2 inside of Wizard2.

"""


class User2():
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard2(User2):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User2.attack(self)
        print(f"Attacking with power of {self.power}")


class Archer2(User2):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: Arrows left: {self.num_arrows}")


wizard3 = Wizard2("Merlin", 88)
archer3 = Archer2("Robin", 133)

wizard3.attack()


print("###################################")


# A Good Exercise:

class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add nother Cat

class Cati(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 2 Create a list of all of the pets (create 3 cat instances from the above)


simon = Simon('Simon', 4)
sally = Sally('Sally', 5)
cati = Cati('Cati', 3)

my_cats = [simon, sally, cati]

# 3 Instantiate the Pet class with all your cats use variable my_pets

my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance

my_pets.walk()


print("###################################")


# super()


"""

If in bottom code we run and print wizard4.email, we will get an error that says Wizard3 has no attribute 'email' like bottom. But we thought the User3 is going to be called when we create the wizard when we instantiate wizard4. Well the thing is although we might inherit the sign_in function from the User3 (Line 982), the Wizard already has __init__ function, already a constructor. So how can we solve this? we will see that at the bottom.

"""


class User3():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard3(User3):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard4 = Wizard3("Merlin", 888)

# print(wizard4.email)
# AttributeError: 'Wizard3' object has no attribute 'email'

wizard4.sign_in()


print("###################################")


"""

One way is to just add email here (Line 998) and just have the email attribute right down here (Line 1001). But what's the problem with this. Well it's inefficient. Because if we create an Archer class, we'll have to do the same thing.

"""


class User4():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard4(User4):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard5 = Wizard4("Merlin", 479, "merlin@gmail.com")

print(wizard5.email)

print("###################################")


"""

There is a more efficient way of doing what we did at the top. Well, we want to call the __init__ method of the User5 from inside our Wizard5 __init__ method (Line 1037). Because everytime we instantiate a new wizard, well, this __init__ method (Line 1036), is going to be called. So for doing like that is do like bottom.

"""


class User5():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard5(User5):
    def __init__(self, name, power, email):
        User5.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard6 = Wizard5("Merlin", 329, "merlinmagic@gmail.com")

print(wizard6.email)


print("###################################")


"""

There is another and best way of doing what we actually did at the top. And it's called super(). And with super(), we actually no longer need to the self like we did at the top (line 1037). So our code looks even cleaner. super() allows us to refer to User6 this way and not have to worry about passing self.

"""


class User6():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard6(User6):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard7 = Wizard6("Merlin", 777, "merlinwizard@gmail.com")

print(wizard7.email)


print("###################################")


# Introspection


"""

Introspection in computer programming means the ability to determine the type of an object at runtime (Runtime is when code is runnig). We can introspect an object and actually figure out what our code does as we're coding and then running. And Python allows us to do introdpection and inspect these objects with some nice helper functions. This one function is called dir. Look at the bottom code. dir will give me all of the methods and attributes that the wizard7 instance has. So with a dir function, we give it an instance and right away we get access to what it has access to. So this is really useful when you're trying to figure out what you have access to.

"""


print(dir(wizard7))


print("###################################")


# Dunder Methods


"""

We were able to see what our instance has as methods using the dir functon. And we saw some methods that start with double underscore ( __ ). These methods were inherited from our base object class. And these methods are our special methods. We have things like len() for example that allows us to tell the length of an array. This len() is actually implemented using these special methods that are called Dunder methods. They allow us to use Python specific functions on objects created through our class. 


If we using somthing like __str__() Dunder method that comes with our action_figure object and print that (Line 1134), we saw somthing like this (<__main__.Toy object at 0x0000025A3A917520>) and it's the exact same thing as doing str(action_figure) (Line 1335). These double underscore Dunder methods are special methods that Pythos recognizes. For example this __str__() Dunder method allows us to use action_figure like this (Line 1135), using the str built in function.

As a matter of fact if you go to the Python Documentation, under the special method names section, you'll see that we can do basic customizations of these Dunder methods. 

"""


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age


action_figure = Toy("Blue", 3)

print(action_figure.__str__())
print(str(action_figure))


print("###################################")


"""

We define our own str method here (Line 1168) and we're going to return the color of our object. And you see here that because we modified this, the str built in function now returns the color of the object. It doesn't change things other than with action_figur1 object that is an instance of class Toy2. If we run this (Line 1188) that is not from our Toy2 class, we will see that it still return action_figure1" because it's a string and not an object of our Toy2 class. So the str only modified when we use it on this specific object.

We can change the meaning of len() as well (Line 1171), and simply just return 5. But we said that it works like this on this specific object (action_figure1 that is from Toy2).

We can modify call (Line 1174) and when we call our object it returns "Yess??".

We also can change getitem (Line 1177) in our Toy2 class and then create a dictionary in our class and then return the values of dictionary with their keys like this (Lines 1196 and 1197).

We can modify del (Line 1180) and then del will print "deleted!" when we call it on our specific object that is from Toy2 class. Note that this del keyword I haven't really use in my programs, because it's not somthing that you see a lot and usually this can cause some funny bugs in our programs. But the del keyword delete some sort of variable that we might have had in our program.


So these special magic or Dunder methods are really interesting because it allows us to do some custom modifying of our class and you can also understand how in Python are built in default types had access and abilities to have all these special syntaxes. 

"""


class Toy2():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "Yes??"

    def __getitem__(self, i):
        return self.my_dict[i]

    def __del__(self):
        print("deleted!")


action_figure1 = Toy2("Blue", 1)

print(action_figure1.__str__())
print(str(action_figure1))
print(str("action_figure1"))

print(action_figure1.__len__())
print(len(action_figure1))
print(len("action_figure1"))

print(action_figure1())

print(action_figure1['name'])
print(action_figure1['has_pets'])

del action_figure1


print("###################################")


# Exercise Extending List:


"""

We want to create a SuperClass that return length of it with value of 1000 no matter what, and we want to our class has access to the power of a list. Look at the bottom codes:

"""


class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList()

print(super_list)

super_list.append(7)

print(super_list[0])
print(len(super_list))

print(issubclass(SuperList, list))
print(issubclass(list, SuperList))
print(issubclass(list, object))


print("###################################")


# Multiple Inheritance


"""

We want to create a class of character that have power and also have arrows. And we want to our character has access to all of these attributes and methods of Wizard7 and Archer7. So we create a class in the name of Ogre that inherits from Wizard7 and Archer7. We do this like this:          Ogre(Wizard7, Archer7). We can give it as many parameters as we want as multiple inheritances. 

So if we instance an ogre like this (Line 1272) and then call run method, we will get an error that says: TypeError: __init__() missing 2 required positional arguments: 'name' and 'power'. name and power.

So if we pass it the parameters (name and power) (Line 1277), we will see that our run method works well. But when we call check_arrows method, we will get this error: AttributeError: 'Ogre' object has no attribute 'arrows'. Why is that? Because technically we inherited from Wizard7 first then Archer7. And Wizard7 accepts name and power, but we never gave the arrows, I mean name and arrows of Archer7. So how can we solve this? So if we do like Line 283 and pass it 3 arguments and then call check_arrows method, we will get this error: TypeError: __init__() takes 3 positional arguments but 4 were given. So what we should do here?

"""


class User7():
    def sign_in(self):
        print("logged in")


class Wizard7(User7):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer7(User7):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")

    def run(self):
        print("Ran really fast!")


class Ogre(Wizard7, Archer7):
    pass


# ogre = Ogre()

# ogre.run()
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'power'.

ogre = Ogre("Medusa", 1000)

ogre.run()
# ogre.check_arrows()
# AttributeError: 'Ogre' object has no attribute 'arrows'

# ogre1 = Ogre("Medusa", 1000, 405)

# ogre1.check_arrows()
# TypeError: __init__() takes 3 positional arguments but 4 were given


print("###################################")


"""

So we can define an __init__ method for our Ogre1 class (Line 1326) and inside of it we call __init__ method of Archer8 and then pass in the name and arrows. With this our check_arrows method works. But if we call attack method, we will get this error: AttributeError: 'Ogre1' object has no attribute 'power'. So what we should do now?

"""


class User8():
    def sign_in(self):
        print("logged in")


class Wizard8(User8):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer8(User8):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")

    def run(self):
        print("Ran really fast!")


class Ogre1(Wizard8, Archer8):
    def __init__(self, name, power, arrows):
        Archer8.__init__(self, name, arrows)


ogre2 = Ogre1("Medusa", 1000, 405)

ogre2.check_arrows()
# ogre2.attack()
# AttributeError: 'Ogre1' object has no attribute 'power'.


print("###################################")


"""

So once again in order for us to have power, we'll have to do for Wizard9 what we did for Archer8 above (Line 1327). So now if we run this, we get no errors and our program works well and we has access to name, power and arrows.

So when we do multiple inheritance, things can get complicated. And this is why multiple inheritances is one of those things where it's really really powerful but with great power comes great responsibility. Because we're creating more and more complexity.

"""


class User9():
    def sign_in(self):
        print("logged in")


class Wizard9(User9):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer9(User9):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")

    def run(self):
        print("Ran really fast!")


class Ogre2(Wizard9, Archer9):
    def __init__(self, name, power, arrows):
        Archer9.__init__(self, name, arrows)
        Wizard9.__init__(self, name, power)


ogre3 = Ogre2("Medusa", 1000, 405)

ogre3.check_arrows()
ogre3.attack()
ogre3.sign_in()


print("###################################")


# MRO - Method Resolution Order:


"""

MRO or method resolution order is a rule that Python follows to determine when you run a method which want to run when you have such complicated inheritance structure. MRO is a rule that says hey do this, do this and then do that. And that's the method that you should run.   

        A
      /   \
     /     \
    B       C
     \     /
      \   /
        D   

If we print D.num what's happen? So if we click run, we get 1. Why? D inherits from B and C and then those inherits from A. Look at the structure  above. So we get 1 because the MRO is that it doesn't go D -> B -> A. Instead it goes D -> B -> C -> A. So MRO simply saying what's first in line, If things are common between classes, methods or variables or attributes, what should I pick?

There is good way to check this (Line 1431). It's mro method and if we run it, we will get the order or the MRO of this class (D class). It's going to say, hey, I'm going to check D first if you call let's say D.num, I'm going to check __main__.D (D class) and then I'm going to chaeck __main__.B (B class). Then I'm going to check __main__.C (C class) and then I'm going to check __main__.A (A class) and finally I'm going to check base class object.

"""


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


print("###################################")


"""

Now, if we pass all of these classes, and then run the program, we will get an error like this (Line 1463): AttributeError: type object 'D2' has no attribute 'num'. Because it went through all this path and even check the base object and never found num. But we did somthing like this __str__(Line 1465) and then run the progarm, our program works well and we will get this: <slot wrapper '__str__' of 'object' objects>. Because it goes all the way through the inheritance chain and then gets to the base object and the base object actually has this.


"""


class A2:
    pass


class B2(A2):
    pass


class C2(A2):
    pass


class D2(B2, C2):
    pass


# print(D2.num)
# AttributeError: type object 'D2' has no attribute 'num'.

print(D2.__str__)

print(D2.mro())
# [<class '__main__.D2'>, <class '__main__.B2'>, <class '__main__.C2'>, <class '__main__.A2'>, <class 'object'>]


print("###################################")


"""

We have another example of MRO at the bottom. And we use another way to call mro and is to use the Dunder mro method (Line 1507). Why we have this order here? So the order is because of the way that we're passing in the parameters. You see R is passed before O and Z (Line 1503). So that means the order of MRO is going to be R, then O and then Z. But we had X after R and O (Line 1508). Why did X come before Z? So this is because of the algorithm that they use for doing MRO which is called Depth First Search (DFS). 

Note that you're never going to get tested on this stuff. If you're writing code where the inheritance looks like bottom, I argue that you're writing bad code. Because this is overly complicated. So you should not structure your code in this way.

"""


class X:
    pass


class Y:
    pass


class Z:
    pass


class O(X, Y):
    pass


class R(Y, Z):
    pass


class M(R, O, Z):
    pass


print(M.__mro__)
# (<class '__main__.M'>, <class '__main__.R'>, <class '__main__.O'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)


print("###################################")
