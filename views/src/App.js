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
    <div className="App">
        <h1 id='title'>Oh Tout Doux ... Là </h1>

          <div id="form">
            <form style={{'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center'}}>
              <div style={{'display': 'flex'}}>
                <label style={{'marginRight': '10px'}} htmlFor="day_input" id='day_label'>Date</label>
                <input type="date" id='day_input' />
              </div>
              <br/>
              <div style={{'display': 'flex','justifyContent': 'center', 'alignItems': 'center'}}>
              <label style={{'marginRight': '10px'}} htmlFor="todo" id='day_label'>Tache</label>
              <textarea id='todo' />
              </div>
              <br/>
              <div style={{'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}}>
              <label style={{'marginRight': '10px'}} htmlFor="day_input" id='day_label'>clôturer</label>
              <input type="checkbox" id='day_input' />
              </div>
            </form>
          </div>
        <div className="contact">Contact : {data}</div>
    </div>
  );
}

export default App;
