import platform
from datetime import date, datetime, timedelta

print("""Bonjour!
"Je m'appelle Atlas One
"Je suis un Robot moderne et intelligent.
"Je souhaite devenir votre ami et vous aider dans vos tâches quotidiennes."""
)

actuel = datetime.now()
auj = date.today()
demain = auj + timedelta(days=1)
print(f"""Aujourd'hui on est le {auj} et il est {actuel.strftime("%H:%M:%S")}.
Demain on sera le {demain}.""")

version = platform.python_version()
print(f"J'utilise Python version {version}.")