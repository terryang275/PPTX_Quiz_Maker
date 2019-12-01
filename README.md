# PPTX_Quiz_Maker
Makes Flashcards/Quiz automatically from pptx file.

## Description:
  This project will create fill in the blank flashcard questions using powerpoints that the user provides. The program will allow the user to either choose certain words to omit from the text (and thus create a blank), or randomize the word(s) that will be omitted on each side. The user will be quizzed and will need to answer the created questions. After answering the questions, a report will be generated which will display and compare the answers to the solutions and provide a final mark. Common words, such as the, it, there, etc, will be not be chosen for omission, as programmed into the system. The user can also add additional common words in the code as they please. This program is useful for studying as they are able to identify important points in their powerpoints and be quizzed on them.

## Main Project (main_code.py):
### All Requirements for Main Project:
1. python-pptx library 
2. random library
3. re library
4. numpy library

### All requirements for whole project (main_gui and main_code.py):
certifi==2019.11.28
chardet==3.0.4
docutils==0.15.2
idna==2.8
Kivy==1.11.1
kivy-deps.angle==0.1.9
kivy-deps.glew==0.1.12
kivy-deps.gstreamer==0.1.17
kivy-deps.sdl2==0.1.22
Kivy-Garden==0.1.4
kivymd==0.102.0
lxml==4.4.2
numpy==1.17.4
Pillow==6.2.1
Pygments==2.5.2
pypiwin32==223
python-pptx==0.6.18
pywin32==227
requests==2.22.0
urllib3==1.25.7
XlsxWriter==1.2.6


### Feature 1:
#### 1. Uploading Files:
#### Requirements
Uses pptx library to extract objects in powerpoint so we can later find the text and make flashcards.

#### 2. Extracting Highlighted text with <@ and @>:
#### Requirements
Text must be enclosed with <@ and @>.
Example: <@ Sample text in here will be isolated and random words in here will be ommited@>
Random text, but not in a list of common words.

#### 3. Extracting Highlighted text with <! and !>:
#### Requirements
Text must be enclosed with <! and !> and within <@ and @>
Example: <@ This is sample text <! text between this will be specifically blanked!>, if text is the text has partial markers like <! but no closing, then text will randomly be blocked rather than specifically blocked @>

#### 4. Error Checking:
#### Requirements
Will state which slide has the error if a <@ or @> is missing its other compliment

#### 5. QUIZ/FLashcard:
#### Requirements
a dictionary of the flashcard properties
example
flashcard = {Question #1: ["Original text,"Altered/Blanked Text",[words ommitted in sequenctial order]
             Question #2 :["Original text,"Altered/Blanked Text",[words ommitted in sequenctial order] ...
             }

by taking this dictionary in, we quiz the user using Altered text, we then later match the append their answer to the dictionary for the corresponding question.

flashcard = {Question #1: ["Original text,"Altered/Blanked Text",[words ommitted in sequenctial order],[User response],
             Question #2 :["Original text,"Altered/Blanked Text",[words ommitted in sequenctial order],[User response], ...
             }
We have added a SKIP option so that users can skip a question they found easy or too hard. Either circumstance, the user will recieve ZERO for any REMAINING blanks within the question.

#### 6. Validation and Report:
#### Requirements
flashcard = {Question #1: ["Original text,"Altered/Blanked Text",[words ommitted in sequenctial order],[User response],
             Question #2 :["Original text,"Altered/Blanked Text",[words ommitted in sequenctial order],[User response], ...
             }
for this process, we need the [words ommitted in sequenctial order],[User response] for each question so we can match and see how many equal each other.

We also append the score back to each question. Example: appending [0,1,0,1,1] where each element represents the score for the blank


## Side Project (main_gui.py):
#### 1. Uploading Files:
#### Requirements
1. A graphics card is needed to display GUI
2. Kivy has instruction on how to download and all dependencies required https://kivy.org/#home 
3. KivyMD (Kivy Material Design), simple pip install kivymd, and it an sister project of Kivy
4. .KV file (Apparently it is similar to CSS, but I haven't tried CSS before). The KV file allows editing and layout of application to be easier, instead of setting up code in python file. 

Picture sample and code will be included. If we had more time, we would have integrated our code into the GUI. For now, the GUI is a demonstration of what we would have done. 
