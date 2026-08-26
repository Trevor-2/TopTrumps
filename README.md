GCSE
COMPUTER SCIENCE
Component 3 Programming project task
For candidates entering for the June 2019 8520 examination.
To be issued to candidates on 1 September 2018 or as soon as possible after that date.
Time allowed
 20 hours
Instructions
 Evidence must include a complete listing of all program code together with a report. The report
should describe the design of the solution, the testing and any potential enhancements and
refinements to the solution.
 Students must use one of the following programming languages:
 C#
 Java
 Pascal/Delphi
 Python
 VB.Net
Information
 The project is designed to be completed in 20 hours.
 The allocated time is not required to be continuous.
 There are restrictions on when and where students can work on this problem. Please see the
Teachers’ Notes which accompany this task for more information about these restrictions.
 Students may need to use the Internet to research certain parts of the problem. This must be
within the 20 hours.
 Submission may be paper based or electronic using CD/DVD.
 Students will need to complete and sign a Candidate Record Form which declares that the work is
their own. This must be countersigned by the teacher.
 Copyright permission is granted by AQA to use the copyright in the materials on the condition that
such use is limited strictly to the personal use by each teacher and their students for the purpose of
the preparation for and conduct of the programming project task only. The materials are not to be
provided to anyone other than the teacher and the students undertaking the task. The teacher
must collect this task back from the students at the end of each session. The use of the materials
for the production and publication in any format of teaching materials or any other such material
(other than for the teacher’s personal use) is strictly forbidden.
8520/CA/CB/CC/CD/CE
IB/G/Jun19/E1

2
Celebrity Dogs Game
A program needs to be created that allows the user to play Celebrity Dogs, a round-based category
comparison card game.
There is a pack of cards with each card in the pack representing a famous dog. The following details
about the dog appear on the card:
 The name of the dog.
 A value between 1 and 5 that indicates how much exercise the dog does, with 1 being the
least amount of exercise and 5 the most amount of exercise.
 A value between 1 and 100 that indicates the intelligence of the dog, with 1 being the least
intelligent and 100 being the most intelligent.
 A value between 1 and 10 that indicates the friendliness of the dog, with 1 being the least
friendly and 10 being the most friendly.
A value between 1 and 10 that indicates the amount of drool the dog produces, with 1 being
the least amount of drool and 10 being the most amount of drool.
How does the game work?
The game is played against the computer. The game consists of a series of rounds. The player is
asked to enter the number of cards in the pack. The pack of cards is dealt out with the player and the
computer receiving half the cards in the pack each.
The player is shown their first card and they choose a category: exercise, friendliness, intelligence or
drool.
The computer’s first card is then revealed and the value for the chosen category compared to the
value on the player’s card.
If the category chosen was exercise, friendliness or intelligence then:
 if, for the chosen category, the player’s card is equal to or higher than the computer’s card
then both cards are put at the bottom of the player’s pile of cards
 if, for the chosen category, the player’s card is lower than the computer’s card then both cards
are put at the bottom of the computer’s pile of cards.
If the category chosen was drool then:
 if the player’s card is equal to or lower than the computer’s card then both cards are put at the
bottom of the player’s pile of cards
 if the player’s card is higher than the computer’s card then both cards are put at the bottom of
the computer’s pile of cards.
If the player won the comparison then they won that round and the next card from their pile is
revealed and they choose a category for the round.
If the computer won the comparison then they won that round and the next card for both the player
and the computer are revealed. The computer then randomly selects a category for the round.
The game continues until the player or the computer have no cards left in their pile. The winner of
the game is the player who has all the cards in their pile.
IB/G/Jun19/8520/CA/CB/CC/CD/CE

3
The program should work in the following way:
1 A menu is displayed allowing the user to select from the following options:
 Play Game
 Quit.
2 If the user selects the ‘Quit’ option then a suitable message should be displayed and the
program ends.
3 If the user selects the ‘Play Game’ option they are asked to enter the number of cards to be
played. If the entered number is less than 4 or greater than 30, or is an odd number, then an
appropriate error message is displayed, and the user returned to the menu.
4 The program should then read in the names of the dogs from the text file dogs.txt, creating a
card for each dog.
5 The program should randomly generate a value for each category for each dog using the
ranges described on page 2, adding them to each dog’s card.
6 The number of cards entered in task 3 are then separated into two equal piles, the player’s
pile and the computer’s pile. If you wish to extend your program further then the cards may be
shuffled before they are separated into two piles, however you do not have to do this.
7 The first card in the player’s pile is displayed and the user is asked to enter a category. The
categories are exercise, intelligence, friendliness and drool.
8 The first card in the computer’s pile is then displayed.
9 The value on the player’s card for the chosen category is compared to the value in the same
category on the computer’s card.
 If the category chosen is exercise, intelligence or friendliness then the higher value
