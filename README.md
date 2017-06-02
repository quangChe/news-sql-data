# Logs Analysis -- Analyzing Large-Scale News Data

This app utilizes PostgreSQL to analyze over 1.6 million rows of news data in order to
provide statistical reports addressing 3 questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Tools Required:

In order to run this program you need to first set up a virtual machine to run an SQL database
server on your machine. Please download the correct version for your machine and follow their installation instructions
for these three files:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - software for running a virtual machine
* [Vagrant](https://www.vagrantup.com/downloads.html) - software that configures the virtual machine
* [VM Configuration Files](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip) - files for configuring the virtual machine with Vagrant
* [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) - file containing the database we're going to be working with

## How to set up virtual machine:

**Note:** Do not make any changes to the python or SQL files or errors may occur.

1. After successfully installing all the files above, unzip the VM Configuration Files which will unload
the **FSND-Virtual-Machine**
2. Unzip the News Database file from above and move the **newsdata.sql** file into **/FSND-Virtual-Machine/vagrant**
3. From your Terminal, navigate into **/FSND-Virtual-Machine/vagrant** and run the command: *vagrant up*  (you only need to perform this step once unless you restart your LOCAL--not virtual--machine)
4. Wait for initial setup of the virtual machine to finish
5. Once the virtual machine has started, log into it using: *vagrant ssh*
6. You should now be connected to the virtual machine, which is equipped with a server for the PostgreSQL database that we will use for this app

## Starting up the app:
1. Clone or download the files from this repository into **/FSND-Virtual-Machine/vagrant** directory  (same directory as the **newsdata.sql** file)
2. You should have your virtual machine set up and logged in using *vagrant ssh* on your Terminal if you've gotten this far
3. In the terminal, which is now the VM environment, navigate into **/vagrant**
4. You should be able to see the **newsdata.sql** and **newsdb.py** files in here
5. Run the app using: *python newsdb.py*
6. The results should be printed
7. If correct, the results should match the view shown in the **sample_output.rtf** file from this repository
