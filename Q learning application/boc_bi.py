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
            move = player.make_move(self.sobi)
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

class AIPlayer:
    def __init__(self):
        self.q = defaultdict(lambda: DEFAULT_Q)
        self.sobi = None
        self.move = None
        self.EPSILON = EPSILON
        self.available_actions = None
        self.board = tuple()  # convert board to a tuple

    def make_move(self, sobi):
        self.board += (self.sobi,)  # append to the tuple
        if (sobi <= 4) & (sobi > 0):
            self.available_actions = list(range(1, sobi + 1))
        else:
            self.available_actions = ACTIONS 

        if random.random() < self.EPSILON:
            self.move = random.choice(self.available_actions)
        else:
            q_values = [self.get_q(self.board, a) for a in self.available_actions]
            max_q_value = max(q_values)
            best_actions = [i for i in range(len(self.available_actions)) if q_values[i] == max_q_value]
            best_move = self.available_actions[random.choice(best_actions)]
            self.move = best_move
        
        return self.move

    def get_q(self, state, action):
        return self.q[(state, action)]

    def reward(self, reward, state):
        st = tuple(state)
        if self.move:
            prev_q = self.get_q(st, self.move)
            max_q_new = max([self.get_q(st, a) for a in self.available_actions])
            self.q[(self.board, self.move)] = prev_q + ALPHA * (reward + GAMMA * max_q_new - prev_q)

class HumanPlayer:
    def reward(self, reward, state):
        pass

    def make_move(self, sobi):
        move = int(input('Nhap so: '))
        return move
    
if __name__ == '__main__':

    ai_player_1 = AIPlayer()
    ai_player_2 = AIPlayer()

    print('Training the AI player(s)...')

    ai_player_1.EPSILON = EPSILON
    ai_player_2.EPSILON = EPSILON

    for _ in range(50000):
        game = Tree1(ai_player_1, ai_player_2)
        game.play()

    print('\nTraining is Done')
    # epsilon=0 means no exploration - it will use the Q(s,a) function to make the moves
    ai_player_1.EPSILON = 0
    human_player = HumanPlayer()
    game = Tree1(ai_player_1, human_player)
    game.play()

