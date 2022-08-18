from connect4 import *
from model import *


player1 = Model()
game_list = torch.zeros((10, 42))
for i in range(10):
    win = False
    player = 0
    waiter = 1
    game = Connect4()
    while win == False:
        board = torch.flatten(torch.from_numpy(game.board)).float()
        if player == 0:
            move = player1.forward(board)

            played = torch.argmax(move)

        elif player == 1:
            played = np.random.choice(game.get_legal_actions())

        else:
            raise ValueError("player value must be 0 or 1")
        win = game.play(played)[0]
        player, waiter = waiter, player

    print_board(game)
    game_list[i] = torch.flatten(torch.from_numpy(game.history))


torch.save(game_list, 'game_history.pt')
