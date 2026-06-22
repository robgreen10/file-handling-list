# lead-pipeline-mutator
This project demonstrates how Python handles memory management and object mutability through a dynamic queue tracking script. By utilizing the .pop(0) method inside an isolated function, the script extracts the first element of a list while directly altering the parent array's state. The codebase serves as a clear architectural example of how passing lists by reference can cause permanent, global data modifications across an execution environment.


In-Place Mutation: The .pop(0) method shifts the entire array in memory by extracting the target index and instantly shrinking the dataset's length.

Pass-by-Reference Behavior: Python does not duplicate lists when they are passed into a function, meaning any structural modifications made inside the block will permanently impact the global variable.

State Preservation: To prevent a function from mutating your master dataset, you must explicitly pass a duplicate of the array using the .copy() method.
