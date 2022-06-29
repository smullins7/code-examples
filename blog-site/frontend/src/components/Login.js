import {Component} from "react";
import { GoogleLogin } from '@react-oauth/google';
import jwt_decode from "jwt-decode";
import {withCookies} from "react-cookie";


class Login extends Component {
    render() {
        return (
            <GoogleLogin
                onSuccess={credentialResponse => {
                    const decoded = jwt_decode(credentialResponse.credential);
                    const { cookies } = this.props;
                    cookies.set("logged-in-user", {"name": decoded.name, "email": decoded.email});
                    console.log(credentialResponse);
                    console.log(decoded);
                }}
                onError={() => {
                    console.log('Login Failed');
                }}
            />
        )
    }
}

export default withCookies(Login)
