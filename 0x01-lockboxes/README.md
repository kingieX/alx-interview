# 0x01-lockboxes

## Task

<h2>0. Lockboxes</h2>

<p>You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
</p>

<h2>Solution</h2>

<p> The function works by starting with the first box (boxes[0]), which is already unlocked. It adds the keys in this box to a queue, and then starts processing the keys one by one.</p>

<p> If a key opens a box that hasn't been unlocked yet, the function adds the box to a set of unlocked boxes and adds the keys in the box to the queue. It continues searching for keys until the queue is empty. </p>

<p>At the end of the function, it checks whether the set of unlocked boxes contains all the boxes in boxes. If so, it returns True, otherwise it returns False.</p>
