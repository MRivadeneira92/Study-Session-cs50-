# Study Sessions
#### Video demo:
#### Description: 

Study Sessions is a web app designed to help manage your time. It's written in HTML with javaScript and CSS. It's buildt so it can be set up in any way you need. It was inspired by online time trackers. I use one set up using the pomodoro technique (25 minutes of work with 5 minute breaks) but I found it cumbersome having to start each pomodoro manually.

## Files breakdown

Study Sessions is made of the following files: 
- **index.html**: This stores the code of the program. It's written both in HTML and JavaScript. 
- **style.css**: The CSS used in Timer.html.
- **bell1.mp3**: online bell sound designed by user cdrk. From freesounds.org.
- **Figtree-ExtraBold.tff**: By Erik Kennedy. Font used on the page.
- **greenlogo.pgn**: By Andrea Morillo. Logo of the page. 

The design of the page was made by Andrea Morillo. I turned it into CSS and made some modifications to make it more user friendly.

## How it works

### Initial set up

The first thing the user sees is the Setup window. In here there are two options: Start a new set of timers or load a previous session. By pressing the **Load Saved Timers** button the program will show the users saved session and can load one by picking a name. Next to the name is a **Delete** button that will delete that session. A message will show confirming this action but the user here has the option to undo this by pressing the **undo** button on the message. If the user has no sessions saved the button just displays the message "No timers saved". 

The software will ask the user for the ammount of timers that will be used. One timer is made of three elements: minutes, seconds (both a positive integer) and a checkbox labeled as **continuous**. The program is coded so each timer has to be started manually by default, by checking continuous the next timer will start once the current one runs out, this can be changed at any moment. This input only accepts numbers from 1 to 99, anything else will show an error message. The value of this input is stored in a variable called *nTimers*. 

Next you have **all continuous?**. If this option is checked it will set the continuous property of each timer to true. So when the timers are rendered all the continuous checkboxes will be set to true.

Finally, pressing **Setup** will render a table the size of the integer stored in *nTimers*. In here the user can set up the minutes and seconds of every timer. If the user changes the number and presses the button again the program will update the number of timers on screen.

The timers will be rendered from top to bottom. The values from the first row are the values for the starting timer.

The next step is entering the value of each element of the timers. By defaul each numeric element of the timers is set to 0 so, if the user leaves the input unchanged it will render that value as 0. The numeric inputs only takes positive two digit integers, minutes top value is 99 while seconds is 60. The third column, labeled as continuous, allows the user to set which timer will be activated manually and which ones will be automatic. 

The final checkbox, labeled as **Loop timers**, tells the program to restart the session from the first timer once the last one is completed. 

By pressing **Load** the program renders the user settings. If there's any non-valid value on any input the program alerts the user and deletes the wrong value. When every value is correct, the program stores the user settings in an object called *saveTimers*. 

### Main timer

Here's the final result. On top is the first timer with its corresponding *continuous* value. Next are the buttons for interacting with the current timer:
- **Start**: begins the timer.
- **Stop**: pauses it. 
- **Next**: passes to the next timer.
- **Reset**: sets the timer to its starting value and pauses it.
- **Save Timer**: Saves the current session. The program stores each timer in order with both their respective *continuous* value and the state of the loop variable. The first time is pressed an input will appear where the user must enter a name for the session. Press the button again to save. 
- **Back**: Return to the setup window. This will reset every value the user added before. 

On the bottom of the page are displayed, in order, all the following timers in the session, each with its their *continuous* value. When a timer is done *bell1.mp3* is played alerting the user. If *loop timers* was checked before, a message appears after the final timer saying "Loop timer: On". Once the last timer has finished the session stars again (if Loop timers was on) or the session stops. 

## Code breakdown

Study Sessions is buildt around the object *saveTimers*. Its an global object that stores the value of every timer, its respective *continuous* and *loop* value. This object is used for rendering, and saving, the users input. I'll divide this section in two: how data is stored in *saveTimers* and how is read.

