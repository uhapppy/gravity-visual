# gravity-visual
simulation of gravity for great visual

# keys feature
   * 3 color setting
  * a lot of parameter to play with
  * possiblility to create custom ring system
  * real time simulation
  
  # setting explain
  ## star setting
  
  * x , y , z coordonate -define the position of the star
  * mass    -define the mass of the star
  * size  - define the size of the star
  
  ## general setting
  
  * grid    -if checked will show a grid
  * pxmode  -if checked activate the pxmode
  * trace   -if checked the planet will leave a trace behind them 
  * collision   -if checked will activate the collision mode inn this mode if a planet touch the star the star absorb the planet and get bigger
  * g value   -change the value of gravity force
  * time value -change the time interval high value will run faster but will be less precise low value run slower but more precise
  
  ## color setting
  
  * random -each planet will have a random color
  * depend on scalar speed    -each planet will have is color determine by is scalar speed in real time
  * depend on coord speed  -each planet will have is color determine by the speed of each of is coordonate (red=x, blue=y ,z=green) 
  
  ## ring setting
  
  * x,y,z coordonate -define the coordonate of the center of the ring
  * number of astre  -define the number of celestial corpse in the ring
  * distance of the center -define a wich distance from the center celestial corpse will be create
  * width of the ring  - define the width of the ring
  * speed - define the speed of the celestial corpse
  * angle of the ring -define the angle of rotation by the y axis of the ring
  * tickness of the ring -define the range in z value in which celestial corpse can be create
  
  ## camera setting
  
  * x,y,z -define the center of the camera
  * elevation -define the angle at which the camera will look
  * distance from center -define the distance from the center where the camera willl be
  * field of view -define the field of view can be change in real time
  
  # buttons explain
  
  * start simulation -will start a new simulation
  * stop simulation  -will erase everything and stop simulation
  * freeze movement  -will freeze the simulation in place
  * unfreeze movement -will unfreeze the simulation
  * clear ring -will erase all ring but the simulation will not stop
  
  * add ring -will add a ring with the current setting in the current simulation can be use to add ring in a already running simulation
  
  # instruction
  
  * 1   if you want the dark theme download the Geoos.qss file and change the directory on the line 610 or if you want to have the light theme just erase the line 610 to 613
  or you can download the .exe file here https://drive.google.com/file/d/1BwDfBA-ZGBHWdFt2N5isz2MAT77ZBMtM/view?usp=sharing (the .exe file its not working for everybody also with thee .exe file only light theme is available,also the label for the setting can be a little bit bugged but still very usable)
  
  * 2    to run a simulation just put the parameter you want for a ring then click add ring (before starting a simulation you always need to add a leats one ring)
  
  
  # NOTE
  
  the programm is not realy well optimized and python is note the best for simulation like that so you will have some limitation dependent on your hardware
  i test it on different computer
  * on a computer with a gtx 1660ti and i5 9600k and 16gb of ram the maximum body to have a fluid experience is about 2000 without trace and collision with collision is about 200 and with trace is about 200 too
  
  * on a computer with a intel graphic 620 , i5 8250u  and 8gb of ram the maximum body to have a fluid experience is about 400 without trace and collision with collision is about 150 and with trace is about 150 too
