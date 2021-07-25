import urls
from pprint import pprint
from session import SessionManager

session_manager = SessionManager()
pprint(session_manager.login())

pprint(session_manager.get(urls.ACTIVITIES))
pprint(session_manager.get(urls.TIME_ENTRIES.format("2021-07-22T00:00:00.000", "2021-07-23T23:59:59.999")))
