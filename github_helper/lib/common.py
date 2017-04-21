def exec_command(cmd):
    try:
        subprocess.check_call(cmd)
        return True
    except:
        print("Error found and skipped")
        return False
