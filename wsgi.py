"""module info """
import sys
from contacts_app import create_app

app = create_app("contacts")

if __name__ == "__main__":
    try:
        app.run(port=5000, use_reloader=True)
    except Exception as exc:
        sys.stderr.write(str(exc))
        sys.exit(1)
