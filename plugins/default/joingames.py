if answ[1] in ['talk','чат']:
    if (toho < 2000000000):
        apisay('Чат доступен только в конфе.',toho,torep)
    else:
        game_module['active_users'][userid] = 'talk'
        apisay('Ты вступил в разговор с ботом. Для выхода напиши "exit"',toho,torep)