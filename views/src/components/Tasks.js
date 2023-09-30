import React, {useState, useEffect} from "react"

const Tasks = (props)=>{
   const [task, setTask] = useState()
    return (
        <div>
            <h2>Mes To Do ...</h2>
            <div>Utilisateur: {props.username}</div>
            <div>Date: {props.date}</div>
            <div>Tâche: {props.task}</div>
        </div>
    )
}

export default Tasks;