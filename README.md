    AirBnB Clone Command Interpreter

 Description

This project is an implementation of a command-line interpreter (CLI) for an AirBnB clone. The command interpreter allows users to interact with an underlying database of AirBnB-like objects, such as users, places, states, cities, amenities, and reviews. Users can perform various operations, including creating, displaying, updating, and deleting objects within the database.

  Command Interpreter

The command interpreter, named `console.py`, provides a user-friendly interface for interacting with the AirBnB database. It is built using Python and utilizes the `cmd` module for command parsing and execution. The interpreter offers a set of commands to perform CRUD operations on the database, as well as other utility commands for managing and querying objects.

 How to Start

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/your_Hussein380/AirBnB_clone.git


2. Navigate to the project directory:


cd AirBnB_clone


3. Run the command interpreter:


./console.py


How to Use

Once the command interpreter is running, you can enter commands at the prompt (`hbnb`) to interact with the AirBnB database. The available commands include:

create: Create a new instance of a specified class and print its ID.

show: Display the string representation of an instance based on its class name and ID.

destroy: Delete an instance based on its class name and ID.

all: Print the string representation of all instances or instances of a specific class.

count`: Retrieve the count of instances of a given class.

update`: Update attributes of a specific instance based on its class name, ID, and attribute name.

Examples

Here are some examples of how to use the command interpreter:

1. Creating a new user instance:


(hbnb) create User
```

2. Showing details of a specific user instance:


(hbnb) show User <user_id>


3. Deleting a user instance:

(hbnb) destroy User <user_id>
```

4. Displaying all instances of a specific class:


(hbnb) all Place
```

5. Updating attributes of a user instance:


(hbnb) update User <user_id> email "example@example.com"

6. Retrieving the count of instances of a given class:


(hbnb) count City



