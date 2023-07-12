# 

from graia.ariadne.event.mirai import NudgeEvent


def nudge_str(event: NudgeEvent) -> str:
    t = event.type
    supp = f'[{event.supplicant}]'
    targ = f'[{event.target}]'
    return f'{t}: {supp} {event.msg_action} {targ}'