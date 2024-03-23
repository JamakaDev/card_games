import { useState, useEffect } from 'react'
import { Button } from 'react-bootstrap'

import deck from './CardImages';
import './App.css'



function App() {
  const [count, setCount] = useState(0)
  const [tasks, setTasks] = useState([])
  const [cards, setCards] = useState(deck.slice(2))
  const [burn_card, cut_card] = deck.slice(0,2)
  
  useEffect(() => {
    const getTasks = async () => {
      const curr_tasks = await fetchTasks()
      setTasks(curr_tasks)
    }
    
    getTasks()
    
  },[])


  const fetchTasks = async () => {
    const resp = await fetch(`http://localhost:5000/tasks`)
    const data = await resp.json()
    return data
  }

  const moveCard = (e, idx) => {
    e.preventDefault();

    let card = document.getElementById(`card${idx}`)
    card.style.left += 50

  }


  return (
    <div className="App">
      
        
        <div className='deck-container'>
          {cards.map((card, idx) =>{
            return (
              <Button className='logo cards' style={{backgroundImage:`url(${card})`,backgroundSize:"cover", width:"128px", height:"160px"}}></Button>     
          )})}
          <Button onClick={(e) => {
            e.preventDefault();
            e.target.style.left += `${50}px`
          }} className='logo cards cut' style={{backgroundImage:`url(${cut_card})`,backgroundSize:"cover", width:"128px", height:"160px"}}></Button>
          <Button className='logo cards burn' style={{backgroundImage:`url(${burn_card})`,backgroundSize:"cover", width:"128px", height:"160px"}}></Button>
  
        </div>
             

      
    </div>
  )
}

export default App
