import React from 'react'

const Signin = () => {
return (
    <>
        <form>
            <label htmlFor="email">email</label>
            <input type="text" id="email" />
            <label htmlFor="pwd">email</label>
            <input type="text" id="pwd" />
            <input type="submit" value="Se connecter"/>
        </form>
    </>
    )
}

export default Signin