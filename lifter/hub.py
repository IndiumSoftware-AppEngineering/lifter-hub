from .db import get_connection
from .auth import authenticate

class Hub:
    def __init__(self, token: str):
        if not authenticate(token):
            raise PermissionError("Invalid authentication token")
        self.token = token

    def pull(self, prompt_name: str) -> str:
        """Fetch prompt by name."""
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT content FROM prompts WHERE name = %s", (prompt_name,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            conn.close()

# Singleton instance
def pull(prompt_name: str) -> str:
    """Retrieve a prompt by name (requires token initialization)."""
    if not hasattr(Hub, "_instance"):
        raise RuntimeError("Hub is not initialized with a valid token")
    
    return Hub._instance.pull(prompt_name)

def init(token: str):
    """Initialize Hub with a token."""
    Hub._instance = Hub(token)
