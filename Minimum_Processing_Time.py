class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        core_task = []
        count = 0
        i = 0
        time = 0
        while i < len(tasks):
            task_list = []
            while i < len(tasks) and count < 4:
                task_list.append(tasks[i])
                i += 1
                count += 1
            count = 0
            core_task.append(task_list)
        j = 0
        for i in range(len(core_task)):
            time = max(time, (processorTime[j] + max(core_task[i])))
            print(time, i)
            j += 1
        print(core_task)
        return time
        
        
