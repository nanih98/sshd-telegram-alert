def convert_path(dir):
    if not dir.endswith("/"):
        dir = dir+"/"
    return dir

def get_env_path(dir):
    env_path = convert_path(dir)+".env"
    return env_path
