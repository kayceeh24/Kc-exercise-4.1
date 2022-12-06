# Exercise 4.1 - Validate Grade

In this assignment, you will create a program that reads a percent grade from the user, validates it, then prints out its level grade.

## Requirements

Write a program that asks for a a percent grade (an integer), which must be between 0 and 100.  If the grade is invalid, repeatedly print the error `Invalid grade! Try again.` and then ask for the grade again.

The program should print the level grade that corresponds with the percent grade based on this table:

| Percent Grade | Level Grade |
|:---:|:---:|
| 0 to 49 | R |
| 50 to 59 | 1 |
| 60 to 69 | 2 |
| 70 to 79 | 3 |
| 80 to 100 | 4 |

**Sample Execution #1**

```
Enter a percent grade: 62

62% is Level 2
```

**Sample Execution #2**

```
Enter a percent grade: -18
Invalid grade! Try again.
Enter a percent grade: -18
Invalid grade! Try again.
Enter a percent grade: 88

88% is Level 4
```

## Submitting

When you are finished, push your code to GitHub.  Submit it on [Gradescope](gradescope.com) where it will be graded:
* Correctness - 80% (automatic)
* Style - 20% (manual - see [Style Guide](https://mrdevet.github.io/ICS3C/assignments/Style-Guide/))

## Resources

The following lessons will be helpful with this exercise:

* **[Repeating Code](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/1-Repeating-Code/)**
  * [Intro to While Loops](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/1a-While-Loops/)
* **[Loops and Data](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/2-Loops-and-Data/)**
  * [Looping Input](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/2b-Looping-Input/)
