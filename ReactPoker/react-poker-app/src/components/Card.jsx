import React from 'react'
import deck from '../CardImages';

const Card = () => {
  const [cards, setCards] = useState(deck.slice(2))
  const [cut_card, burn_card] = deck.slice(0,2)


  return (
    <div>Card</div>
  )
}

export default Card