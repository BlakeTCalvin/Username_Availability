from config import app
from controller_functions import index, username, register, usersearch

app.add_url_rule("/", view_func=index)
app.add_url_rule("/register", view_func=register, methods=["POST"])
app.add_url_rule("/username", view_func=username, methods=["POST"])
app.add_url_rule("/usersearch", view_func=usersearch, methods=["POST"])