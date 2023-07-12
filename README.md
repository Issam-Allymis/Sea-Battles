# Sea Battles

![Screenshot 2023-07-12 023955](https://github.com/Issam-Allymis/Sea-Battles/assets/126810074/0ba55347-5863-4520-b5f9-0ff96336f07f)


Sea Battles is a Python terminal game that runs in the Code Institute mock terminal on Heroku. It is a one-player game where the user aims to hit all the randomly placed ships on the board. Each battleship occupies one square on the board. Sea Battleship is a turn-based game where you, as the player, try to hit and sink all the battleships on the game board. The game board is a grid consisting of squares, and each square represents a coordinate on the board.

[Sea Battles🎮](https://sea-batt1es-affc65a93948.herokuapp.com/)

[Repository📁](https://github.com/Issam-Allymis?tab=repositories)
## How to play Sea Battles 🎲
The objective of the game is to sink all the battleships within ten turns. In each turn, you will guess a coordinate by providing the row and column numbers. The top left corner of the board is represented by row 0 and column 0, while the bottom right corner is represented by row 6 and column 6.

After making your guess, the game will provide feedback on whether your guess was a hit or a miss. If you hit a battleship, the corresponding square on the board will be marked with an 'X' (representing a HIT). If you miss, the square will be marked with an 'O' (representing a MISS). You will also receive a message indicating whether it was a hit or a miss.

The game will continue for a maximum of ten turns or until you have sunk all the battleships on the board. If you manage to sink all the battleships within ten turns, you win the game. Otherwise, if you reach the maximum number of turns without sinking all the ships, the game ends.

Throughout the game, you can refer to the game board to see your previous guesses and the results. The 'X' marks represent your hits, and the 'O' marks represent your misses.

## Features
### Current features 

![Screenshot 2023-07-12 022320](https://github.com/Issam-Allymis/Sea-Battles/assets/126810074/e50f9122-c5ef-459f-94f4-c7c9513dfc29)

- Game Initialization: The game initializes by asking for the player's name and displaying the board size and the total number of ships.

- Game Board: The game displays a board of a specified size, representing the sea battlefield. It shows the player's username at the top and visualizes the hits and misses on the board.

- Ship Placement: The game randomly places a specified number of ships on the board. Each ship occupies one square on the board.

![Screenshot 2023-07-12 025419](https://github.com/Issam-Allymis/Sea-Battles/assets/126810074/91166e4d-8824-4656-8e76-a49f0b00f12b)

- Input Validation: The game enforces the following input validation rules for player guesses:
  - You cannot enter coordinates that have already been guessed.
  - You cannot enter coordinates outside the size of the game board.
 
![Screenshot 2023-07-12 025419](https://github.com/Issam-Allymis/Sea-Battles/assets/126810074/9da6fdfc-1c0c-4ce3-9bfb-e0f3a8ac9dbf)


## Data Model
The Seaship_Battle class serves as the model for the Sea Battleship game. It plays a pivotal role in the game by defining and managing important aspects of the gameplay. This class allows for the configuration of essential game parameters, including the size of the game board and the number of ships. Additionally, it facilitates the storage and retrieval of crucial information, such as the player's name. By encapsulating these details, the Seaship_Battle class provides a structured representation of the game's data and rules, enabling seamless interactions and effective management of the game state.

## Testing 
I have manually tested my project.
- Passed the code through a PEP8 linter and can confirm that no errors were detected.
- Used print function to debug any problems that i met through the journey
- Tested in my local terminal in the Code Institute Heroku terminal

## Bugs
**Solved**
- I resolved the issue where the HIT and MISS markers were not displaying properly on the board. The previous implementation made the board difficult to read and understand which coordinates were being targeted. I resolved this problem by adding spaces around the ' X ' and ' O ' markers in the for loop. This adjustment improved the readability and organization of the game board, making it easier to identify the hit and miss coordinates.

### Remaining Bugs
- None

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
**Steps for deployment**:
- Clone or fork the repository.
- Create a new Heroku app.
- Set the buildpacks to *Python* and *NodeJS* in that exact order.
- Link the Heroku app to the GitHub repository.
- Click **Deploy**

Happy coding!

## Credits
- I would like to express my sincere gratitude to my senior personal tutor for their invaluable assistance in structuring and debugging my code. Their guidance and insights have been instrumental in improving the overall quality and organization of my code. Their tips and ideas have significantly contributed to my understanding of code structure and debugging techniques. I am truly grateful for their support throughout this process.
- Code Institute for the deployment terminal "Heroku" and for the invaluable information available on the course.
- I would like to extend my heartfelt appreciation to my family and friends for their unwavering support and patience during these challenging weeks of dedicated coding. Their understanding and encouragement have been invaluable as I immersed myself in this intense coding journey. Their belief in me and their willingness to provide the space and understanding I needed are truly cherished. I am grateful to have such amazing individuals in my life who stand by me as I pursue my passion.

# Disclaimer
***The Sea Battles Project Was Created Only For Educational Purposes.*** 📖