The body of the program is made of five divs, a navbar and a footer. The page can be divided into two: the top section where the circle div is stored, made of *first-div* and *first-buttons*, and the bottom section made of *second-div*, *bottom-buttons* and *bottom-text*. 

### Getting data in

The first value that the program needs is the ammount of timers. This is handled by *num-timers* contained inside *first-div*. The input takes a positive integer up to 99. The value added by the user is stored in a variable called *nTimers*. This variable is then validated, if its an incorrect value an error message is shown, the value is deleted and the function returns.    

The function then makes *bottom-buttons* visible. It makes a copy of *nTimers* called *delTimers* that is used by the function *nextTimer*. The function inside **btnSetup** creates a table in *second-div* that its going to be used for sending the values necessary for each timer. The body of the table is assembled by making rows using a for loop that ends when *i* reaches the same value in *nTimers*. Each element inside a row has an indidivual id that's made of both a name(either *timerMin*, *timerSec* or *set-check*) and a number that is the value of *i* at the moment the row is created. 

Pressing the **Load** button calls the function *timerLoad*. First, a variable called *errorLoad* is created and is set to false, the variable is set to true whenever a wrong value is found by the function. When this happens *addAlert* is called displaying an error message, deleting the corresponding value and setting *errorLoad* to true. After every value is checked, the function returns before *timerLoad* is finished. Before the data can be read the value of *loadSkip* is checked. If the variable is set to true that means that *saveTimers* already has data loaded so the code can skip the loading. *loadSkip* is false by default and its set to true when the session loop or if a session is loaded from local memory. *timerLoad* then goes into every row, using a for loop, checking every numeric value and check state and storing it inside *saveTimers* with its corresponding ID number.

By this point *saveTimers* has all the information it needs. The next step is to render the corresponding information into working timers. This is handled by another function called *renderTimers* and its triggered by *timerLoad* after finishing the previous check. The final step is making visible the buttons used when the timer is running, hide the buttons that are not needed and change the style of *second-div* to accomodate the new timers. 

### Reading the data

*renderTimers* is the function in charge of reading the users data stored in *saveTimers* and render the resulting timers. It firsts creates a variable (*firstHTML*) for the HTML that will replace the content on *first-div*. *renderTimers* redrawns the input circle and gives it a new function. It now works as a container for the running timer (current-timer is the name used on the code). Inside the container two p tags are inserted, the first to handle the minutes(with the id *timerMin*) and the second for seconds (*timerSec*). This ensures that the mechanism of the timer runs independently of the values it holds. When the current timer is done, the software looks for the next timer and replaces the numbers and continuous state on the one stored at *first-div*. Every time a number is used in this section the function *padZero* is called which adds a leading zero when necessary. Next, a if statement is used to check the continuous state of the first timer, or if the user selected that all timers must be set to continuous. 

A new variable is made for storing the HTML of the rest of the timers (*nextHTML*). A loop is used for reading the data from *saveTimers* for the remaining timers and for renderning a container, inside are two p tags, one for minutes and one for seconds, along with a checkbox for the continous state. Each timer is rendered in order. 

Finally. The HTML is injected into the corresponding div, if *loopTimers* is set to true a message reading "Timer Loop: on" is added after the last timer, and the timer is ready to be used. 

## Counting down

### How it works

#### Main function

The mechanism behind Study Sessions lies in the function *downTimer*. Inside this function is the countdown mechanism itself called *timerStart*, a function that triggers a setInterval() method that runs every second. It first stores the two values on the current timer at separate variables that second. The value for the second is substracted 1, if the result is -1 means that a minute has passed so 1 is substracted from *min*. After the values are calculated ...  

The rest of the function has triggers for **btnStop** and **btnBack**, both stops the timer by calling clearInterval on *timerStart* and setting *timerOn* to false. 

