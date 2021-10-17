# Coroutines, event loops and futures

There are few common elements that most asynchronous programs have, and coroutines, event loops, and futures are three of those elements. They are defined as follows:

* **Event loops** are the main coordinators of tasks in an asynchronous program. An event loop keeps track of all of the tasks that are to be run asynchronously, and decides which of those tasks should be executed at a given moment. In other words, event loops handle the task switching aspect (or the execution flow) of asynchronous programming.
* **Coroutines** are a special type of function that wrap around specific tasks, so that they can be expected asynchronously. A coroutine is required in order to specify where in the function the task switching should take place; in other words, they specify when the function should give back the flow of execution to the event loop. The tasks for coroutines are typically either stored in a task queue or created inside the event loop.
* **Futures** are placeholders for the results returned from coroutines. These future objects are created as soon as coroutines are initiated in the event loop, so futures can represent actual resuts, pending results (if the coroutines have not finished executing), or even an exception (if that is what the coroutine will return)

