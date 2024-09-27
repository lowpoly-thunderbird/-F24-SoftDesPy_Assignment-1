from plugin import Plugin, onLoadDecorator
import plugin
from printStyle import style as st
import sys

StartText="""

Great tool to compare real price of filament.
Only measurement, which accurately tells you how
much you can print with your purchased filament,
is volume in cm3. Filament vendors should provide
price per cm3 which doesn't happen now. So I made
this simple tool for you to calculate it.

#################################################
Example: You are offered 100m of PLA both in 3mm
and 1.75mm for $25. With 3mm you will buy 2827cm3
but with 1.75mm just 962cm3 of plastic. That
renders 1.75mm deal pretty awful as you will get
just one third for the same price.
#################################################
"""

FilamentSelector="""

Choose filament:
(used to determine density)

>pla    >abs    >petg   >sbs

>"""

Calculations="Price per cm3:    Total volume cm3:\n"

class HelloPlugin(Plugin):
    Name = "Real filament price"

    @onLoadDecorator
    def OnLoad(self):
        st.newLine()
        st.print('     "Real filament price" plugin Loaded!', 0.02)
        st.newLine()
        st.newLine()

    def OnCommand(self, cmd, args):
        if cmd == "1" :
            st.newLine()
            st.newLine()
            st.print(">>Real filament price", 0.02)
            st.newLine()
            st.print(StartText,0.008)
            st.print(FilamentSelector, 0.02)
            
            Density=0
            while True:
                
                 match input():
                    case "pla":
                        Density=1.25
                        break
                    case "abs":
                        Density=1.04
                        break
                    case "petg":
                        Density=1.23
                        break
                    case "sbs":
                        Density=1.11 
                        break
                    case _:
                        st.print("Incorrect input", 0.02)
                        st.newLine()
                        st.print(">", 0.02)

            st.print("Enter weight (g)", 0.02)
            st.newLine()
            st.print(">", 0.02)
            
            Weight = int(input())

            st.print("Enter package price", 0.02)
            st.newLine()
            st.print(">", 0.02)
            
            Price = int(input())
            ########################################
            #st.print("Enter package price", 0.02)

            PricePCM = lambda x,y: x/y
            Volume = lambda x,y: x/y
            
            st.print(Calculations, 0.02)
            st.print(str(PricePCM(Price,Weight)), 0.02)
            st.print("               ", 0.02)
            st.print(str(int(Volume(Weight,Density))),0.02)
            st.newLine()

            st.print("Press 'P' to choose plugin or 'C' to exit", 0.02)
            st.newLine()

            while True:
                st.print(">", 0.08)
                a = input()
                if a == "p" or a == "P":
                    st.newLine()
                    plugin.LoadPlugins()
                    st.newLine()
                    ''''''''
                    st.print("Choose plugin (number):", 0.02)

                    while 1:
                        #print(">")

                        a = input().split(" ")

                        for p in plugin.Plugins.keys():
                            plugin.Plugins[p].OnCommand(a[0], a[1:])
                    ''''''''''''
                    break
                if a == "c" or a == "C":
                    st.print("\nShutting down...", 0.02)
                    st.newLine()
                    sys.exit()
                else:
                    st.print("Incorrect input", 0.02)
                    st.newLine()


        else:
            return False
''''''