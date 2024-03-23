from card_utils import *

def main() -> int:

    deck1 = create_deck()
    shuffle_deck(deck1, 2)
    cut_deck(deck1, 2)
    deal_card(deck1)
    display_deck(deck1)
    deal_card(deck1)

    
    return 0;


if __name__ == '__main__':
    main()
