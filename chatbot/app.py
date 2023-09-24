"""
Write code here which need access to the app during runtime. 
You can decorate functions using '@pyttman.app.hooks.run("before_start")' and have 
them executed before the app goes online - useful for database connections and alike.
"""
from pyttman import app


# from pyttman import app
# @app.hooks.run("before_start")
# def hello_world():
#     print("Hello, world!")

@app.hooks.run("before_start")
def test():
    app.database_handle = {}
