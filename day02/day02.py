# 100% Done
with open('input.txt') as f:  # Opens the file and get rid of '\n'
    data = f.readlines()

# Get all games in a dict[int,list[str,str,...]]
games = {i+1: x.strip().split(': ')[1].split('; ') for i, x in enumerate(data)}


class Colors:
    def __init__(self, games:str) -> None:
        self.games = games.replace(',', '').split()
        self.red = self.get_color('red')
        self.green = self.get_color('green')
        self.blue = self.get_color('blue')

    def get_color(self, color):
        """Get the color number by getting the index of the name of the color and going to the predecessor

        Args:
            color (str): the chosen color. In this exercise it's (red,green,blue)

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


# Part 2
class MinColor:

    def __init__(self, game_list: list) -> None:
        self.reds = []
        self.greens = []
        self.blues = []
        for g in game_list:
            color = Colors(g)
            self.reds.append(color.red)
            self.greens.append(color.green)
            self.blues.append(color.blue)
        
        self.minimum_colors = (max(self.reds),max(self.greens),max(self.blues))

    @property
    def power(self):
        p = 1
        for c in self.minimum_colors:
            p*=c
        return p


def minimum(games_dict = games):
    total = 0
    for g in games_dict.values():

        color = MinColor(g)
        total+= color.power
    return total
print(minimum())