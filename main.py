from maze_game import MazeGame

if __name__ == "__main__":
    bad_points = [
        (115, 120), (164, 95), (189, 95),
        (215, 164), (274, 192), (221, 240)
    ]
    start = (90, 60)
    goal = (310, 260)

    game = MazeGame("Labirint.png", start, goal, bad_points)
    game.run()