#!/usr/bin/env python
# coding: utf-8

# In[1]:


#22BCI0194 #DANISH SHAH
number_of_processes=int(input("Enter the number of processes:"))
# Initialize lists to store process information
processes=[]
arrival_times=[]
burst_times=[]
# Input arrival and burst times for each process
for i in range(number_of_processes):
 processes.append(i+1)
 arrival_times.append(int(input(f"Enter the number of processes {i + 1}: ")))
 burst_times.append(int(input(f"Enter the number of processes {i + 1}: ")))


# In[2]:


# Combine process information into a list of tuples and sort by arrival time
process_info=list(zip(processes,arrival_times,burst_times))
process_info.sort(key=lambda x:x[1])
processes,arrival_times,burst_times=zip(*process_info)


# In[9]:


completion_times = [0] * number_of_processes  # Initialize an array to store completion times

for i in range(number_of_processes):
    if i == 0:
        completion_times[i] = arrival_times[i] + burst_times[i]
    else:
        completion_times[i] = max(completion_times[i - 1], arrival_times[i]) + burst_times[i]


# In[10]:


# Calculate turnaround times
turnaround_times=[0]*number_of_processes
for i in range(number_of_processes):
 turnaround_times[i]=completion_times[i]-arrival_times[i]


# In[11]:


# Calculate waiting times
waiting_times=[0]*number_of_processes
for i in range(number_of_processes):
 waiting_times[i]=turnaround_times[i]-burst_times[i]


# In[13]:


# Assuming processes, arrival_times, burst_times, completion_times, turnaround_times, and waiting_times are defined

# Print header
print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")

# Print details for each process
for i in range(number_of_processes):
    print(f"{processes[i]}\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")


# In[ ]:




