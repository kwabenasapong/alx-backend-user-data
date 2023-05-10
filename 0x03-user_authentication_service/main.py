#!/usr/bin/env python3
"""
Main file
"""
import requests


def register_user(email: str, password: str) -> None:
    """Register user"""
    url = 'http://localhost:5000/users'
    data = {'email': email, 'password': password}
    r = requests.post(url, data=data)
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': 'user created'}
    print('register_user OK')


def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password"""
    url = 'http://localhost:5000/sessions'
    data = {'email': email, 'password': password}
    r = requests.post(url, data=data)
    assert r.status_code == 401
    assert r.json() == {'message': 'wrong password'}
    print('log_in_wrong_password OK')


def log_in(email: str, password: str) -> str:
    """Log in"""
    url = 'http://localhost:5000/sessions'
    data = {'email': email, 'password': password}
    r = requests.post(url, data=data)
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': 'logged in'}
    print('log_in OK')
    return r.cookies.get('session_id')


def profile_unlogged() -> None:
    """Profile unlogged"""
    url = 'http://localhost:5000/profile'
    r = requests.get(url)
    assert r.status_code == 403
    assert r.json() == {'message': 'Forbidden'}
    print('profile_unlogged OK')


def profile_logged(session_id: str) -> None:
    """Profile logged"""
    url = 'http://localhost:5000/profile'
    cookies = {'session_id': session_id}
    r = requests.get(url, cookies=cookies)
    assert r.status_code == 200
    assert r.json() == {'email': 'guillaume@holberton.io'}
    print('profile_logged OK')


def log_out(session_id: str) -> None:
    """Log out"""
    url = 'http://localhost:5000/sessions'
    cookies = {'session_id': session_id}
    r = requests.delete(url, cookies=cookies)
    assert r.status_code == 200
    assert r.json() == {'message': 'Bienvenue'}
    print('log_out OK')


def reset_password_token(email: str) -> str:
    """Reset password token"""
    url = 'http://localhost:5000/reset_password'
    data = {'email': email}
    r = requests.post(url, data=data)
    assert r.status_code == 200
    assert len(r.text) == 72
    print('reset_password_token OK')
    return r.text


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password"""
    url = 'http://localhost:5000/reset_password'
    data = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    r = requests.put(url, data=data)
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': 'Password updated'}
    print('update_password OK')


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    # register_user(EMAIL, PASSWD)
    # log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
