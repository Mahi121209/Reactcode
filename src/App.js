import React from "react";
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import About from "./About";
import Contact from "./Contact";
import Error from "./Error";

const App = () => {
  return (
    <>
      <Router>
        <Switch>
          <Route exact path="/" component={About} />
          <Route path="/contact" component={Contact} />
          <Route component={Error}/>
        </Switch>
      </Router>
    </>
  );
};

export default App;
