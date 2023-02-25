import random
from collections import defaultdict

ACTIONS = [1, 2, 3, 4]
SO_BI = 22
EPSILON = 0.3
ALPHA = 0.3
GAMMA = 0.9
DEFAULT_Q = 0


class Tree1:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.first = True
        self.board = [SO_BI]
        self.sobi = SO_BI

    def play(self):
        while True:
            if self.first:
                player = self.player1
            else:
                player = self.player2

            self.first = not self.first
            move = player.make_move(self.board)
            
            self.sobi -= move
            self.board.append(self.sobi)
            print(self.sobi)

            if self.sobi == 0:            
                winner = player
                loser = self.player2 if player == self.player1 else self.player1
                winner.reward(1, self.board)
                loser.reward(-10, self.board)
                print(f"Winner: {winner.__class__.__name__}, Loser: {loser.__class__.__name__}")
                break

class AIPlayer():

    def __init__(self, epsilon=0.4, alpha=0.3, gamma=0.9, default_q=0):

        self.EPSILON = epsilon
        self.ALPHA = alpha
        self.GAMMA = gamma
        self.DEFAULT_Q = default_q
        self.q = {}
        self.move = None
        self.board = tuple()

    # these are available or empty cells on the grid (board)
    def available_moves(self, board):
        return  [ACTIONS if board[-1]>4 else list(range(1, board[-1]+1))][0]

    # Q(s,a) -> Q value for (s,a) pair - if no Q value exists then create a new one with the
    # default value (=1) and otherwise we return the q value present in the dict
    def get_q(self, state, action):
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = self.DEFAULT_Q

        return self.q[(state, action)]


    def make_move(self, board):

        self.board += tuple(board)
        actions = self.available_moves(board)

        # action with epsilon probability
        if random.random() < self.EPSILON:
            # this is in index (0-8 board cell related index)
            self.move = random.choice(actions)
            return self.move

        # take the action with highest Q value
        q_values = [self.get_q(self.board, a) for a in actions]
        max_q_value = max(q_values)

        # if multiple best actions, choose one at random
        if q_values.count(max_q_value) > 1:
            best_actions = [i for i in range(len(actions)) if q_values[i] == max_q_value]
            best_move = actions[random.choice(best_actions)]
        # there is just a single best move (best action)
        else:
            best_move = actions[q_values.index(max_q_value)]

        self.move = best_move
        return self.move

    # let's evaluate a given state: so update the Q(s,a) table regarding s state and a action
    def reward(self, reward, board):
        if self.move:
            prev_q = self.get_q(self.board, self.move)
            max_q_new = max([self.get_q(tuple(board), a) for a in self.available_moves(self.board)])
            self.q[(self.board, self.move)] = prev_q + self.ALPHA * (reward + self.GAMMA * max_q_new - prev_q)

class HumanPlayer:
    def reward(self, reward, state):
        pass

    def make_move(self, sobi):
        move = int(input('Nhap so: '))
        return move
    
if __name__ == '__main__':

    ai_player_1 = AIPlayer()

    print('Training the AI player(s)...')

    ai_player_1.EPSILON = EPSILON

    for _ in range(100):
        game = Tree1(ai_player_1, ai_player_1)
        game.play()

    print('\nTraining is Done')
    # epsilon=0 means no exploration - it will use the Q(s,a) function to make the moves
    ai_player_1.EPSILON = 0
    human_player = HumanPlayer()
    game = Tree1(ai_player_1, human_player)
    game.play()

