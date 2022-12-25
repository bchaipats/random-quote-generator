import datetime
import os

from requests import get

from flask import Flask
from flask.cli import AppGroup

from sample_project.loan import LoanStatus

import pytest


@pytest.fixture(scope="module")
def authenticated_client(app):
    client = app.test_client()
    client.post(
        "/login",
        data=dict(email="dummy@email.ai", password="notreal"),
        follow_redirects=True,
    )
    return client


def get_error_message(error_type):
    colors = {
        404: "red",
        403: "orange",
        401: "yellow",
    }

    return colors[error_type] if error_type in colors else "blue"


def main():
    res = get("https://api.github.com/events")
    status = res.status_code
    if res.ok:
        print(f"{status}")
    else:
        print(get_error_message(status))


if __name__ == "__main__":
    main()
    evaluate = 'print("Hi!")'
    eval(evaluate)


    evaluate = 'open("secret_file.txt").read()'
    eval(evaluate)