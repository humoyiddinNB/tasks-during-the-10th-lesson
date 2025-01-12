import os
import threading
import multiprocessing
import time

os.system("clear")

# def process_file():
#     for i in range(5):
#         with open("my_text1.txt", "w") as file:
#
#
# start = time()
# def process_file(file_name):
#     with open(file_name)
#
# if name == "main":
#     files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
#     processes = []
#
#     for file in files:
#         process = Process(target=process_file, args=(file,))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     print("All files are processed!")
# print(time() - start)

#
# sonlar = [i for i in range(1, 19)]
# sonlar1 = set(sonlar)
# print(sonlar1)
# # count  = 0
# # for i in sonlar:
# #     print(i)








### 1-misol  fileni ochib beradigan contex manager
# def ochar_funk(file_name, mode):
#     try:
#         file = open(file_name, mode)
#         if mode == "w":
#             file.write("python")
#         if mode == "r":
#             return file.read()
#         if mode == "a":
#             file.write("bu append qilinngan matn")
#     except FileNotFoundError:
#         return f"{file_name} not found"
#     finally:
#         if file:
#             file.close()
#
# my_file = ochar_funk("text.txt", "r")
# print(my_file)






#####  2-misol  funksiya ko'rinishidagi kontex manger
# @contextmanager
# def file_manager(file_name, mode):
#     try:
#         file = open(file_name, mode)
#         yield file
#     except:
#         file.close()
#
# with file_manager("my_text", "r")as file:
#     # file.write("salom oshna")
#     print(file.read())









####    multi threatining
# start = time.time()
#
# numbers = list(range(1_000_000))
#
# def task1():
#     for i in numbers:
#         print(i)
#
# def task2():
#     for i in numbers:
#         print(i ** 2)
#
#
# def task3():
#     for i in numbers:
#         print(i / 2)

# # threading1 = threading.Thread(target=task1())
# # threading2 = threading.Thread(target=task2())
# # threading3 = threading.Thread(target=task3())
# #
# # threading1.start()
# # threading2.start()
# # threading3.start()
# #
# # threading1.join()
# # threading2.join()
# # threading3.join()
#
# task1()
# task2()
# task3()
#
# print(f"Hammasi tugadi, ketgan vaqt: {time.time() - start}")







#####   mutiproccessing misol
# def calculate_nums(number):
#     print(f"calculating square of the {number}")
#     time.sleep(5)
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]
#     processes = []
#
#     for number in numbers:
#         process = multiprocessing.Process(target=calculate_nums, args=(number, ))
#         processes.append(process)
#         process.start()
#
#     for proces in processes:
#         proces.join()
#
#     print("Barcha jarayonlar tugadi")







#### filega son yozadigan multiprossing qilingan file
# start = time.time()
#
# def yozar(file_name):
#     with open(file_name, "w") as file:
#         for num in range(1000000):
#             file.write(f"{num}  ")
#
# if __name__ == "__main__":
#     files = ["myfile1.txt", "myfile2.txt", "myfile3.txt", "myfile4.txt", "myfile5.txt"]
#     processes = []
#
#     for file in files:
#         proces = multiprocessing.Process(target=yozar, args=(file,))
#         processes.append(proces)
#         proces.start()
#
#     for proces in processes:
#         proces.join()
#
# print(f"All this tasks have been done, spanded time: {time.time() - start}")
#
#



####        Pool bilan sihlaydigan multiprosserga misoollar
# def do(work):
#     print("Workers are doing tasks")
#     sleep(2)
#     return f"{work} done"
#
# tasks = range(1, 12)
#
# if __name__ == "__main__":
#     with Pool(2) as pool:
#         result = pool.map(do, tasks)
#         print(result)