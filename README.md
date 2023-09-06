# ipc_rpc_optimization
Here's the example of IPC/RPC optimization
In this example:

We demonstrate lightweight IPC using shared memory in Python's multiprocessing module.
A shared memory object shared_data is created with an initial value of 0.
We create a child process that accesses the shared memory using the multiprocessing.Process class.
In the parent process, we modify the value of shared_data to 42.
After that, we wait for the child process to finish using child.join().
Finally, we print the updated value of shared_data in both the parent and child processes.
