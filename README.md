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

Study Sessions is buildt around an object: *saveTimers*. This object is used for rendering, and saving, the users input. I'll divide this section in two: how data is stored in *saveTimers* and how is read.

### Getting data in

