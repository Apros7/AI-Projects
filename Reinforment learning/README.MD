# Based on Kaggle course on Reinforcement Learning: Connect4 Agents
In this repo the following agents has been developed:
- A simple agent (no-step) looking at how the next step will affect their and the opponents chances of connecting 4
- A smarter agent (one-step) looking at not only the current, but also the next possible action and how that will affect the board state
- An even smarter agent (3-step) looking n (3 is used in my notebook) steps ahead

## Results:
A benchmark of a random model is used to ensure agents quality:
- All agents got 100% accuracy compared to the random agent
- One-step won 77% of games over no-step
- 3-step won 78% of games over no-step
- 3-step and one-step seemed to perform equally well: 3-step won 49% of games, one-step 45% of games, and 6% were draws.
It's funny how 3-step is about 25x slower than one-step yet does not achieve a noticeable difference in performance.