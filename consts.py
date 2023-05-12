INITIAL_POSITIONS = {
        "light_pieces": {
            "King": [(4, 0)],
            "Queen": [(3, 0)],
            "Rooks": [(0, 0), (7, 0)],
            "Bishops": [(2, 0), (5, 0)],
            "Knights": [(1, 0), (6, 0)],
            "Pawns": [(i, 1) for i in range(8)],
        },
        "dark_pieces": {
            "King": [(4, 7)],
            "Queen": [(3, 7)],
            "Rooks": [(0, 7), (7, 7)],
            "Bishops": [(2, 7), (5, 7)],
            "Knights": [(1, 7), (6, 7)],
            "Pawns": [(i, 6) for i in range(8)],
        }
}

print(INITIAL_POSITIONS["light_pieces"]["King"])