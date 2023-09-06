import multiprocessing
import os

# Lightweight IPC mechanisms example: Using shared memory
def child_process(shared_data):
    print(f"Child Process (PID: {os.getpid()}) received data: {shared_data.value}")

if __name__ == "__main__":
    # Create a shared memory object
    shared_data = multiprocessing.Value("i", 0)

    # Create a child process and pass the shared memory to it
    child = multiprocessing.Process(target=child_process, args=(shared_data,))
    child.start()

    # Modify the shared data from the parent process
    shared_data.value = 42

    # Wait for the child process to finish
    child.join()

    print(f"Parent Process (PID: {os.getpid()}) updated shared data: {shared_data.value}")
