import os
import sys
import time
from printStyle import style as st

# Plugins = []
Plugins = dict()


def onLoadDecorator(func):
    def Return(*args, **kwargs):
        st.print("Loading plugin...", 0.02)
        st.newLine()
        time.sleep(0.5)
        st.print("       ", 0)
        func(*args, **kwargs)

    return Return


class Plugin:
    Name = "undefined"

    @onLoadDecorator
    def OnLoad(self):
        pass

    def OnCommand(self, cmd, args):
        pass


def LoadPlugins():
    ss = os.listdir("plugins")
    sys.path.insert(0, "plugins")

    loadingResult = -1

    for s in ss:
        loadingResult += 1
        # time.sleep(0.5)
        if s != "__pycache__":
            st.print("<", 0.02)
            st.print(str(loadingResult+1), 0.02)
            st.print(">Found plugin" + str(s), 0.02)
            st.newLine()
        time.sleep(0.5)

        __import__(os.path.splitext(s)[0], None, None, [""])

    st.newLine()
    st.print(str(loadingResult), 0.02)
    st.print(" plugin(s) detected", 0.02)
    st.newLine()
    st.newLine()

    for plugin in Plugin.__subclasses__():
        p = plugin()
        # print(plugin.Name)
        # print(p.__class__.__name__)
        Plugins[plugin.Name] = p
        # Plugins.append(p)
        p.OnLoad()

    return
