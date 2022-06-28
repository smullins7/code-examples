import moment from "moment";
import React, {Component, Fragment} from "react";
import {Link} from "react-router-dom";
import Comment, {CommentModal} from "./Comment";

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
    receiveComment = (comment) => {
        console.log("received comment: ", comment);
        let {post} = this.state;
        const index = post.comments.indexOf(comment);
        if (index !== -1) {
            post.comments.splice(index, 1);
        } else {
            post.comments.push(comment);
        }
        this.setState({
            post: post
        })
    }
    render() {
        console.log("Rendering with state: ", this.state);
        return (
            <Fragment>
                <div className="container">
                <div className="row g-5">
                    <div className="col-md-8">
                        <article className="blog-post">
                            <h2 className="blog-post-title mb-1">{this.state.post.title}</h2>
                            <p className="blog-post-meta">{moment.utc(this.state.post.created).format("LLLL")} by <a href="#">TODO</a></p>

                            <p><span style={{"whiteSpace": "pre-line"}}>{this.state.post.content}</span></p>
                        </article>
                    </div>
                </div>
                    <Link to={`/post-form/${this.state.post.id}`}>
                        <button type="button" className="btn btn-primary btn-lg px-4 gap-3">Edit</button>
                    </Link>
                    <Link to={`/post-del/${this.state.post.id}`}>
                        <button type="button" className="btn btn-lg px-4 gap-3 btn-danger m-2"><i className="bi bi-trash"/> Delete</button>
                    </Link>
                    <hr />

                    {this.state.post.comments?.length > 0 ? (
                            <h3>Article Comments</h3>
                        ) : (
                            <h5 className="font-italic">no comments yet</h5>
                        )}
                    <CommentModal key={this.state.post.id} postId={this.state.post.id} parentHook={this.receiveComment} />

                    {this.state.post.comments?.map(comment => (
                        <Comment key={comment.id} comment={comment} postId={this.state.post.id} parentHook={this.receiveComment}/>
                    ))}
                </div>
            </Fragment>
        );
    }
}

export default BlogPost
