def convert_path(dir):
    """
        Convert path to force always end with slash "/"
    """
    if not dir.endswith("/"):
        dir = dir+"/"
    return dir

def get_env_path(dir):
    """
        Get concatened path with .env file
    """
    env_path = convert_path(dir)+".env"
    return env_path
