# Study Sessions
#### Video demo:
#### Description: 

Study Sessions is a web app designed to help manage your time. It's written in HTML with javaScript and CSS. It's buildt so it can be set up in any way you need. It was inspired by online time trackers. I use one set up using the pomodoro technique (25 minutes of work with 5 minute breaks) but I found it cumbersome having to start each pomodoro manually.

## Files breakdown

Study Sessions is made of three files: Timer.html, style.css and bell1.mp3.
- **Timer.html**: This stores the code of the program. It's written both in HTML and JavaScript. 
- **Style.css**: The CSS used in Timer.html.
- **bell1.mp3**: online bell sound designed by [ADD CREDIT FROM METADATA]

## How it works

### Initial set up

The first thing the user sees is the Setup window. In here there are two options: Start a new set of timers or load a previous session. By pressing the **Load Saved Timers** button the program will show the users saved session and can load one by picking a name. Next to the name is a **Delete** button that will delete that session. A message will show confirming this action but the user here has the option to undo this by pressing the **undo** button on the message. If the user has no sessions saved the button just displays the message "No timers saved". 

The software will ask the user for the ammount of timers that will be used. One timer is made of three elements: minutes, seconds (both a positive integer) and a checkbox labeled as **continuous**. the program is coded so each timer has to be started manually by default, by checking continuous the program starts the next timer once the current one runs out, this can be changed at any moment. This input only accepts numbers from 1 to 99, anything else will show an error message. The value of this input is stored in a variable called *nTimers*. 

Next you have **all continuous?**. If this checkbox is marked it will set the continuous property of each timer of the session as true. So when the timers are rendered all the continuous checkboxes of each one will be set to true. Is possible to change this later when the the timer is running.

Finally, pressing **Setup** will render a table the size of the integer stored in *nTimers* in the user can set up the minutes and seconds of every timer. If the user changes the number and presses the button again the program will update the number of timers on screen.

The timers will be rendered from top to bottom. The values from the first row are the values for the starting timer.

The next step is entering the value of each element of the timers. By defaul each numeric element of the timers is set to 0 so, if the user leaves the input unchanged it will render that value as 0. The numeric inputs only takes positive two digit integers, minutes top value is 99 while seconds is 60. The third column, labeled as continuous, allows the user to which timer will be activated manually and which one will be automatic. 

The final checkbox, labeled as **Loop timers**, tells the program to restart the session from the first timer once the last one is completed. 

By pressing **Load** the program renders the user settings. If there's any non-valid value on any input the program alerts the user and deletes the wrong value. When every value is correct, the program stores the user settings in an object called *saveTimers*. 

### Main timer

Here's the final result. On top is the first timer with its corresponding *continuous* value. Next are the buttons for interacting with the current timer:
- **Start**: begins the timer.
- **Stop**: pauses it. 
- **Next**: passes to the next timer in line.
- **Reset**: sets the timer to its starting value and pauses it.
- **Save Timer**: Allow to save the current session. The program stores each timer in order with both their respective *continuous* value and the state of the loop variable. The first time is pressed a input will appear where the user must enter a name for the session. Press the button again to save. 
- **Back**: Return to the setup window. This will reset every value the user added before. 

On the bottom of the page are displayed in order all the following timers with a checkbox that shows the *continuous* stated setup on the previous step, this values can be modified by clicking on the checkboxes. When a timer is done a sound plays. If *loop timers* was checked before, a message appears after the final timer saying "Loop timer: On". If *loop timers* was left unchecked, once the final timer is done ...

## Code breakdown

Study Sessions is buildt around an object: *saveTimers*. Its an global object that stores the value of every timer, its respective *continuous* and *loop* value and, when **btnSave** is pressed, a name and unique ID used to save and load the session. This object is used for rendering, and saving, the users input. I'll divide this section in two: how data is stored in *saveTimers* and how is read.

### Getting data in

// The body of the program is made from five divs, a navbar and a footer. The divs acts as containers are organised into two sections, the top one that includes *first-div* and *first-button, and the second one made of *second-div*, *bottom-buttons* and *bottom-text*.

*first-div* contains the input *num-timers* that takes a positive integer ... // 

The first value that the program needs is the ammount of timers the user will create. This is handled by *num-timers* contained inside *first-div*. The input takes a positive integer up to 99. //Pressing the **Setup** button sets in motion the first value for *saveTimers*//. The value added by the user is stored in a variable called *nTimers*. This variable is then validated, if its an incorrect value an error message is shown, the value is deleted and the function returns.    

The function then makes *bottom-buttons* visible It makes a copy of *nTimers* called *delTimers* that is used by the function *nextTimer*. The function inside **btnSetup** creates a table in *second-div* that its going to be used for sending the values necessary for each timer. The body of the table is assembled by making the same ammount of rows using a for loop that ends when *i* reaches the same value in *nTimers*. Each element inside a row has an indidivual id that's made of both a name(either *timerMin*, *timerSec* or *set-check*) and a number that is the value of *i* at the moment the row is created. 

Pressing the **Load** button calls the function *timerLoad*. First, a variable called *errorLoad* is created and is set to false, the variable is set to true whenever a wrong value is found by the function. This function goes into every row, by a for loop, checking every numeric value and check state and storing it inside *saveTimers* with its corresponding ID number. If an incorrect value is found *addAlert* is called displaying an error message, deleting the corresponding value and setting *errorLoad* to true. If an error is found *errorLoad* is set to false and the function returns before finishing. 

By this point *saveTimers* has all the information it needs. The next step is to render the corresponding information into working timers. This is handled by another function called *renderTimers* and its triggered by *timerLoad* after finishing the previous check. The final thing this function does is make visible the buttons used in the next step, hide the buttons that are not needed and change the style of *second-div* to accomodate the new timers. 

### Reading the data

*renderTimers* is the function in charge of reading the users data stored in *saveTimers* and render the resulting timers with its corresponding continuous state. It firsts creates a variable(*firstHTML*) for the HTML that will replace the content on *first-div*. *renderTimers* redrawns the input circle and gives it a new function. It now works as a container for the running timer (current-timer is the named used on the code). Inside the container two p tags are inserted, the first to handle the minutes(with the id *timerMin*) and the second for seconds (*timerSec*). This ensures that the mechanism of timer runs independently of the values it holds. When the current timer is done, the software looks for the next timer and replaces the numbers and continuous state on the one stored at *first-div*. Every time a number is used in this section the function *padZero* is called which adds a leading zero when necessary. Next, a if statement is used to check the continuous state of the first timer, or if the user selected that all timers must be set to continuous. 

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

- *numbNextTimer* : Numeric. Used for function *nextTimer* ...

#### Next button 

**btnNext** has an if statement that makes sure that there is a timer to replace the current one. It checks if *numbNextTimer* is not the same as *nTimers* 
...
## Functions

### addAlert

Takes a string and turns it into an alert displayed at the bottom of the page. After five seconds the alert fades out. It first creates a variable for storing the *bottom-text* container. A second variable is then made that stores the ammount of elements inside *bottom-text*, this is used on the next line for assigning an unique ID to every message so it can be deleted by anothen function inside this one called *delText*. The function takes the input text and places it between p tags with an unique ID, it's then added to *bottom-text* and this container is scrolled to the new message always appears at the bottom. Each message invokes a function stored inside called *delText*. This function finds the alert created and deletes it after five seconds. The function is stored inside *addAlert* so every message is individualy erased. 

### addAlertundo

Takes 