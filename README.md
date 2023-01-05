# ARA Project
Created on: 4/24/2022<br/>
Group 4: Tiana Cook, Jake Follett, Cristian Ion, Wanrong Qi, Jack White.



## About
ARA is an Assisted Reading Application that allows users to be able to take notes on different chapters of different books. It is meant to have a user take notes using the SQ3R (Survey, Question, Read, Recite, Review) method, but it can be used as a simple book note organizer as well. It has two text boxes, top and bottom, where questions can be written on the bottom text box and answers on the top text box. The top text box can be toggled to hide the answers from the user which allows the user to be able to quiz themselves on their questions.

# How to Run:

1. Establish a connection with MySQL\
  -I use [XAMPP Control Panel](https://www.apachefriends.org/download.html)  \
          -To use XAMPP: run XAMPP, start MySQL \
   -To see DBs in browser, also start Apache, and then click "Admin" for MySQL
2. Make sure that your MySQL password, the one in line 26 of database.py, and on line 16 of main.py match (or else connection will fail)
3. In terminal, once in the cis422-kanban folder, run "python3 .\ARA.py"



# How to Use:

1. Running the program opens up a Book Menu that uploads all of your previously created books. You can select an existing book or create a new one.
2. Next the program loads up all the saved chapters for that selected or new book. From here you can select an existing chapter or create a new chapter notes page.
3. Now the notes window appears for that chapter. You have the option to save and delete your notes. You can also create a new chapter straight from this window. A toggle quiz button will hide/show the top text from the top text box. There is also a toggle SQ3R button that reminds the user how to take notes in the SQ3R style.
