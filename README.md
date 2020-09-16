# Header Buttons
This addon allows you to create custom buttons and buttons templates for Blender, they will be displayed in the header.
![image](https://user-images.githubusercontent.com/1472884/93373026-0cddea00-f855-11ea-9877-df3d3913d81a.png)


Quickly switch between shelves to ahve actions for different tasks at hand.
![shelves_switching](https://user-images.githubusercontent.com/1472884/93270182-d353a300-f7b0-11ea-9d6b-9a25267c1ef2.gif)

##Addon Preferences Description
![image](https://user-images.githubusercontent.com/1472884/93374529-1e27f600-f857-11ea-9a2a-18437e385f89.png)



## Create a new button
1. go to the user preferences of blender, navigate to the Interface section and enable "Developer Extras"
![image](https://user-images.githubusercontent.com/1472884/93373229-5a5a5700-f855-11ea-917d-526707c86f64.png)

This will allow you to copy the operator from belnders UI elements
![image](https://user-images.githubusercontent.com/1472884/93373392-8d9ce600-f855-11ea-87f8-fe52faf7cc39.png)


2. Go to the Shelves addon preferences and use the + button on the right side to add a new button, by default this will add a button with a hearth icon and a operator to open the user preferences
![Screen Shot 09-16-20 at 07 49 PM](https://user-images.githubusercontent.com/1472884/93373704-ff752f80-f855-11ea-810a-d128ed605632.PNG)

3. Navigate to the Icon Viewer Addon and open the Icon Viewer, select the icon you want and copy the Icon String over to your Icon Field in the Shelves addon.
![image](https://user-images.githubusercontent.com/1472884/93374820-8d9de580-f857-11ea-9458-0dcde4d527f5.png)
![image](https://user-images.githubusercontent.com/1472884/93374990-cccc3680-f857-11ea-8d1d-e24b93a706d0.png)

4. Give your Button a Name
![image](https://user-images.githubusercontent.com/1472884/93375278-3ba98f80-f858-11ea-8801-fbfbf8f9c1e3.png)


5. Navigate to the action you want to bind to that button and copy the python command
![image](https://user-images.githubusercontent.com/1472884/93376337-baeb9300-f859-11ea-9296-4b2fe5635fe4.png)

Paste the python command in the operator field and remove the brackets at the end and the parts in the front (this might vary a bit from operator to operator)
![image](https://user-images.githubusercontent.com/1472884/93377132-ea4ecf80-f85a-11ea-80b3-523dfa0b226e.png)

6. save you rnew Shelve
![image](https://user-images.githubusercontent.com/1472884/93377610-87aa0380-f85b-11ea-99ee-bbf7b4ed2e5b.png)
![image](https://user-images.githubusercontent.com/1472884/93378096-3c442500-f85c-11ea-8068-447c9b7aec86.png)