The last part of *timerStart* is reserved for what happens when the current timer reaches 00:00. Play() is called which reproduces an sound when the timer is completed, clearInterval(timerStart) stops the timer and an alert is created. Then the continuous status of the current timer is checked by first creating a variable (*check0*) that stores the value on the current timer check, after that an if statement is used to pass onto the next timer: If the continuous value is checked and if there is another timer after the current one, then load the next timer calling the function *nextTimer* and start the new timer by calling *downTimer*. The final part is the looping functionality. An if statement listen for *loopTimers* and if *timerPass* has the same value as *nTimers*, meaning that there a no more timers after the current one. If the conditions are met then all timers are reset by rendering the page again (by calling *renderTimers*) and setting returning the values from *ceroTimer*, *numbNextTimers*, *delTimers* and *timerPass* to their default values. 

There a number of global variables inside that keep track of the state of the timer. They are designed so other functions and buttons don't trigger *downTimer* when it shouldn't. Ej: The counter running twice. 

- *timerOn*: Boolean. Set to true when the timer is running. It's used with **btnStart** to make sure only one instance of *downTimer* is running. Is set to false by stopping the timer either with **btnStop**, **btnBack** or when the timer runs out.

- *timerPass*: Numeric. Keeps track of the current timer running. It begins at 0 and adds 1 whenever the current timer ends. It's only used for looping the session. If *loopTimers* is true and *timerPass* is the same number as *ntimers* then the session is looped. 

- *backTimer*: Boolean. False by default. It's changed to true when **btnBack** is pressed. When it's true triggers *clearInterval(timerStart)* stopping the timer and then is returned to false by the code in the button. 

- *ceroTimer*: Boolean. False by default. Changes to true when the current timer is at 00:00. It was created for making sure *downTimer* only is called when the current timer has values that it can count down from. 

- *numbNextTimer* : Numeric. Used for function *nextTimer*. It stores the numeric position of the timer that follows the current one. 

- *delTimers*: Numberic. Used for function *nextTimer*. At the start of the session holds the same value as *nTimers* but is counts down every time a timer is completed or passed. In *nextTimer* is employed for rendering the remaining timers by being the number for the condition to finish the loop. 

#### Next button 

**btnNext** has an if statement that makes sure that there is a timer to replace the current one. It checks if *numbNextTimer* is not the same as *nTimers*. If the condition is met then the function *nextTimer* is called. This function is in charge of updating the values on the current timer to the next one on *saveTimers*. It stores the direction of the inner HTML of the current timer minutes and seconds by looking for their respectives IDs, it takes the values of the following timer by accessing their respective propeties using the ID given by *numbNextTimer*. The continuous status is also updated by looking at the value next on the rendered page, this is done because the user might change the value from the setup. The list of the remaining timers is rendered with a for loop using *delTimers* as the top value. *delTimers* is subtract#ed by 1, *timerFinish* is set to false, *numbNextTimers* and *timerPass* are added 1 and the last element in the remaining list is deleted. 

#### Reset button

**btnReset** replaces the values on the current timer with the corresponding one on *saveTimers* ...

#### Saving sessions

**btnSave** is used to save the current session on local memory. The button does two things. First it renders a input box for the user to name the current session and changes the state of the variable *saveBtnFtn* to true. Pressing the button again saves the session with the name on local memory. The name is stored in the variable *saveName*.In order to save the session two new values are added to *saveTimer*: length and id. Length is storing the value of *nTimers* and ID is an unique number created by adding one to the ammount of sessions stored locally (*localStorage* + 1). Sessions need an ID for the undo function when they is deleted from local memory.  The session is saved by running JSON.stringify on *saveTimers* alogn with *saveName*. *saveBtnFtn* is changed to false, an alert confirms that the session was saved and the input tag is deleted. The final stage is updating the dropdown menu from the setup page. This is done by creating a new div with the id recently made. In this div two buttons are stored: the first is the button for selecting the saved session. Each button has the id of the currrent session, the name in the function *dropdownSelect* and the name of the session, the second button is used to delete the saved session, inside the button tag is the function *dropdownDelete* with the name and id of the session. This last container only exist for the correct implementation of the dropdown menu if the **btnBack** is pressed. The next time Study Sesssion is loaded or if the page is refleshed, the dropdown menu will be rendered from local memory. The last two lines delete the length and id properties from *saveTimers*. 

