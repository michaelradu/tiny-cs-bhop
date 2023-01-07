import pymem
import win32api
import time

# offsets
LOCAL_PLAYER = 14316652
FORCE_JUMP = 86422944
HEALTH = 256
FLAGS = 260

def bhop() -> None:
    pm = pymem.Pymem('csgo.exe')

    # get module address
    for module in list(pm.list_modules()):
        if module.name == 'client.dll':
            client = module.lpBaseOfDll

    # hack loop
    while True:
        time.sleep(0.01)

        # space bar
        if not win32api.GetAsyncKeyState(0x20):
            continue

        local_player: int = pm.read_uint(client + LOCAL_PLAYER)

        if not local_player:
            continue

        # is alive
        if not pm.read_int(local_player + HEALTH):
            continue

        # on ground
        if pm.read_uint(local_player + FLAGS) & 1 << 0:
            pm.write_uint(client + FORCE_JUMP, 6)
            time.sleep(0.01)
            pm.write_uint(client + FORCE_JUMP, 4)

if __name__ == '__main__':
    bhop()
