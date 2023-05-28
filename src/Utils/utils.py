import uuid

def generate_short_id():
    return str(uuid.uuid4())[:8]