wins the round.
 If the category chosen is drool then the lower value wins the round.
 If the values are the same then the player wins the round.
10 If the player wins the round then both cards are moved to the bottom of the player’s pile. If the
computer wins the round then both cards are moved to the bottom of the computer’s pile. An
appropriate message saying what the result of the comparison was and who won that round
should be displayed.
11 If the player or the computer now has all the cards then they have won the game and a
suitable message should be displayed. The program should return to the main menu.
12 Otherwise, the next round is played and the winner of the previous round chooses the
category.
 If the player won the previous round then the card that is now on the top of the
player’s pile is displayed and they are asked to choose a category.
 If the computer won the previous round then a random category is chosen. The cards
that are now on the top of the player’s and computer’s piles are displayed.
 The game continues until the player or the computer has won.
Turn over ►
IB/G/Jun19/8520/CA/CB/CC/CD/CE

4

EXAMPLE

Figure 1 shows an example of a pack of six cards.

Figure 1

| Dog name                 |     | Exercise  |     | Intelligence  | Friendliness  |     | Drool  |
| ------------------------ | --- | --------- | --- | ------------- | ------------- | --- | ------ |
| Annie the Afghan Hound   |     |           | 4   | 15            |               | 6   | 1      |
| Bertie the Boxer         |     |           | 5   | 50            |               | 9   | 9      |
| Betty the Borzoi         |     |           | 3   | 25            |               | 6   | 2      |
| Charlie the Chihuahua    |     |           | 2   | 30            |               | 2   | 2      |
| Chaz the Cocker Spaniel  |     |           | 2   | 80            |               | 9   | 4      |
| Donald the Dalmatian     |     |           | 5   | 65            |               | 7   | 3      |

The cards in the deck are separated into two piles.  The player’s pile now contains three cards as
shown in Figure 2.  The computer’s pile also contains three cards as shown in Figure 3.

Figure 2

| Dog name                |     | Exercise  |     | Intelligence  | Friendliness  |     | Drool  |
| ----------------------- | --- | --------- | --- | ------------- | ------------- | --- | ------ |
| Annie the Afghan Hound  |     |           | 4   | 15            |               | 6   | 1      |
| Bertie the Boxer        |     |           | 5   | 50            |               | 9   | 9      |
| Betty the Borzoi        |     |           | 3   | 25            |               | 6   | 2      |

Figure 3

| Dog name                 |     | Exercise  |     | Intelligence  | Friendliness  |     | Drool  |
| ------------------------ | --- | --------- | --- | ------------- | ------------- | --- | ------ |
| Charlie the Chihuahua    |     |           | 2   | 30            |               | 2   | 2      |
| Chaz the Cocker Spaniel  |     |           | 2   | 80            |               | 9   | 4      |
| Donald the Dalmatian     |     |           | 5   | 65            |               | 7   | 3      |

The player goes first and chooses the category drool. The player wins as the drool value of their first
card is less than the drool value of the first card in the computer’s pile.  Figure 4 shows the
comparison made.

Figure 4

| Card Category  |                         | Player Card  |     |     | Computer Card          |     |     |
| -------------- | ----------------------- | ------------ | --- | --- | ---------------------- | --- | --- |
| Name           | Annie the Afghan Hound  |              |     |     | Charlie the Chihuahua  |     |     |
| Exercise       |                         |              | 4   |     |                        | 2   |     |
| Intelligence   |                         |              | 15  |     |                        | 30  |     |
| Friendliness   |                         |              | 6   |     |                        | 2   |     |
| Drool          |                         |              | 1   |     |                        | 2   |     |

IB/G/Jun19/8520/CA/CB/CC/CD/CE

5
As the player won the round the player’s card and the computer’s card are placed at the bottom of
the player’s pile. Figure 5 shows the player’s pile at the end of the round and Figure 6 shows the
computer’s pile at the end of the round.
Figure 5
Dog name Exercise Intelligence Friendliness Drool
Bertie the Boxer 5 50 9 9
Betty the Borzoi 3 25 6 2
Charlie the Chihuahua 2 30 2 2
Annie the Afghan Hound 4 15 6 1
Figure 6
Dog name Exercise Intelligence Friendliness Drool
Chaz the Cocker Spaniel 2 80 9 4
Donald the Dalmatian 5 65 7 3
END OF PROGRAMMING PROJECT TASK
Copyright © 2018 AQA and its licensors. All rights reserved.
IB/G/Jun19/8520/CA/CB/CC/CD/CE
