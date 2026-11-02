import logo from './logo.svg';
import './App.css';
import UserContainer from './UserContainer'

function App() {
  return (
    <div>
    {/* <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      <h2>Main</h2>
      <UserContainer />
    </div>
  );
}

export default App;
