import React, {Component, Fragment} from "react";

class BlogPost extends Component {
    state = {
        post: {}
    }
    componentDidMount() {
        const { postId } = this.props.match.params
        fetch(`http://127.0.0.1:4000/posts/${postId}`)
            .then(res => res.json())
            .then((data) => {
                this.setState({post: data})
            })
            .catch(console.log)
    }
    render() {
        return (
            <Fragment>
                <h1>{this.state.post.title}</h1>
                <p>{this.state.post.content}</p>
                <p>{this.state.post.created}</p>
            </Fragment>
        );
    }
}

export default BlogPost