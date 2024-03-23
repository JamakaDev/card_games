WIDTH = 1280
HEIGHT = 960
MIDDLE = (WIDTH//2, HEIGHT//2)

CARD_WIDTH = 96
CARD_HEIGHT = 128
CARD_SIZE = (CARD_WIDTH, CARD_HEIGHT)

MARGIN = 24
FPS = 60


POSITIONS = {
  # 108px DIFFERENCE || 1.125 CARD_WIDTH
  # 168px DIFFERENCE || 1.75 CARD_WIDTH
  'DECK': (MARGIN, 3*CARD_HEIGHT),
  'BURN': (2*CARD_WIDTH, 3*CARD_HEIGHT),

  'FLOP': ((3.75*CARD_WIDTH, 3*CARD_HEIGHT),(5.5*CARD_WIDTH, 3*CARD_HEIGHT),(7.25*CARD_WIDTH, 3*CARD_HEIGHT),),
  'TURN': (9*CARD_WIDTH, 3*CARD_HEIGHT),
  'RIVER': (10.75*CARD_WIDTH, 3*CARD_HEIGHT),
  
  'DEALER': ((2*CARD_WIDTH, MARGIN), (3.75*CARD_WIDTH, MARGIN)),
  'PLAYER': ((2*CARD_WIDTH, 6*CARD_HEIGHT-MARGIN), (3.75*CARD_WIDTH, 6*CARD_HEIGHT-MARGIN)),
  
  'SHUFFLE': (6*CARD_WIDTH, 6*CARD_HEIGHT-MARGIN),
  'DEAL': (8*CARD_WIDTH, 6*CARD_HEIGHT-MARGIN),
  'FOLD': (9.5*CARD_WIDTH, 6*CARD_HEIGHT-MARGIN),

  'DEAL_FLOP': (6*CARD_WIDTH, 6*CARD_HEIGHT+MARGIN),
  'DEAL_TURN': (8*CARD_WIDTH, 6*CARD_HEIGHT+MARGIN),
  'DEAL_RIVER': (9.5*CARD_WIDTH, 6*CARD_HEIGHT+MARGIN),
}


# O=Opponent Card, P=Player Card, D=Deck, B=Burn Cards, M=Muck, C=Check/Call, F=Fold, R=Raise
LAYOUT = [
  [' ',' ','O1','O2',' ',' ',' ',' ',' ',' ',' ',],
  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
  ['D','B','M',' ','1','2','3','4','5',' ',' ',],
  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
  [' ',' ','P1','P2',' ',' ',' ','C','R','F',' ',]
]