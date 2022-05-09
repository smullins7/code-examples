import React, {Component, useState} from "react";
import { Route, Switch } from "react-router-dom";
import About from "../pages/About";
import NotFound from "../pages/NotFound";
import BlogPost from "./BlogPost";
import BlogPostsList from "./BlogPostsList";
import ErrorAlert from "./ErrorAlert";
import OAuth2Login from "react-simple-oauth2-login";
import NavBar from "./NavBar";
import NewBlogPost from "./NewBlogPost";
import UserSettings from "./UserSettings";

class Main extends Component {
  render() {
    return (
        <>
            <NavBar />
            <Switch>
                <Route path="/" exact>
                    <BlogPostsList />
                </Route>
                <Route path="/posts/:postId"  component={BlogPost} />
                <Route path="/new-post" component={NewBlogPost} />
                <Route path= "/settings">
                    <UserSettings />
                </Route>
                <Route path= "/about">
                    <About />
                </Route>
                <Route path="*">
                    <NotFound />
                </Route>
            </Switch>
        </>)
  }
}


export function OauthExample() {
    const [accessToken, setAccessToken] = useState(null);
    const [error, setError] = useState(null);

    const onSuccess = ({ access_token: token }) => setAccessToken(token);
    return (
        <div className="column">
            {
                error && <ErrorAlert error={error} />
            }

            <OAuth2Login
                scope="email profile"
                authorizationUrl="https://accounts.google.com/o/oauth2/v2/auth"
                responseType="token"
                clientId="362134854545-bejckl8jl3m4vj78gp6p4hmbm7dibcsq.apps.googleusercontent.com"
                redirectUri="http://localhost:3000/oauth-callback"
                onSuccess={onSuccess}
                onFailure={setError}/>
            {
                accessToken && <p>Access token: {accessToken}</p>
            }
        </div>
    );
}

export default Main;
