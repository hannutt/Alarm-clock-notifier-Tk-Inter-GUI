import datetime
import time
from tkinter import *
from tkinter import ttk
from pygame import mixer
from tkinter import filedialog
from tkinter.font import Font
from plyer import notification

mixer.init()

#luodaan funktio, joka näyttää tämänhetkisen ajan muodossa tunnin,minuutit ja sekunnit.
def timeNow():
    currenttime = time.strftime('%H:%M:%S')
    timeLabel.config(text = currenttime)
    timeLabel.after(1000,timeNow)

#luodaan funktio, jolla valitaan soitettava kappale ja asetetaan haluttu
#hälytysaika.
def setAlarm():
    track = filedialog.askopenfilename()
    timenow = datetime.datetime.now()
    hours = int(Entry.get(setHour))
    minutes = int(Entry.get(setMin))
    while True:
        if hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:
            mixer.music.load(track)
            mixer.music.play()
            break

#funktio, jolla musiikin toisto lopetetaan.
def stopAlarm():
    mixer.music.stop()

    
#funktio, joka nostaa muistutuksen työpöydälle haluttuun kellonaikaan.
def notify():
    note = (Entry.get(noteEntry))
    timenow = datetime.datetime.now()
    hours = int(Entry.get(setHour))
    minutes = int(Entry.get(setMin))
    while True:
        if hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:
            notification.notify(title = 'Remember', message = note)
            break
    

        
#luodaan pohjakomponentti ja frame komponentit. frame komponenttien avulla
#asetellaan muut komponentit
root = Tk()
root.configure(background = 'LightBlue3')
root.title('Clock & notify')
frame1 = Frame()
frame1.configure(background = 'LightBlue3')
frame2 = Frame()
frame2.configure(background = 'LightBlue3')
frame3 = Frame()
frame3.configure(background = 'LightBlue3')
frame4 = Frame()
frame4.configure(background = 'LightBlue3')
frame5 = Frame()
frame5.configure(background = 'LightBlue3')

#tallennetaan otsikkofontti muuttujaan
titlefont = Font(family = 'Segoe UI Black')


#lisätään pudotusvalikkoihin numerot
hours = [00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
minutes = [59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38
           ,37,36,35,34,33,32,31,30,39,38,37,36,35,34,33,32,31,30,29,28
           ,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6
           ,5,4,3,2,1,0]

#luodaan pudotusvalikot
setHour = ttk.Combobox(frame1, width = 5, values = hours)
setMin = ttk.Combobox(frame2, width = 5, values = minutes)

#luodaan tekstikomponentit label komennolla
name = Label(root, text = 'Alarm clock & notifier', font = titlefont, bg = 'LightBlue3')
minLabel = Label(frame2, text = 'Set minute: ',bg = 'LightBlue3')
hourLabel = Label(frame1, text = 'Set hour: ',bg = 'LightBlue3')
timeLabel = Label(frame3)
noteLabel = Label(frame5, text = 'Write a note here: ')
nowLabel = Label(frame3, text = 'Time now: ')

#luodaan painikkeet button komennolla, command komennolla kerrotaan
#mikä funktio suoritetaan kun painiketta painetaan.

setbtn = Button(frame4, text = 'Set alarm', command = setAlarm)
stopbtn = Button(frame4, text = 'Stop alarm', command = stopAlarm)
notebtn = Button(root, text = 'Set note', command = notify)

#luodaan syötekentät entry komennolla
noteEntry = Entry(frame5)



#kutsutaan timenow funktiota
timeNow()

#pakataan komponentit
name.pack()
frame3.pack()
nowLabel.pack(side=LEFT)
timeLabel.pack(side=RIGHT)
frame1.pack()
frame2.pack()
hourLabel.pack(side = LEFT)
setHour.pack(side = RIGHT,pady=4,padx=4)
minLabel.pack(side = LEFT)
setMin.pack(side = RIGHT,pady=4,padx=4)
frame4.pack()
frame5.pack()
noteLabel.pack(side=LEFT)
noteEntry.pack(side=RIGHT,pady=4,padx=4)
setbtn.pack(side=LEFT,pady=4,padx=4)
stopbtn.pack(side=RIGHT,pady=4,padx=4)
notebtn.pack(pady=4)
