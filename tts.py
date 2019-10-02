#CR William Collins 2019#
#Text to Speach to Perform Weather Data Forecast.  
#JSON Return of weather data, parse and communicate via Speach#
#Wikipedia return of text and speech#
# Wikipedia API and Data Parsing#
# Lib:  pip install wikipedia   #

import wikipedia
searchtxt = "machine learning"

i=0 
while i<1:
    searchtxt = input("Please enter search string for Wikipedia lookup:\n")

    search = wikipedia.search (searchtxt)
    print ("Search Result=\n",search)

    suggest = wikipedia.suggest (searchtxt)
    print ("Suggest Result=\n",suggest)

    summary = wikipedia.summary (searchtxt)
    print ("Summary Result=\n",summary)

    import pyttsx3
    engine = pyttsx3.init() # object creation

    """ RATE"""
    rate = 200
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', rate )     # setting up new voice rate
    rate = engine.getProperty('rate')   # getting details of current speaking rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    #engine.say("Hello World!")
    #engine.say('My current speaking rate is ' + str(rate))
    print ("Wiki Search Text=\n", searchtxt)
    engine.say(summary)
    engine.runAndWait()
    engine.stop()