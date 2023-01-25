# Logging
here we explain about our logs
___
## dungeon_and_dragon.py
___
### main
- Start the program
- Inside the main loop
    - If the user entered -register
    - If the user entered -login
    - If the user entered -help
    - If the user entered -exit
    - If the user entered -hint
    - If the user entered unauthorized command
    - end the program
### dash_register
  - Inside the register loop
      - If the user entered -return
      - If the user entered -exit
      - If the user entered -help
      - If the user entered -hint
      - If the user entered Duplicate Username
      - The user successfully registered
### dash_login
  - Inside the login loop
  - If the user entered -return
  - If the user entered -help
  - If the user entered -hint
  - If username was classified
  - If the password is wrong
  - When you enter the wrong password 3 times, you will be banned
  - And the username is not in the database
### get_level
  - Inside the level loop
    - If the user entered -easy
      - When the user does not have enough money
      - The user enters the game sections
    - If the user entered -normal
      - When the user does not have enough money
      - The user enters the game sections
    - If the user entered -hard
      - When the user does not have enough money
      - The user enters the game sections
    - If the user entered -adv
    - If the user entered -logout
    - If the user entered -help
    - If the user entered -hint
    - If the user entered unauthorized command
### easy_level
  - Inside the easy level loop
    - When the user loses the game
    - or won
### normal_level
  - Inside the normal level loop
    - When the user loses the game
    - or won
### hard_level
  - Inside the hard level loop
    - When the user loses the game
    - or won
### read_database_file
  - Start and end of reading database information
### write_database_file
  - Start and end of writing database information
___
## game_function.py
___
### draw_map
  - Start and position of the character
  - Drawing the map is finished
### allowed_direction
  - When the allowed directions are listed at the end
### move_dragon
  - If the dragon chooses the left side
  - If the dragon chooses the right side
  - If the dragon chooses the up side
  - If the dragon chooses the down side
  - If the dragon chooses random side
  - or the dragon did not move
___
## other_func.py
___
### dash_help
  - Start and end -help
### dash_exit
  - Start and end -exit
### dash_adv
  - Start and end -help
### loading_logo
  - Start and end -help
### loading_icon
  - Start and end -help