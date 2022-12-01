import numpy as np
import matplotlib.pyplot as plt


#---------------------------------------------
#Recorded Data        User #1   2  3  4  5
createReminder = np.array([[12,22,15,10,14],#Time in seconds
                           [4,6,4,5,4],#User clicks
                           [4,4,4,4,4]])#Optimal Clicks

editReminder = np.array([[30,20,23,22,27],#Time in seconds
                        [7,5,5,5,6],#User clicks
                        [5,5,5,5,5]])#Optimal Clicks

deleteReminder = np.array([[15,10,10,12,16],#Time in seconds
                           [4,3,3,3,4],#User clicks
                           [3,3,3,3,3]])#Optimal Clicks

changeCalendar = np.array([[10,8,6,7,7],#Time in seconds
                           [5,4,3,3,3],#User clicks
                           [3,3,3,3,3]])#Optimal Clicks

#---------------------------------------------
#Mean and Standard Deviation Calculations
meanCreateReminder = np.mean(createReminder, axis=1)
meanEditReminder = np.mean(editReminder, axis=1)
meanDeleteReminder = np.mean(deleteReminder, axis=1)
meanChangeCalendar = np.mean(changeCalendar, axis=1)

SDCreateReminder = np.std(createReminder, axis=1)
SDEditReminder = np.std(editReminder, axis=1)
SDDeleteReminder = np.std(deleteReminder, axis=1)
SDChangeCalendar = np.std(changeCalendar, axis=1)

#---------------------------------------------
#Printing of Means and SD
print("-----------Means-----------")
print(meanCreateReminder[0], ":", meanCreateReminder[1], ":", meanCreateReminder[2],
      "->Create Reminder(User Time : User Clicks : Optimal Clicks)")
print(meanEditReminder[0], ":", meanEditReminder[1], ":", meanEditReminder[2],
      "->Edit Reminder(User Time : User Clicks : Optimal Clicks)")
print(meanDeleteReminder[0], ":", meanDeleteReminder[1], ":", meanDeleteReminder[2],
      "->Delete Reminder(User Time : User Clicks : Optimal Clicks)")
print(meanChangeCalendar[0], " :", meanChangeCalendar[1], ":", meanChangeCalendar[2],
      "->Change Calendar(User Time : User Clicks : Optimal Clicks)")

print("----Standard Deviations----")
print(round(SDCreateReminder[0], 2), ":", round(SDCreateReminder[1], 2), ":",
      round(SDCreateReminder[2], 2),
      "->Create Reminder(User Time : User Clicks : Optimal Clicks)")
print(round(SDEditReminder[0], 2), ":", round(SDEditReminder[1], 2), ":",
      round(SDEditReminder[2], 2),
      "->Edit Reminder(User Time : User Clicks : Optimal Clicks)")
print(round(SDDeleteReminder[0], 2), " :", round(SDDeleteReminder[1], 1), ":",
      round(SDDeleteReminder[2], 2),
      "->Delete Reminder(User Time : User Clicks : Optimal Clicks)")
print(round(SDChangeCalendar[0], 2), ":", round(SDChangeCalendar[1], 2), ":",
      round(SDChangeCalendar[2], 2),
      "->Change Calendar(User Time : User Clicks : Optimal Clicks)")

#---------------------------------------------
#Graphing

#Original Data
figure, axis = plt.subplots(2, 4)

#Create Reminder
axis[0,0].bar([1,2,3,4,5],createReminder[0][:])
axis[0,0].set_xticks([1,2,3,4,5])
axis[0,0].set_title("Create Reminder Time")
axis[0,0].set_ylabel("Time (S)")
axis[0,0].set_xlabel("User")

axis[1,0].bar([1,2,3,4,5],createReminder[1][:])
axis[1,0].plot([4,4,4,4,4,4,4], linestyle='solid', color='green')
axis[1,0].set_xticks([1,2,3,4,5])
axis[1,0].set_title("Create Reminder User Clicks")
axis[1,0].set_ylabel("# of user clicks")
axis[1,0].set_xlabel("User")
axis[1,0].legend(["Optimal Clicks"])

#Edit Reminder
axis[0,1].bar([1,2,3,4,5],editReminder[0][:])
axis[0,1].set_xticks([1,2,3,4,5])
axis[0,1].set_title("Edit Reminder Time")
axis[0,1].set_ylabel("Time (S)")
axis[0,1].set_xlabel("User")

axis[1,1].bar([1,2,3,4,5],editReminder[1][:])
axis[1,1].plot([5,5,5,5,5,5,5], linestyle='solid', color='green')
axis[1,1].set_xticks([1,2,3,4,5])
axis[1,1].set_title("Edit Reminder User Clicks")
axis[1,1].set_ylabel("# of user clicks")
axis[1,1].set_xlabel("User")
axis[1,1].legend(["Optimal Clicks"])

#Delete Reminder
axis[0,2].bar([1,2,3,4,5],deleteReminder[0][:])
axis[0,2].set_xticks([1,2,3,4,5])
axis[0,2].set_title("Delete Reminder Time")
axis[0,2].set_ylabel("Time (S)")
axis[0,2].set_xlabel("User")

axis[1,2].bar([1,2,3,4,5],deleteReminder[1][:])
axis[1,2].plot([3,3,3,3,3,3,3], linestyle='solid', color='green')
axis[1,2].set_xticks([1,2,3,4,5])
axis[1,2].set_title("Delete Reminder User Clicks")
axis[1,2].set_ylabel("# of user clicks")
axis[1,2].set_xlabel("User")
axis[1,2].legend(["Optimal Clicks"])

#Delete Reminder
axis[0,3].bar([1,2,3,4,5],changeCalendar[0][:])
axis[0,3].set_xticks([1,2,3,4,5])
axis[0,3].set_title("Change Calendar Time")
axis[0,3].set_ylabel("Time (S)")
axis[0,3].set_xlabel("User")

axis[1,3].bar([1,2,3,4,5],changeCalendar[1][:])
axis[1,3].plot([3,3,3,3,3,3,3], linestyle='solid', color='green')
axis[1,3].set_xticks([1,2,3,4,5])
axis[1,3].set_title("Change Calendar User Clicks")
axis[1,3].set_ylabel("# of user clicks")
axis[1,3].set_xlabel("User")
axis[1,3].legend(["Optimal Clicks"])

plt.show()



