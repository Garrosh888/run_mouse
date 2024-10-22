import platform
import os
import getpass

def get_system_info():
    systeminfo = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
    return systeminfo

def get_user_info():
    user_info = {
        "username": getpass.getuser(),
        "user_id": os.getuid() if hasattr(os, "getuid") else "N/A",
        "group_id": os.getgid() if hasattr(os, "getgid") else "N/A",
        "home_directory": os.path.expanduser("~"),
    }
    return user_info

if __name__ == "__main__":
    system_info = get_system_info()
    user_info = get_user_info()

    print("Данные о системе:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\nДанные о пользователе:")
    for key, value in user_info.items():
        print(f"{key}: {value}")
