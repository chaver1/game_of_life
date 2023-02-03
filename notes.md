# DEVELOPMENT NOTES

## RULES OF GAME OF LIFE

- Any live cell with 0 or 1 live neighbors becomes dead due to underpopulation
- Any live cell with 2 or 3 live neighbors stays alive due to its neighbors being just or right
- Any live cell with 3 live neighbors becomes alive due to reproudction
- Any live cell with >3 live neighbors becomes dead due to overpopulation

## Function Development

### Render Function Potential Iterations

-Color Choice ability to input color choice as optional param from default

-Character-Choice; ability to input choice of characters to represent 0s and 1s

## In-Development Notes

### State-Change Function

-given cell can have as few as two neighbors or as many as four neighbors. These neighbors can be left, right, up, or down from a given cell. Cells on the borders of the state matrix have at most three neighbors, while internal cells can have at most 4 neighbors depending on matrix structure.

-a given cell must always know the status of each neighbor, a binary value of either "dead" or "alive". This is easily programmed by allowing each cell to be associated with 1(alive) or 0(dead), or an alternate symbol; however using int is easiest I believe

### Validation-Code

-only need to have validation code of inputs of board_state_transform because inputs. Validating input at random_state level assumes
that random state will be used always as an initial board. In reality certain custom initial matrices may need to be inputed or retrieving previous states from
a data struct if developed further. So any validation prior to board_state_tranform is redundant since it will have to be validated at transform-stages or else
nonapplicable matrices may never get caught.

### Random Board Testing

-need to figure out how to test a random function. Entropy is a plausible measure.
