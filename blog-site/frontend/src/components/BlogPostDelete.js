import {Component} from "react";

class BlogPostDelete extends Component {
    componentDidMount() {
        try {
            const { postId } = this.props.match.params;
            fetch(`http://127.0.0.1:4000/posts/${postId}`, {
                method: "DELETE",
            }).then(response => response.text())
                .then(data => {
                    console.log(data);
                    this.props.history.push("/");
                })
        } catch (err) {
            console.log(err);
        }
    }
    render() {
        return <div></div>
    }
}

export default BlogPostDelete
