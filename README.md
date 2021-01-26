# gravity-visual
simulation of gravity for great visual

# keys feature
   * 3 color setting
  * a lot of parameter to play with
  * possiblility to create custom ring system
  
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
  * clear ring will erase all ring but the simulation will not stop
  
  * add ring -will add a ring with the current setting in the current simulation can be use to add ring in a already running simulation