#### Back button

**btnBack** is the last button from the current timer page. Its function is to get back to the setup page from the current timer without reloading the page. This button changes the state of *backTimer* to true, triggering one of the if statements on *timerStart* that stops the timer mechanism. *saveTimers* contents are deleted. The div contained in *first-div* is replaced by the original circle container, the buttons are hidden by changing their display values to "none". Lines 121 to 126 return those values to their default state. The last lines insert to *first-div* and *second-div* their original HTML. 

### Loading from local storage

To access the saved sessions a function is run when the window is loaded. The first thing this functions does is store the keys(names) of every session stored by using a loop using the length of *localStorage* in a variable called *timerNames*. An if stated is used to check if there are any saved sessions. In case there aren't a p tag with the text "no timers saved" is injected into the *user-selection* div. If there are sessions saved then the code runs a for loop from 0 up until the length of *timerNames*. A variable called *menuHTML* is created for storing the HTML of the dropdown menu. For every cicle of the loop a container is made that host two buttons. The first button is used for loading the correct data from memory, this is done by adding an onclick function called *dropdownSelect* with the name of the session as its input. The second button deletes the previous sessions. This button also has an onclick function called *dropdownDelete* which takes the name of the session and its ID as input. At the end of every loop the container is added to *menuHTML*. When the loop is completed the HTML is send to *user-selection*. Finally an alert is created welcoming the user. 

#### dropdownSelect, dropdownDelete and Undo

These two functions are used to interact with the information in *localStorage*.
*dropdownSelect* : Takes a name as an input. This function loads into *saveTimers* the data stored in localStorage by using the name as a key. The information is parsed with JSON. *saveTimers* length is stored in *nTimers*. The *loadSkip* function is set to true because *timerLoad* will be called at the end of this function. 

*dropdownDelete*: Takes a name and a number. It moves the corresponding saved session from local storage into session storage so it can be recalled later if the user wants to recover it but, once the browser is closed, the session is deleted. This function calls a second function named *addAlertUndo* which generates a message similar to *addAlert* but with a undo button inside. The input data from localStorage is saved into a variable called *tempData* and then saved into session storage. The original data is deleted from local storage. Using the number input the containers that hold the buttons for loading the information are removed. Finally a copy of the session is saved into an object called *arrayUndo* using the name as key. This object is used when multiple sessions are deleted, with this object the undo function can restore any individual session.  

*undoTimer*: Takes a name as an input. Restores to local storage a deleted timer by coping the session from *arrayUndo* back to local storage. The first line of the function does this by grabbing the session using the name as key in *arrayUndo*, using JSON.stringify to turn the data into a string and using the same name to save tore it back into local storage. An alert is sent. The session is deleted from session storage. The button for selecting and deleting the session are added back to the dropdrown menu using the information from *arrayUndo*. After the HTML is added into *user-selection*, the session is deleted from *arrayUndo*.
...
## Functions

### addAlert

Takes a string and turns it into an alert displayed at the bottom of the page. After five seconds the alert fades out. It first creates a variable for storing the *bottom-text* container. A second variable is then made that stores the ammount of elements inside *bottom-text*, this is used on the next line for assigning an unique ID to every message so it can be deleted by anothen function inside this one called *delText*. The function takes the input text and places it between p tags with an unique ID, it's then added to *bottom-text* and this container is scrolled to the new message always appears at the bottom. Each message invokes a function stored inside called *delText*. This function finds the alert created and deletes it after five seconds. The function is stored inside *addAlert* so every message is individualy erased. 

### addAlertundo

Takes 