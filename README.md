# dice-roll

A simple Python script that rolls some dice given a dice roll expression. 

## Format
Expressions must be of the following format:

```
AdB
```
where A is an integer value that describes the number of dice to be rolled, and B is an integer that describes the number of sides on the dice. These values don't have to be logical from a physical perspective.

## Output

For a given expression:

```
> 3d20
```

the output may be something like:

```
> 3d20
  Rolling 1d20... 1
  Rolling 1d20... 7
  Rolling 1d20... 20
TOTAL: 28 / 60
```

## Licensing

This program is licensed under the GNU General Public License v3.0. See the license for more details.
