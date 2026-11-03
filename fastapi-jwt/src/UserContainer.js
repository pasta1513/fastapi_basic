import { useState } from "react"

const path = 'http://localhost:8080/users'

function MainCon(){
    const [token, setToken] = useState('')
    
    async function onAddUser(){
        const user = {
            'id': 'aaa', 'password': '111'
        }

        const res = await fetch(path + '/signup', {
            method: 'post',
            headers: {'content-type':'application/json'},
            body: JSON.stringify(user)
        })

        console.log(await res.json())
    }

    async function onSignIn(){
        const user = {
            'id': 'aaa', 'password': '111'
        }

        const res = await fetch(path + '/signin', {
            method: 'post',
            headers: {'content-type':'application/json'},
            body: JSON.stringify(user)
        })

        setToken(await res.json())
        console.log(token)
    }

    async function onInfo(){
        const res = await fetch(path + '/info/aaa', {
            method: 'get',
            headers: {
                'content-type':'application/json',
                'Authorization':token['token_type'] + ' ' + token['token']
            },
        })

        const result = await res.json()
        
        console.log('res -> ', res)
        console.log('result -> ', result)
    }

    return (<>
        token : {token['token']}<br></br>
        token_type : {token['token_type']}<br></br>
        <hr></hr>
        <button onClick={onAddUser}>aaa 회원가입</button>
        <button onClick={onSignIn}>aaa 로그인</button>
        <button onClick={onInfo}>aaa 개인정보 확인</button>
    </>)
}

export default MainCon