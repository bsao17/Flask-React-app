import React, {useState, useEffect} from "react"
import style from "./tasks.module.css"

const Tasks = (props)=>{
   const [task, setTask] = useState()
    return (
        <div id={style.task_body}>
            <h1 id={style.title}>Mes To Do ...</h1>
            <div id={style.username}><span id={style.username_item}>Utilisateur</span>: {props.username}</div>
            <div id={style.date}><span id={style.date_item}>Date</span>: {props.date}</div>
            <div id={style.task}><span id={style.task_item}>Tâche</span>: {props.task}</div>
        </div>
    )
}

export default Tasks;