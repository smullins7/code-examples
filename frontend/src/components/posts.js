import React from 'react'
    
const Posts = ({ posts }) => {
  return (
    <div>
      <center><h1>Posts</h1></center>
      {posts.map((post) => (
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{post.title}</h5>
          </div>
        </div>
      ))}
    </div>
  )
};

export default Posts
