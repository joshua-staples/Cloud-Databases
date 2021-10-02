# Overview

The purpose of this project is to learn how to use cloud databases on a high level. Read, write, update, and query (view) were my main objectives. 

In this project I am using Google Firebase to explore cloud databases. I decided to make a very fundamental password manager that could store a login name, password, and username in a cloud database for future retreval.

My project uses command line prompt to get user input and then store that input. The data is stored in a 'Passwords' collection on the database, and a future feature would be to add multi-user support with firebase authentication. 

My purpose for writing this software was to create an achieveable project to complete in a two week time frame. Password managers already exist in many different forms, however, they are still a great tool for learning about how a cloud database functions. 

[Software Demo Video](https://youtu.be/Iev7sPTmaxY)

# Cloud Database

I am using Google Firebase for my cloud database. Google firebase is a very intuitive first time application development tool for cloud databases that has very thourough and useful documentation. 

My database has a 'Passwords' *collection*, which contains as many login name *documents* as a user inputs. Inside of each *document* there is a key-value pair of username and password. 

# Development Environment

Tools:
* VS Code
* Google Firebase
* Github

Language/Libraries:
* Python 3.9
* firebase_admin sdk

# Useful Websites

* [Google Firebase Documentation](https://firebase.google.com/docs)
* [Python Documentation](https://docs.python.org/3/)
* [Youtube Firebase Tutorial](https://www.youtube.com/watch?v=N0j6Fe2vAK4&t=3469s)

# Future Work

* Multi-user Authentication
* Better printing of passwords
* Integration into a web-app interface

### Contact

sta16016@byui.edu

