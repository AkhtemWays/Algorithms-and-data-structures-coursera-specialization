# python3

#
# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     workers = [i for i in range(n_workers)]
#     assert len(jobs) == n_jobs
#     start_time = {} # initialization of starting time
#     for i in workers:
#         start_time[i] = 0
#     answer = []
#     if len(jobs) <= len(workers): # check whether amount of threads is less than jobs
#         for i in range(len(jobs)): # in that case just return threads in order with initialized time
#             print(workers[i], start_time[i])
#     else:
#         for i, j in zip(range(len(workers)), jobs[:len(workers)]): # jobs amount is bigger than threads per job
#             answer.append((i, 0)) # here we get rid of all the threads making them busy
#             start_time[i] = j
#         jobs = jobs[len(workers):]
#         for job in jobs: # then work with the rest of jobs with starting time
#             minimum_value = float('inf')
#             minimum_key = 0
#             for key in start_time.keys():
#                 if start_time[key] < minimum_value:
#                     minimum_value = start_time[key]
#                     minimum_key = key
#             answer.append((minimum_key, minimum_value))
#             start_time[minimum_key] += job
#     for worker, beginning in answer:
#         print(worker, beginning)
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     main()


def create_width_of_str(width):
    space = ' '
    strr = space*width
    return strr

def create_full_string(text, width):
    width_string = create_width_of_str(width)
    return text + width_string

def ticker(text, width, tick):
    length_of_text = len(text)
    overall_length = length_of_text + width
    needed_tick = tick%overall_length
    string_to_display = create_width_of_str(width)
    full_string = create_full_string(text, width)
    if needed_tick == 0:
        return string_to_display
    elif needed_tick == width:
        return full_string[:width]
    elif needed_tick <= width:
        space = " "
        needed_space = space*(width-needed_tick)
        return needed_space + full_string[:needed_tick]

    else:
        return full_string[needed_tick-width:needed_tick]
print(ticker("Should work in cycle", 10, 42))
def demo(text, width):
    for tick in range(100):
        print(ticker(text, width, tick))
demo('Beautiful is better than ugly.', 10)

arr = [1.0, 2.0, 3.0]


def blocks(s):
    dicti = {}
    for i in s:
        if i not in dicti:
            dicti[i] = 0
    for i in s:
        dicti[i] += 1
    maximum_blocks = max(dicti.values())
    work_list = list(s)
    result = []

    for i in range(maximum_blocks):
        new_work_list = [i for i in work_list]
        arr = []
        indices_to_remove = []
        for j,let in enumerate(new_work_list):
            if let not in arr:
                arr.append(let)
                indices_to_remove.append(j)
        result.append(arr)
        for k in arr:
            work_list.remove(k)
    str = "".join(result[0])
    result = result[1:]
    for i in result:
        str = str + "-" + "".join(i)
    return str



print(blocks("abaacdb"))



