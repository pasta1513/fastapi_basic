import { useState } from "react"

const path = `http://localhost:8080`

async function get_users(){
    const res = await fetch(path + `/users`, {method:`get`})
    console.log(`res: `, res)
    if (res.ok){
        const data = await res.json()
        console.log(data)
        return data ?? []
    }

    return []
}

async function get_user(email){
    const res = await fetch(path + `/users/` + email, {method:`get`})
    console.log(`res: `, res)
    if (res.ok){
        const data = await res.json()
        console.log(data)
        return data ?? ''
    }

    return ''
}

async function del_user(username){
    const res = await fetch(path + `/users/` + username, {method:`delete`})
    console.log(`res: `, res)
    if (res.ok){
        const data = await res.json()
        console.log(data)
        return data ?? ''
    }

    return ''
}

function MainCon(){
    // const [num, setNum] = useState(100)
    const [users, setUsers] = useState([])
    let num = 100

    async function onAllUser(){
        // alert(`실행???`)
        // num += 1
        // SVGAnimatedNumber(num + 1)
        // console.log(`num: `, num)
        // get_users()
        // console.log(`get_users: `, await get_users()) # 비동기 방식으로 불러온 함수는 리턴값도 비동기기 때문에 받을 때도 await을 붙여야 함!

        const arr = [
            {username:"aaa", password:"aaa", email:"aaa@aaa.com", name:"홍길동"},
            {username:"bbb", password:"bbb", email:"bbb@bbb.com", name:"김개똥"},
        ]

        setUsers(await get_users())
    }

    const [email, setEamil] = useState('')

    function onChangeEmail(e){
        console.log(e.target.value)
        setEamil(e.target.value)
    }

    const [user, setUser] = useState({})

    async function onClickUser(){
        setUser(await get_user(email))
    }

    const [username, setUsername] = useState('')

    function onChangeUsername(e){
        console.log(e.target.value)
        setUsername(e.target.value)
    }

    // const onClickDelUser = async () => {} # 호출한 시점에 생성 후 자동 삭제
    async function onClickDelUser(){
        let result = await del_user(username)

        if (result){
            alert(`삭제 성공: ${username}`)
        } else {
            alert(`삭제 실패: ${username}`)
        }
    }

    const [addUser, setAddUser] = useState({
        username:"", password:"", email:"", name:""
    })

    function onChangeAdd(e){
        setAddUser({...addUser, [e.target.name] : e.target.value})
        console.log(addUser)
    }

    async function onAddSubmit(e){
        e.preventDefault() // action을 막아줌
        console.log(e.target)
        // console.log(typeof(addUser))
        // console.log(typeof(JSON.stringify(addUser)))

        const res = await fetch(path + "/users", {
            method: "post",
            headers: {"content-type":"application/json"},
            body: JSON.stringify(addUser)
        })
        console.log(`res: `, res)

        if (res.ok) {
            const data = await res.json()
            alert(`회원가입 성공! ${data.name} 님 안녕하세요!`)
        } else {
            alert(`회원가입 실패! (${res.status})`)
        }
    }

    const [userUpdate, setUserUpdate] = useState({
        username:"", name:"", email:""
    })

    function onChangeUpdate(e){
        setUserUpdate({...userUpdate, [e.target.name] : e.target.value})
    }
    
    async function onUpdateSubmit(e){
        e.preventDefault() // action을 막아줌
        const formData = new FormData(e.target)
        const res = await fetch(path + "/users/form/" + e.target.username.value, {
            method: "put",
            body: formData
        })
        console.log(`res: `, res)

        if (res.ok) {
            const data = await res.json()
            alert(`${data.username} 님의 회원 정보를 수정했습니다!`)
        } else {
            alert(`정보 수정 실패! (${res.status})`)
        }
    }

    return <>
        <h3> - 저 장 - </h3>
        <form onSubmit={onAddSubmit} action={"https://www.naver.com"}>
            username: <input name="username" onChange={onChangeAdd}></input><br></br>
            password: <input name="password" onChange={onChangeAdd}></input><br></br>
            email: <input name="email" onChange={onChangeAdd}></input><br></br>
            name: <input name="name" onChange={onChangeAdd}></input><br></br>
            <button>저장</button>
        </form>

        <h3> - 수 정 - </h3>
        <form onSubmit={onUpdateSubmit} action={"https://www.google.com"}>
            username: <input name="username"></input><br></br>
            email: <input name="email"></input><br></br>
            name: <input name="name"></input><br></br>
            <button>수정</button>
        </form>

        <h3> - 삭 제 - </h3>
        <input type="username" onChange={onChangeUsername}></input><br></br>
        <button onClick={onClickDelUser}>삭제</button><br></br>

        <h3> - 조 회 - </h3>
        id: {user.username}<br></br>
        pw: {user.password}<br></br>
        email: {user.email}<br></br>
        name: {user.name}<br></br>

        <input type="email" onChange={onChangeEmail}></input><br></br>
        <button onClick={onClickUser}>개인정보 확인</button><br></br>

        main 연동 num: {users.length}<br></br>
        <hr></hr>
            {users.map((user, idx) => (
                <div key={idx}>
                    id: {user.username}<br></br>
                    pw: {user.password}<br></br>
                    email: {user.email}<br></br>
                    name: {user.name}<hr></hr>
                </div>
            ))}
        <hr></hr>
        <button onClick={onAllUser}>모든 목록 확인</button>
    </>
}
export default MainCon