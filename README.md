# Logs-Analysis
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

1)Install VirtualBox from here   https://www.virtualbox.org/wiki/Downloads

2)Install Vagrant from here https://www.vagrantup.com/downloads.html select according to your   operating system

3)Download the VM configuration

4)Start the virtual machine

  From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause   Vagrant to download the Linux operating system and install it. This may take quite a   while (many   minutes) depending on how fast your Internet connection is.

5)When vagrant up is finished running, you will get your shell prompt back. At this point, you can   run vagrant ssh to log in to your newly installed Linux VM!

  Inside the VM, change directory to /vagrant and look around with ls.

  The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to   the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

  Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only   inside the VM.

6)Running the database
  The PostgreSQL database server will automatically be started inside the VM. You can use the psql   command-line tool to access it and run SQL statements:

7)Download the data
  Next, download the data here 
  
  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

  You will need to unzip this file after downloading it. The file   inside is called newsdata.sql.   Put this file into the vagrant directory, which is shared with your   virtual machine.
  To load the data, use the command psql -d news -f newsdata.sql.


The above steps are to setup the software environment to run the project

------------------------------Here are the steps how to run the project after downloading the zipped folder-------------------------------------

1) unzip the folder then create the following views

   this view is required to display the most popular article authors of all time

   create view logs_analysis as select author,name,slug from articles join authors on articles.author=authors.id;


   
   
   these two views are required to display the On which days did more than 1% of requests lead to errors?

   create view  status_404 as select count(status) as status_count,date(log.time) as date1 from log where status='404 NOT FOUND' GROUP BY date1;
   create view  status as select count(status) as status_count,date(log.time) as date1 from log GROUP BY date1;

2) now run the newsdb.py  which is inside unzipped folder  using the command python newsdb.py
