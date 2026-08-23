import "./App.css";

export default function App() {
  return (
    <div className="app">

      <div className="overlay"></div>

      <header className="hero">

        <p className="company">IOTEC</p>

        <h1>X27</h1>

        <h2>Global Resilience Platform</h2>

        <div className="mission">

          <span>OBSERVE</span>
          <span>PREDICT</span>
          <span>COORDINATE</span>
          <span>RESPOND</span>
          <span>RECOVER</span>
          <span>LEARN</span>

        </div>

      </header>

      <section className="dashboard">

        <div className="card">
          <h3>RESILIENCE INDEX</h3>
          <p>100</p>
        </div>

        <div className="card">
          <h3>NODES ONLINE</h3>
          <p>5</p>
        </div>

        <div className="card">
          <h3>PROGRAMS</h3>
          <p>3</p>
        </div>

        <div className="card">
          <h3>PROJECTS</h3>
          <p>12</p>
        </div>

        <div className="card">
          <h3>CRITICAL RISKS</h3>
          <p>1</p>
        </div>

      </section>

      <section className="modules">

        <h2>WAR ROOM MODULES</h2>

        <div className="module-grid">

          <div className="module">DIGITAL TWIN</div>

          <div className="module">COMMAND CENTER</div>

          <div className="module">ALERT CENTER</div>

          <div className="module">NATIONAL GRID</div>

          <div className="module">CONTINUITY ENGINE</div>

          <div className="module">STRATEGIC AI</div>

          <div className="module">GOVERNANCE</div>

          <div className="module">SIMULATION LAB</div>

        </div>

      </section>

    </div>
  );
}