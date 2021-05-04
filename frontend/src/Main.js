import React, { Component } from "react";
import Posts from './components/posts';

class Main extends Component {
    state = {
        posts: []
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000/')
        .then(res => res.json())
        .then((data) => {
          this.setState({ posts: data })
        })
        .catch(console.log)
      }
  render() {
    return (
          <Posts posts={this.state.posts} />
    );
  }
}
 
export default Main;
