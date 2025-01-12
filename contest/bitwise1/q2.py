"""
There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

"""
from typing import List
import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.system = {}

        for userID, taskID, priority in tasks:
            if taskID in self.system:
                self.system[taskID].append((userID, priority))
            else:
                self.system[taskID] = [(userID, priority)]

        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # guaranteed that taskId does not exist in the system
        if taskId in self.system:
            self.system[taskId].append((userId, priority))
        else:
            self.system[taskId] = [(userId, priority)]



    def edit(self, taskId: int, newPriority: int) -> None:
        # guaranteed that taskId exists in the system
        existing = self.system[taskId]
         
        # print(">>",existing)
        for i in range(len(existing)):
            existing[i] = (existing[i][0], newPriority)



        self.system[taskId] = existing



        

    def rmv(self, taskId: int) -> None:
        # guaranteed that taskId exists in the system
        del self.system[taskId]


        

    def execTop(self) -> int:
        heap=[]


        for key, value in self.system.items():
            for val in value:
                heapq.heappush(heap, (-val[1], -val[0], key))
        
        print(heap)
        if not heap:
            return -1


        if len(heap) >1 and  heap[0][0] != heap[1][0]:
            # remove the taskId fomr the system
            del self.system[heap[0][2]]
            return -heap[0][1] # return the user id
        if len(heap) == 1:
            # remove the taskId fomr the system
            del self.system[heap[0][2]]
            return -heap[0][1] # return the user id

        # if multiple tasks with same priority
        maxTask = heap[0][2]
        user = -heap[0][1]
        maxPriority = -heap[0][0]
        print(maxPriority, maxTask, user)

        while heap:
            pri,cu,task= heapq.heappop(heap)
            # if the task is not max then break
            if maxPriority!= -pri:
                break

            if task > maxTask:
                maxTask = task
                user = -cu
        
        # remove the taskId fomr the system
        del self.system[maxTask]
        return user


            




        
# [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
tm = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
# tm.add(4, 104, 5)
# tm.edit(102, 8)
# tm.rmv(101)
# print(tm.execTop())
# tm.add(5, 105, 15)
# print(tm.execTop())
#

# [[[[7,15,14],[2,2,48],[2,19,4]]],[]]
tm = TaskManager([[7,15,14],[2,2,48],[2,19,4]])
# print(tm.execTop())

# [[[[10,4,10],[10,0,6],[5,23,50],[3,29,50],[2,15,9]]],[]]
tm = TaskManager([[10,4,10],[10,0,6],[5,23,50],[3,29,50],[2,15,9]])
print(tm.execTop())

# [[[[6,5,23]]],[],[]]

tm = TaskManager([[6,5,23]])
print(tm.execTop())
print(tm.execTop())
