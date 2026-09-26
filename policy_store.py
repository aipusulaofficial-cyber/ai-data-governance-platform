import sqlite3
from pathlib import Path


class PolicyStore:
    """Durable policy repository with transactional updates."""

    def __init__(self, path: str = "policies.db") -> None:
        self.path = str(Path(path))
        with sqlite3.connect(self.path) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS policies ("
                "name TEXT PRIMARY KEY, version INTEGER NOT NULL, document TEXT NOT NULL)"
            )

    def put(self, name: str, version: int, document: str) -> None:
        if version < 1 or not name.strip() or not document.strip():
            raise ValueError("invalid policy")
        with sqlite3.connect(self.path) as db:
            db.execute(
                "INSERT INTO policies VALUES(?,?,?) "
                "ON CONFLICT(name) DO UPDATE SET version=excluded.version, "
                "document=excluded.document WHERE excluded.version > policies.version",
                (name, version, document),
            )

    def get(self, name: str):
        with sqlite3.connect(self.path) as db:
            return db.execute(
                "SELECT name,version,document FROM policies WHERE name=?", (name,)
            ).fetchone()
