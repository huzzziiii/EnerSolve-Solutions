import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import time

#os.system("scp Bruh.txt pi@raspberrypi:Desktop")



#while True:

#Step 1: Parse through the home XML files
tree=etree.parse('house.xml')
root=tree.getroot()

#Step 2: Parse through the log xml FILE
tree2=etree.parse('logFile.xml')
root2=tree2.getroot()

etree.SubElement(root.find("CLoad"),"current-load")

#Step 3: Read current consumption
#currentLoad=root.find("current-load")


#forecastLoad=root.find("forecast-load")
#negotiate=root.find("negotiate")

#print("Current load: ",currentLoad.text)

##Step 4: Create a new element
#etree.SubElement(root2.find("CurrentLoad"), "current-load")

#etree.SubElement(root2.find("ForecastLoad"), "forecast-load")
#etree.SubElement(root2.find("NegotiateOrNot"), "negotiate")
#etree.SubElement(root2.find("NegotiateLoad"), "negotiate-load")

#Step 5: Enter the current consumption into the Log file
#root[0].find("current-load[0]").text=currentLoad.text

#root2[1].find("forecast-load[0]").text=forecastLoad.text
#root2[2].find("negotiate[0]").text=negotiate.text
#
#Step 6: Update the Log XML file
tree.write('house.xml');