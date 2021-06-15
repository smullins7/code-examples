import React from 'react'
import { Link } from "react-router-dom";
    
const Posts = ({ posts }) => {
  return (
    <div>
      <center><h1>Posts</h1></center>
      {posts.map((post) => (
        <div class="card">
          <div class="card-body">
            <Link to={`/posts/${post.id}`}><h5 class="card-title">{post.title}</h5></Link>
          </div>
        </div>
      ))}
    </div>
  )
};

export default Posts
