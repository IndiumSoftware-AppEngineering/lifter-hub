from .db import Database

class Hub:
    def __init__(self, db_type="sqlite"):
        self.db = Database(db_type)
        self.db.create_table()

    def pull(self, prompt_name: str) -> str:
        """Fetches a prompt by name."""
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT content FROM prompts WHERE name = %s" if self.db.db_type == "postgres" else "SELECT content FROM prompts WHERE name = ?", (prompt_name,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            conn.close()

    def create(self, name: str, content: str) -> bool:
        """Creates a new prompt."""
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO prompts (name, content) VALUES (%s, %s)" if self.db.db_type == "postgres" else "INSERT INTO prompts (name, content) VALUES (?, ?)", (name, content))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error creating prompt: {e}")
            return False
        finally:
            conn.close()

    def update(self, name: str, new_content: str) -> bool:
        """Updates an existing prompt."""
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("UPDATE prompts SET content = %s WHERE name = %s" if self.db.db_type == "postgres" else "UPDATE prompts SET content = ? WHERE name = ?", (new_content, name))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating prompt: {e}")
            return False
        finally:
            conn.close()

    def delete(self, name: str) -> bool:
        """Deletes a prompt by name."""
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM prompts WHERE name = %s" if self.db.db_type == "postgres" else "DELETE FROM prompts WHERE name = ?", (name,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting prompt: {e}")
            return False
        finally:
            conn.close()

# Singleton instance
def init(db_type="sqlite"):
    """Initialize Hub with a database type."""
    return Hub(db_type)
