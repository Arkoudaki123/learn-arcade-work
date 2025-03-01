class Dog:
    def __init__(self, dog_name):
        self.name = dog_name
        print("A new dog is born!")


 def main():
     my_dog = Dog("Johnny")
     print("The dog's name is: ", my_dog.name)

main()
