class Tile:
    def __init__(self, tile_type: str, position: tuple):
        self.tile_type = tile_type #has not come yet, but will be useful later
        self.position = position

    def __repr__(self):
        return f"Tile(type={self.tile_type}, position={self.position})"

    