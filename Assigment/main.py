import plugin
#from plugin import Plugin, onLoadDecorator
import time
from printStyle import style as st
from printStyle import cursor
import sys

try:

    st.print("     Starting...", 0.02)
    cursor.Spinner(0.1)
    st.newLine()
    # time.sleep(1)

    startText = """
Hi, I am a calculator. I will help you to calculate the real price
of the filament converted to printing volume (in cubic centimetres).
You can also add your calculation templates using plugins.
"""
    st.print(startText, 0.008)
    # sys. exit()
    st.newLine()
    time.sleep(1)

    cursor.Spinner(0.1)
    st.newLine()
    st.print("Press 'Y' to start or 'N' to close", 0.02)
    st.newLine()

    while True:
        st.print(">", 0.08)
        a = input()
        if a == "y" or a == "Y":
            st.newLine()
            plugin.LoadPlugins()
            break
        if a == "n" or a == "N":
            st.print("\nShutting down...", 0.02)
            st.newLine()
            sys.exit()
        else:
            st.print("Incorrect input", 0.02)
            st.newLine()

    st.newLine()
    st.print("Choose plugin (number):", 0.02)

    while not False:
        #print(">")

        a = input().split(" ")

        for p in plugin.Plugins.keys():
            plugin.Plugins[p].OnCommand(a[0], a[1:])

except KeyboardInterrupt:
    st.print("\nShutting down...", 0.02)
    st.newLine()
