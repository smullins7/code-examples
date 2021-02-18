from flask import Flask, render_template, request, url_for, flash, redirect
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())

import posts, comments