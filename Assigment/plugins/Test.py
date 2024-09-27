from plugin import Plugin, onLoadDecorator
import plugin
from printStyle import style as st


class HelloPlugin(Plugin):
    Name = "Test plugin: can be used to create new calculation scenario"

    @onLoadDecorator
    def OnLoad(self):
        st.newLine()
        st.print('     "Test plugin name" plugin Loaded!', 0.02)
        st.newLine()

    def OnCommand(self, cmd, args):
        if cmd == "2":
            st.newLine()
            st.print("Test plugin: can be used to create new calculation scenario", 0.02)
            st.newLine()
            st.print("Press any key to choose plugin", 0.02)
            st.newLine()
            st.print(">", 0.02)
            a=input()
            plugin.LoadPlugins()

            st.newLine()
            st.print("Choose plugin (number):", 0.02)

            while 1:
                #print(">")

                a = input().split(" ")

                for p in plugin.Plugins.keys():
                    plugin.Plugins[p].OnCommand(a[0], a[1:])
            
            return True
        else:
            return False
            
