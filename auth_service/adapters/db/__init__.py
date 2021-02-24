from auth_service.adapters.db.user_psql_adapter import UserDBAdapter
from auth_service.main.db import psql_connection_manager

user_db = UserDBAdapter(psql_connection_manager)
