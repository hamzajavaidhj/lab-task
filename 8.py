class Game:
    def __init__(self):
        self.values = [1,2,3,4,5,6,7,8,9,10]

    def generate_moves(self, node_index):
        return [node_index * 2, node_index * 2 + 1]

    def min_max(self, depth, node_index, maximizing_player):
        if depth == 0:
            return self.values[node_index]

        if maximizing_player:
            best_value = float('-inf')
            for move in self.generate_moves(node_index):
                value = self.min_max(depth - 1, move, False)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = float('inf')
            for move in self.generate_moves(node_index):
                value = self.min_max(depth - 1, move, True)
                best_value = min(best_value, value)
            return best_value

# Example usage
game = Game()
depth = 2
result = game.min_max(depth, 0, True)
print("The best value move generation is:", result)
