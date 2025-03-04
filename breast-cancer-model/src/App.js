import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        Breast Cancer Detection
      </header>
      <div className="App-body">
        <p className="body-header">Tumor Features</p>
        <form>
          <label>
            Feature 1:
            <input type="text" name="name" />
          </label>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default App;
