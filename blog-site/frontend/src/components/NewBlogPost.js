import {Component} from "react";

class NewBlogPost extends Component {
    state = {
        title: "",
        content: "",
    }
    onChange = e => {
        this.setState({
            [e.target.name]: e.target.value,
        })
    }
    handleSubmit = async e => {
        e.preventDefault();
        console.log(this.state);
        try {
            fetch("http://127.0.0.1:4000/posts", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: this.state.title,
                    content: this.state.content,
                }),
            }).then(response =>
                response.json().then(data => ({
                        data: data,
                        status: response.status
                    })
                ).then(res => {
                    console.log(res.status, res.data);
                    this.props.history.push(`/posts/${res.data.id}`);
                }));
        } catch (err) {
            console.log(err);
        }
    };
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input
                    type="text"
                    placeholder="title goes here"
                    value={this.state.title}
                    name="title"
                    onChange={this.onChange}
                />
                <textarea
                    placeholder="content here"
                    value={this.state.content}
                    name="content"
                    onChange={this.onChange}
                />
                <button>Publish</button>
            </form>
        )
    }

}

export default NewBlogPost
