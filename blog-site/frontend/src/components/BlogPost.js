import moment from "moment";
import React, {Component, Fragment} from "react";
import {Link} from "react-router-dom";

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
                <div className="container">
                <div className="row g-5">
                    <div className="col-md-8">
                        <article className="blog-post">
                            <h2 className="blog-post-title mb-1">{this.state.post.title}</h2>
                            <p className="blog-post-meta">{moment.utc(this.state.post.created).format("LLLL")} by <a href="#">TODO</a></p>

                            <p>{this.state.post.content}</p>
                        </article>
                    </div>
                </div>
                    <Link to={`/post-form/${this.state.post.id}`}>
                        <button type="button" className="btn btn-primary btn-lg px-4 gap-3">Edit</button>
                    </Link>
                    <Link to={`/post-del/${this.state.post.id}`}>
                        <button type="button" className="btn btn-primary btn-lg px-4 gap-3 btn-outline-danger m-2">Delete</button>
                    </Link>
                </div>
            </Fragment>
        );
    }
}

export default BlogPost
