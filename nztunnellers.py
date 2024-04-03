#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import iterm2


async def SwitchProfile(connection, session, profile_name):
    print("Switching profile to: " + profile_name)
    partialProfiles = await iterm2.PartialProfile.async_query(connection)
    for partial in partialProfiles:
        if partial.name == profile_name:
            full = await partial.async_get_full_profile()
            await session.async_set_profile(full)


# Main
async def main(connection):
    app = await iterm2.async_get_app(connection)

    window = app.current_terminal_window
    if app.current_terminal_window is None:
        await window.async_create_tab()

    main = await window.async_create_tab()
    await main.async_activate()

    # Create a main terminal for interactive terminal tasks
    session = main.current_session

    # # Set profile to nztunnellers
    await SwitchProfile(connection, session, "Main Profile")
    await session.async_activate()
    await session.async_send_text("..\n")
    await session.async_send_text("cd nztunnellers\n")

    # Start server
    serverSession = await session.async_split_pane(vertical=True, before=False)
    await SwitchProfile(connection, serverSession, "nztunnellers Server Profile")
    await serverSession.async_send_text("..\ncd nztunnellers/\n")
    await serverSession.async_send_text("make run-server\n")

    # Start client
    webappSession = await serverSession.async_split_pane()
    await SwitchProfile(connection, webappSession, "nztunnellers WebApp Profile")
    await webappSession.async_send_text("..\ncd nztunnellers/\n")
    await webappSession.async_send_text("make run-client\n")

    await session.async_activate(select_tab=True)


iterm2.run_until_complete(main)
