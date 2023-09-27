import React, {useState, useEffect} from 'react'
import './App.css';
import axios from 'axios'

function App() {
    const [data, setData] = useState()
    useEffect(() => {
       axios.get('database')
          .then(result => {
          return setData(result.data[0][1])
          })
      }, []);
    console.log(data)
   return (
    <div className="App flex flex-col justify-center align-center">
        <h1 id='title' className='text-2xl mt-10 mb-10'>Oh Tout Doux ... Là </h1>

          <div id="form">
            <form className='m-auto flex flex-col w-1/4'>
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
            </form>
          </div>
        <div className="contact">Contact : {data}</div>
    </div>
  );
}

export default App;
