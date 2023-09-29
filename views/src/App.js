import React, {useState, useEffect} from 'react'
import './App.css';
import axios from 'axios'


function App() {
    const [data, setData] = useState()
    const [click, setClick] = useState(true)
    
    const toggle_click_on = 'm-auto mt-5 bg-red-500 border border-red-500 text-white p-2 w-1/2 rounded'
    const toggle_click_off = 'm-auto mt-5 bg-red-300 border border-red-500 text-white p-2 w-1/2 rounded'

    const toggleClick = (e)=>{
      e.preventDefault()
      setClick(!click)
    }

    useEffect(() => {
      try {
         axios.get('/database')
           .then(result => {
           return setData(result.data[0][1])
           })
      } catch (error) {
        console.error(error)
      }
      }, [data]);

   return (
    <div className="App flex flex-col justify-center align-center">
        <h1 id='title' className='text-2xl mt-10 mb-10'>Oh Tout Doux ... Là </h1>

          <div id="form" className='border border-black w-1/4 m-auto rounded' onSubmitCapture={()=>console.log("c'est fait !!!")}>
            <form className='m-5 flex flex-col'>
              <div className='flex flex-col w-full'>
                <label className='m-2' htmlFor="day_input" id='day_label'>Date</label>
                <input type="date" id='day_input' className='border border-black rounded w-full p-2' />
              </div>
              <br/>
              <div className='flex flex-col w-full'>
              <label className='m-2' htmlFor="todo" id='day_label'>Tache</label>
              <textarea id='todo' className='border border-black rounded w-full p-2' />
              </div>
              <br/>
              <div className='flex flex-col justify-center items-center'>
              <label className='me-5' htmlFor="day_input" id='day_label'>clôturer</label>
              <input type="checkbox" id='day_input' className='text-center' />
              </div>
              <button className={click ? toggle_click_off : toggle_click_on} onClick={toggleClick}>Enregistrer</button>
            </form>
          </div>
        <div className="contact">Contact : {data}</div>
    </div>
  );
}

export default App;
