with open('input.txt') as f:  # Opens the file and get rid of '\n'
    data = f.readlines()

# Get all games in a dict[int,list[str,str,...]]
games = {i+1: x.strip().split(': ')[1].split('; ') for i, x in enumerate(data)}


class Colors:
    def __init__(self, games) -> None:
        self.games = games.replace(',', '').split()
        self.red = self.get_color('red')
        self.green = self.get_color('green')
        self.blue = self.get_color('blue')

    def get_color(self, color):
        """Get the color number by getting the index of the name of the color and going to the predecessor

        Args:
            color (str): _description_

        Returns:
            int: the color count for that game
        """
        if color not in self.games:
            return 0
        index = self.games.index(color)

        return int(self.games[index-1])


def is_possible(red=12, green=13, blue=14, game_dict=games):
    total = 0
    for game_id, g in game_dict.items():
        for game in g:
            colors = Colors(game)
            if colors.red > red or colors.green > green or colors.blue > blue:
                break
        else:  # If the loop doesn't break
            total += game_id
    return total


if __name__ == "__main__":
    print(is_possible())
