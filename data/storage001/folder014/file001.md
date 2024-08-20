# Multithreading/Concepts

**Concurrency:**  
Concurrency refers to the ability of a system to handle multiple tasks at once. In programming, it means that different parts of a program can be executed in an interleaved manner, allowing efficient use of system resources. Concurrency does not necessarily imply simultaneous execution but rather the ability to switch between tasks.

---

**Parallelism:**  
Parallelism is the simultaneous execution of multiple tasks at the same time. In programming, this means that different parts of a program are executed concurrently on different processors or cores. Parallelism is only possible on hardware that supports parallel processing.

---

**Process:**  
A process is an instance of a computer program that is being executed. It contains the program code and its current activity. Each process has its own memory space, which includes the program's code, data, and stack. Processes are independent, and the operating system manages them, providing isolation and protection between different processes.

---

**Thread:**  
A thread is the smallest unit of execution within a process. It is a sequence of programmed instructions that the operating system can manage independently. Threads within the same process share the same memory space, allowing them to communicate more easily but also making them more vulnerable to issues such as race

---

**Time-Slicing Algorithm:**  
Time-slicing is a scheduling method used in multitasking operating systems to allow multiple processes to share the CPU. In this approach, the CPU time is divided into small units called "time slices" or "quanta." Each process is assigned a time slice during which it can execute. If a process does not complete its execution within its allocated time slice, it is paused, and the CPU is given to the next process in the queue. This cycle continues, allowing all processes to make progress without any single process monopolizing the CPU. Time-slicing is commonly used in round-robin scheduling.

---

**Thread States:**  
In most operating systems, a thread can be in one of several states during its lifecycle:

1. **New:** The thread is created but has not yet started executing.
2. **Runnable:** The thread is ready to run and is waiting for CPU time. It may be running or waiting in the scheduler queue.
3. **Blocked/Waiting:** The thread is not eligible for execution until a certain condition is met or a resource becomes available. This can happen when the thread is waiting for I/O operations or other threads to release resources.
4. **Timed Waiting:** The thread is in a waiting state for a specified period. After the time elapses, it becomes runnable again.
5. **Terminated:** The thread has completed its execution and has exited. It cannot be restarted.

These states help manage and optimize how threads are executed and resources are utilized.

---

**Pros of Multithreading:**

1. **Increased Responsiveness:** Multithreading can make applications more responsive, especially in user interfaces where tasks like loading data and updating the display can be handled simultaneously.

2. **Improved Performance:** By utilizing multiple threads, applications can take advantage of multi-core processors, leading to better performance and faster execution of tasks.

3. **Resource Sharing:** Threads within the same process share the same memory space, which allows for efficient communication and data sharing without the need for inter-process communication.

4. **Concurrent Operations:** Multithreading allows multiple operations to occur simultaneously, improving the overall throughput of applications.

**Cons of Multithreading:**

1. **Complexity:** Writing multithreaded programs can be complex and error-prone, requiring careful management of resources and synchronization to avoid issues like race conditions and deadlocks.

2. **Debugging Challenges:** Debugging multithreaded applications can be difficult due to the non-deterministic nature of thread execution and timing issues.

3. **Overhead:** Creating and managing multiple threads can introduce overhead, which may offset the performance gains if not managed properly.

4. **Resource Contention:** Threads competing for the same resources can lead to contention and performance bottlenecks, reducing the benefits of parallel execution.

---
