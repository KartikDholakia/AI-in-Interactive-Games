# Chess AI using Negamax Algorithm

## Steps to run program locally
- Install virtual environment package:
    ```bash
    $ pip install virtualenv
	```

- Activate virtual environment:
    ```bash
    $ venv\scripts\activate
	```

- Run program
	```bash
	$ python chess.py
	```

#

## Negamax Algorithm

### Flowchart
![Flowchart for negamax algorithm](<negamax algo.png>)

#

## Optimizations applied:
### 1. Alpha Beta Pruning - 
The objective of alpha-beta pruning is to decrease the number of nodes to be evaluated by the algorithm. This prunes those branches of the tree which cannot affect the final result. 
### 2. Transposition Table - 
This is a dictionary that stores board positions that have already been evaluated during the
search process. When searching the game tree, often two different pathways can result in the same
board being evaluated. Instead of evaluating the same board several times, the program stores the
values of each board position in the transposition table with the keys being the positions. This way,
repeated positions can have their evaluations looked up fairly quickly as the board state is hashed.
### 3. Opening Table - 
This is a dictionary that stores board positions that are often seen in the beginning few moves of a
game of chess. The appropriate moves that can be played at such positions are stored in the dictionary. The opening
book is stored using the pickle module and can be read from or written to a file. The program also
allows for recording moves to the opening book, which can be done by setting the "isRecord" variable
to True.

#

## Video Demonstration
Link to the demo video: https://drive.google.com/file/d/1rp52c1CEorEJ-5VKQTPVDB3EdYeYokWf/view?usp=sharing