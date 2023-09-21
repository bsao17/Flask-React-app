import React, {useState, useEffect} from 'react'
import './App.css';
import axios from 'axios'


function App() {
const [data, setData] = useState(null)

useEffect(() => {
   axios.get('users')
      .then(result => setData(result))
  }, []);
console.log(data)
    return (
    <div className="App">

        <h1 id='title'>La To-Do de LouLou</h1>
        <div> voici mes données: {data}</div>
          <div id="form">
            <form style={{'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center'}}>
              <div style={{'display': 'flex'}}>
                <label style={{'marginRight': '10px'}} htmlFor="day_input" id='day_label'>Jour</label>
                <input type="date" id='day_input' />
              </div>

              <br/>
              <div style={{'display': 'flex'}}>
              <label style={{'marginRight': '10px'}} htmlFor="todo" id='day_label'>A faire</label>
              <textarea id='todo' />
              </div>
              <br/>
              <div style={{'display': 'flex'}}>
              <label style={{'marginRight': '10px'}} htmlFor="day_input" id='day_label'>fermé</label>
              <input type="checkbox" id='day_input' />
              </div>
            </form>
          </div>
    </div>
  );
}

export default App;
