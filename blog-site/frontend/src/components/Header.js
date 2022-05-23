import React from "react"

const Header = () => {
    return (
        <div className="container">
            <header className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
                <ul className="nav nav-pills">
                    <li className="nav-item"><a href="/" className="nav-link active" aria-current="page">Posts</a></li>
                    <li className="nav-item"><a href="/settings" className="nav-link">Settings</a></li>
                    <li className="nav-item"><a href="/about" className="nav-link">About</a></li>
                </ul>
            </header>
        </div>
    )
}

export default Header
