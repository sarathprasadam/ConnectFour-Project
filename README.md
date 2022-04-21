
# ConnectFour-Python cmd Gaming Application


This is command prompt based connecte four 2 player application where number of rows,columns or pieces can be selected by user.

## Features

- Variable no of rows,columns,pieces
- Game can be stopped by typing END in keyboard



## Deployment

Clone this repository

```bash
  git clone https://github.com/sarathprasadam/ConnectFour-Project.git
```
Connect to this directory ie ConnectFour-Project (cd  ConnectFour-Project)

Run py connect_four.py to run the program.

## Documentation

The Win check is done by following Method.

First of all the position of player is stored in a variable. ie if player in row 3 and column 4 then [3,4] is stored.

Then 4 Checks are performed:

1)Horizontal Check:- it include 2 sub check.

Firstly Right side of Position. Now column number is increased by keeping rows fixed.Counter is increased until a not filled position or other player position appears or until column no is less than total columns. 

Secondly Left Side of Position.For that column number is decreased while keeping row fixed.Counter is increased until a not filled position or other player position appears or column no become 0. 


Finally, Counter is checked with no of pieces. If Counter is greater than or equals to no of pieces player wins.

2)Verticle Check:- it include 2 sub check.

Firstly Top side of Position. Now Row number is increased by keeping Column fixed.Counter is increased until a not filled position or other player position appears or until row no is less than total rows. 

Secondly Bottom Side of Position.For that row number is decreased while keeping column fixed.Counter is increased until a not filled position or other player position appears or row no become 0. 


Finally, Counter is checked with no of pieces. If Counter is greater than or equals to no of pieces player wins.

3)North-West to South-East Check:- it include 2 sub check.

Firstly North West side of Position. Now Row number is increased and  Column no decreased.Counter is increased until a not filled position or other player position appears or until column no become 0. 

Secondly South East Side of Position.For that row number is decreased and column no increased.Counter is increased until a not filled position or other player position appears or row no become 0. 


Finally, Counter is checked with no of pieces. If Counter is greater than or equals to no of pieces player wins.

3)North-East to Souht-West Check:- it include 2 sub check.

Firstly North East side of Position. Now Row number is increased and  Column no increased.Counter is increased until a not filled position or other player position appears or until column no is less than no of columns. 

Secondly South West Side of Position.For that row number is decreased and column no decreased.Counter is increased until a not filled position or other player position appears or row no become 0. 


Finally, Counter is checked with no of pieces. If Counter is greater than or equals to no of pieces player wins.
