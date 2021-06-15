import React, { Component, Fragment } from "react";
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";
import Posts from './components/posts';

class Main extends Component {
    state = {
        posts: []
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000/posts')
        .then(res => res.json())
        .then((data) => {
          this.setState({ posts: data })
        })
        .catch(console.log)
      }
  render() {
    return (
       <Router>
        <main>
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
            </ul>
          </nav>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/posts/:postId"  component={Post} />
        </Switch>
        </main>
    </Router>
    );
  }
}

class Home extends Component {
    state = {
        posts: []
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000/posts')
        .then(res => res.json())
        .then((data) => {
          this.setState({ posts: data })
        })
        .catch(console.log)
      }
  render() {
    return (
      <Fragment>
        <Posts posts={this.state.posts} />
      </Fragment>
    );
  }
}

class Post extends Component {
    state = {
    }
    componentDidMount() {
        const { postId } = this.props.match.params
        fetch(`http://127.0.0.1:5000/posts/${postId}`)
        .then(res => res.json())
        .then((data) => {
          this.setState(data)
        })
        .catch(console.log)
      }
  render() {
    return (
      <Fragment>
        <h1>{this.state.title}</h1>
        <p>{this.state.content}</p>
        <p>{this.state.created}</p>
      </Fragment>
    );
  }
}


export default Main;

