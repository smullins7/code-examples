import React, {Component} from 'react'
import { Link } from "react-router-dom";


class BlogPostsList extends Component {
    state = {
        posts: []
    }
    componentDidMount() {
        fetch('http://127.0.0.1:4000/posts')
            .then(res => res.json())
            .then((data) => {
                this.setState({ posts: data })
            })
            .catch(console.log)
    }
    render() {
        return (
            <div>
                <center><h1>Posts</h1></center>
                <Link to="/new-post">
                    <button type="button">
                        Create New Post!
                    </button>
                </Link>
                {this.state.posts.map((post) => (
                    <div className="card" key={post.id}>
                        <div className="card-body">
                            <Link to={`/posts/${post.id}`}><h5 className="card-title">{post.title}</h5></Link>
                        </div>
                    </div>
                ))}
            </div>
        );
    }
}

export default BlogPostsList
