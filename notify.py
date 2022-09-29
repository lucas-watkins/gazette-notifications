import GazetteNewsAPI as gpi
from tkinter import messagebox as msg
from time import sleep, time
from threading import Thread
from os import getlogin

def adgendaAndLunch(): # Shortcut to show info window
  msg.showinfo('Gazette Notification: Lunch and Agenda', gpi.adgendaAndLunch())

def announcementsAndAthletics(): # Shortcut to show info window
  msg.showinfo('Gazette Notification: Athletics', gpi.announcementsAndAthletics())

adgendaAndLunch() # Run each method the first time
announcementsAndAthletics()

first_run_lunch = gpi.adgendaAndLunch()
first_run_athletics = gpi.announcementsAndAthletics()

error_counter = 0
def payload1():
  while True:
    try:
      sleep(600) # Wait 10 mins

      # If adgenda and lunch or athletics and announcements 
      # are the same do nothing, but if they are different update stored information and show updated notif
      if first_run_lunch == gpi.adgendaAndLunch() or first_run_athletics == gpi.announcementsAndAthletics():
      
        print('Debug: Gazette is the same')
      
      else:
        adgendaAndLunch()
        announcementsAndAthletics()
        first_run_lunch = gpi.adgendaAndLunch()
        first_run_athletics = gpi.announcementsAndAthletics()
      
    
      # Error Handling: Create counter and if error show 1 error msg every hour

    except:
      if error_counter == 6:
        msg.showerror('Gazette Error', 'No Internet Connection or Unexpected Error')
        error_counter = 0
      else:
        print('Debug: Error')
        error_counter += 1
     
def payload2():
    '''
Idea: write every some seconds to a file and check regularly.
It is assumed that if the time delta is too big,
the computer just woke from sleep.
'''

  

    TSFILE= r'C:\\Users\\' + getlogin() + '\\tsfile.txt'
    CHECK_INTERVAL= 10
    CHECK_DELTA = 15

    def wake_up_from_sleep():
      adgendaAndLunch()
      announcementsAndAthletics()

    while True:
        curtime = time()
        with open(TSFILE, "w") as fd:
            fd.write("%d" % curtime)
        sleep(CHECK_INTERVAL)
        print('Debug: Slept through check interval')
        with open(TSFILE, "r") as fd:
            old_ts = float(fd.read())
            print('Debug: Read file')
        curtime = time()
        if old_ts + CHECK_DELTA < curtime:
            print('Debug: old_ts + CHECK_DELTA:', old_ts + CHECK_DELTA,)
            print('Debug:', curtime)
            wake_up_from_sleep()


Thread(target = payload1).start()
Thread(target = payload2).start()