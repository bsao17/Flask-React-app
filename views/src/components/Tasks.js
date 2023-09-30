import React, {useState, useEffect} from "react"

const Tasks = (props)=>{
   const [task, setTask] = useState()
    return (
        <div>
            <h1 style={{fontSize: "1.5rem", fontWeight: "bold", marginBottom: "2%"}}>Mes To Do ...</h1>
            <div>Utilisateur: {props.username}</div>
            <div>Date: {props.date}</div>
            <div>Tâche: {props.task}</div>
        </div>
    )
}

export default Tasks;