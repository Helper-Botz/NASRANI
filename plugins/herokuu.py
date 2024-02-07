import heroku3
from plugins.helpers.sample_config import Config

"""
    Appending each value to the list
    So even if app vars not in order,
    it will be appended to the list XD

    Copy paste this code to make more apps :)

"""


app = []
try:
    app.append(Config.HRK_APP_NAME)
except AttributeError:
    app.append(None)
    pass

# Always for safety XD
app.append(None)



h_conn = []
try:
    h_conn.append(heroku3.from_key(Config.HRK_API))
except AttributeError:
    pass


# Always for safety XD
h_conn.append(None) 
