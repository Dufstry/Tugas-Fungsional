import collections;
pieceses = collections.namedtuple('ChessPieces', ['color','piece'])

class ChessPieces:
    color = 'white black'.split()
    piece = [str(f'pawn{n}') for n in range(1,9)] + [str(f'rook{n}') for n in range(1,3)] + [str(f'bishop{n}') for n in range(1,3)] + [str(f'knight{n}') for n in range(1,3)] + [str('queen')] + [str('king')]

    def __init__(self):
        self._pieceses = [
                pieceses(color, piece) 
                    for color in self.color 
                    for piece in self.piece
            ]

    def __len__(self):
        return len(self._pieceses)

    def __getitem__(self, position):
        return self._pieceses[position]

    def __str__(self):
        return str(self._pieceses)


print(ChessPieces());