"""
                                DSA CheatSheet

                OOP

    Abstract Class : A class that can contain abstract methods and cannot be instantiated directly. It can have both abstract and regular methods.

    Interface : A structure that contains only method signatures. It supports multiple inheritance.

    Polymorphism : Allows the same method to behave differently. It is divided into Overriding and Overloading.

    Overloading : Methods defined in the same class with the same name but different parameters.

----------------------------------------------------------------------------------------------------------------------------------------------

                System Design


    Vertical Scaling : Updating the server like cpu ram etc but it eventually reaches the max point.
    Horizontal Scaling : We create multiple servers and we use load balancer to decide when to switch between servers. Ex / After 100 users switch to the other service.
    Logging (external) : Trace the logs for every users. If there is an error immidiately fix it.
    Metrics (external) : How the system reacts for user actions . Can it handle requests without an issue. Time series. Positive or negative trend ? cpu can handle requests or has a bottleneck .
    Alerts : When something bad happens . Alert system takes info from metrics and email developers

                Design Requirements
    1 - Move Data
    2 - Store Data
    3 - Transform Data

    Availability = It should be 99.999 optimal. Which means in a year system only off 5 minutes. Service Level Objective(SLO) < Service Level Aggreement(SLA)(refund) -> uptime / uptime + downtime
    Reliability -> Probability system wont fail 
    Fault Tolerance -> If one server is down and we can continue with the other one the system has fault tolerance.
    Redundancy -> It is like copy. Server has an identical server so its redundant but it is required in order to prevent failures.
    Throughput -> measured by request per second - how many concurrent user can system handle ---> For database = Queries per second(QPS) ---> For data = Bytes per second
    Latency -> Entire operation time -> how long each individual request takes -> CDN

                Networking
    Ip Header : Metadata from ip --> to ip etc
    Tcp Ip : Sequence number
    Static and Dynamic ip adresses --> Check Dynamic Dns
    Tcp / Ip : Reliable -> 3 way handshake
    Udp / Ip : Faster but no guarantee for data integrity --> Commonly used for streaming data like live videos etc.
    
                API

    RPC : Remote Procedure Call. Ex/ gRPC
    Info : 100-199
    Success : 200-299
    Redirection : 300-399
    Client Error : 400-499
    Server Error : 500-599

    Websockets : Connect via http and update response immediately

    GraphQL : Uses htpp post. Solves overfetching and also underfetching ( making lots of request ). Single endpoint -> Query and mutation

    gRPC : HTTP/2 . Mostly used server to server communications. Protocol Buffers

                API Design
    
    Do not add verbs to http endpoints -> getVideos should be videos for rest apis

                Caching
    Write-around cache : simply only update database
    Write-through cache : immidiately update cache then update database
    Write-back cache : Faster but inconsistent -> simply only update cache and periodically update database
    Eviction Policy : deciding which part of the cache will remove after cache is full
        Random
        FIFO
        LRU : Least recently used
        LRU : Least frequently used

                CDN ( Content Delivery Network )

    Static Content : Ex / images , videos
    Push cdn & pull cdn : Pull CDN is better because push cdn strategy we have lots of unnecessary data

                Proxies & Load Balancers
    Forward and Reverse Proxy
    Proxy Server : Ex / you cant access a server but proxy server can . So proxy server access the wanted server for you ---- or opposite proxy server can limit your actions like corporate proxy cant access instagram etc
    Forward proxy ex : VPNs hides the client
    Reverse proxy : ex : CDNs & Load Balancer hides the actual server

    Load Balancer Algorithms:
        Round Robin : first request goes server 1 second goes 2 ... cycles requests
        Weighted Round Robin : We arrange request by percentage like %50 of the requests will go server 1 etc.
        Least Connections : We send the coming request to the server which has least connections.
        Location : location based arrangement
        Hashing

        Layer 4 vs Layer 7 : Layer 4 is network(Tcp) layer, Layer 7 is the application layer --> Layer 4 load balancer will be faster but less flexible because can see application data /// see more maglev paper by google

        
                Consistent Hashing
    According to ip address we hash the value and redirect users by their ip address so everytime users will redirect to the same server. This can be helpful when working with in memory redis etc.
    If we want to map users how we want to and we need consistent data than we need to use consistent hashing.
    When one server crashes the requests goes to the nearest server according to the hashing algorithm.
    Clockwise strategy : nearest server in clockwise direction.

    Rendezvous hashing is another approach to consistent hashing.

    Consistent hashing consists of 3 main parts : Hashkey , HashFunction , Nodes

                SQL
    ACID stands for : Atomicity , Consistency , Isolation , Durability
    Atomicity : A transaction is treated as a single atomic unit. All steps that make up the transaction must succeed or the entire transaction rolls back. If they all succeed, the changes made by the transaction are permanently committed to the managing system.
    Consistency : A transaction must preserve the consistency of the underlying data. The transaction should make no changes that violate the rules or constraints placed on the data.
    Isolation : A transaction is isolated from all other transactions. Transactions can run concurrently only if they don't interfere with each other.
    Durability : A transaction that is committed is guaranteed to remain committed -- that is, all changes are made permanent and will not be lost if an event such as a power failure should occur. 

                NoSql
    Document database : Mongo DB
    Write-column database : when you have a situation needs lots of writing and minor reading. Ex / Casssandra , BigTable
    Graph based database : Nodes etc

    Scaling NoSql : Scaling sql databases horizontally is hard because of ACID but NoSql can scale with ease.
    NoSql version ACID :  BaSE -> Eventual Consistency = We have two replicas one is leader one is follower

                Replication & Sharding
    Leader - Follower or Master - Slave Replication : Leader can write/read and Follower can only read
    Multi Master Replication : Multiple masters 

    Sharding : If we have large amount of data . We take a database broken it into smaller databases aka database shards
        Ex / Half of the table goes one db with external server and other one goes another. It can be more like 10 100 etc
        ShardKey : How to split database

                CAP Theorem
    C - Consistency : Data consistency between databases
    A - Availability : 
    P - Partition Tolerance : When one of the databases crashes other ones should be able to run without issue.

    We choose p always and c or a.

                Object Storage
    Aws S3
    Stored in a flat way
    BLOB : Binary Large Object / Images , videos
    We cant update the files only read and write

                Message Queues
    Pub/Sub : Publisher / Subscriber
    Topic

                MapReduce
    Batch vs Streaming
    WordCount : Batch processing use case
    Real time : Streaming
    Batch works with already exist data streaming is real time. 

    MapReduce : One of the workers can be master and decide how data must be splitted.
        First Step Map layer : First input split among the workers ex 1/3 and map the input according to given map function. 
        Middle Step Shuffle : Shuffle words
        Last Step Reduce :  Aggregate the data and group "the" word 110 occurence.
        Ex : Batch : Spark , Hadoop -- Streaming : Flink

                System Design Interview
    
    How to approach : Scoping -> What specific part do we want to focus on ?
    Do not make assumptions clarify the requirements. What exactly the interviewer wants from you ?

    Functional Requirements : The apps requirements
    Non-Functional Requirements : Scalability -> throughput, storage capacity --- Performance -> Latency , availability , 

    Back of the envelope calculations :
        Thoroughput : 60 * 60 * 24 --> 86400
        10 billion / 100k approximately = 100000 read per second and 100 write per second

                Design a Rate Limiter
    Limit the user actions. Like you cant upload more than 20 videos to youtube etc. 429 error code.
    Fail-open : If the rate limiter down system goes on like it was never exists. 
    Fail-closed : Whole system goes down with it.
    Clarify the needs up front. Do not design a system unrelated.

    Fixed window algorithm : fixed size requests like in 1 minute only allow 100 request 
    Other algorithms : Sliding window , token bucket , sliding window counter
    Also we can cache the rules for better performance since they are not changing too often.

                Design TinyUrl
    NoSql would be better since we dont need to join any queries etc. We just need to store tinyUrls.
    Prevent Collusion = Url generator also has keys to generate tiny urls and after using them mark them as true in order to use them again. We need to use sql in order to take advantege of ACID
    And also after a tinyurl expired then we can go to the keys database and return the used property to false and use it again.

                Design Twitter
    Functional Requirements : Follow other users , create tweets , view feed
    Non-Functional Requirements : 
        Users : 500M, daily 200M ---> 200M people read 100 tweets per day it makes 20B read/day. 
        Tweets : 1Mb can be because it can be a video --> so it is huge like 20 petabyte daily.
    We can use sharding and user id as shard key in order to make it better. Simply we put people's tweets according to region or relation.

                Design Discord
    Ex / 5 million daily users and 50 million messages per day design a system handles that specific situation. 
        20k user per channel lets say. 10 k messages per channel
    High Level Design:
        Can use polling but not that efficient instead use Websockets
        Discord uses NoSql : at first they used mongoDb but after that they are using cassandra

                Design Youtube
    Ex / 1 billion daily users and 5 billion views 50 million upload
        Availability > Consistency : should be like that because users should view their recommended videos instantly. They can see the latest upload little bit later.
    Youtube uses vitess as a middle layer. Research that.
    
    High Level Design:
        upload : 
            50 million uploads is huge so we have to use load balancer and multiple servers which are scaled horizontally.
            For videos we should obviously use object store.
            Since there are lots of content and large contents we should use queue 
            Should use rate limiter

        And also since it is a huge traffic and involves all parts of the world we should use CDNs
        LRU cache can be implemented



    
// TODO add here



- Sliding Window
- Two Pointers
- Prefix Sums
- Fast and Slow Pointers



Static arr : The problem with static array they have fixed size. Python offers dynamic arrays as default.

Linked List : Consist of nodes -> value and next -> head and tail

Doubly Linked List : extra prev node

Recurcion : Factorial , Fibonacci number : F(n) = F(n-1) + F(n-2) -> F(0) = 0, F(1) = 1

    Sorting

Insertion Sort : every time compare two element in order and swap if it is necessary. it is an iterative solution so it includes loops --> o(n'2)

Merge Sort : divide and conquer -> everytime divide the array to the half of it and sort from the smallest one --> o(nlogn)

Quick Sort : pick a pivot compare numbers with it if it is less then put it into left container etc. --> o(nlogn)

Bucket Sort : if we have small range of members like 0 to 2 -> find the element occurrences and put it in a bucket.

Binary Search : You can use it only if it is sorted. Higher or lower half.

Binary Search Tree : Sorted

LinkedList

Singly linkedList

        Location first
            node.next = head;
            head = node;

        Location last
            node.next = null;
            last.next = node;
            tail = node;

        Somewhere in linkedList not first not last
            Find location with loop
            current.next = node;
            node.next = nextNode;

        Time and Space Complexity

                        Time     Space
            Creation   O(1)      O(1)
            Insertion  O(n)      O(1)
            Searching  O(n)      O(1)
            Traversing O(n)      O(1)
            Delete 1   O(n)      O(1)
            Delete all O(1)      O(1)

Circular Singly LinkedList
Doubly LinkedList
Circular Doubly LinkedList

--------------------------------------------------------------

Stack (LIFO)

    Can use with Array and LinkedList

    Methods = createStack , Push , Pop , Peek , isEmpty , isFull , deleteStack
        Use = Lifo functionality , The chance of data corruption is minimum
        Avoid = Random access is not possible


--------------------------------------------------------------

Queue (FIFO)

    Can use with Array (Linear Queue , Circular Queue) and LinkedList

    Methods = createQueue , Enqueue , Dequeue , Peek , isEmpty , isFull , deleteQueue
        Use = Fifo functionality , The chance of data corruption is minimum
        Avoid = Random access is not possible



--------------------------------------------------------------

Recursion

    Definition = A way of solving a problem by having a function calling itself
        Use = When we can easily break down a problem into similar sub problems - When we need a quick solution instead of efficient one - When traverse a tree - When we use memoization in recursion (Dynamic Programming Subject)
        Avoid = If time and space complexity matters - Uses more memory - Can be slow
        Recursion in 3 steps
            Step 1 - Recursive case - the flow
            Step 2 - Base case - the stopping criterion
            Step 3 - Unintentional case - the constraint


--------------------------------------------------------------

Tree / Binary Tree

    Why = Quicker and easier access to the data - Store hierarchical data, like folder structure, organization structure, XML/HTML data - Unlike linear data structure no need to traverse all the data
    Example = File system in computers
        There are many different types of data structures which performs better in various situations
            - Binary Search Tree (allows finding the closest item very quickly) , AVL , Red Black Tree , Trie
                Tree Terminology
                    root : top node without parent
                    edge : a link between parent and child
                    leaf : a node which does not have children
                    sibling : children of same parent
                    ancestor : parent , grandparent , great-grandparent of a node
                    depth of node : a length of the path from root to node
                    height of node : a length of the path from the node to the deepest node
                    depth of tree : depth of root node
                    height of tree : height of roof node

    Binary Tree
        Binary trees are the data structures in which each node has at most two children, often referred to as the left and right children
        Binary tree is a family of data structure (Binary Search Tree , Heap Tree , AVL , Red Black Trees , Syntax Tree) -> they are all binary tree
            Why -> Huffman coding problem , heap priority problem and expression parsing problems can be solved efficiently using binary trees
        Types of Binary Tree
            Full Binary Tree = 0 or 2 children not 1
            Perfect Binary Tree = Every node has 2 children
            Complete Binary Tree = Except last step all nodes are full
            Balanced Binary Tree =  Left and right side are in equal level
        Binary Tree Traversal
            Depth First Search
                -Preorder traversal -> root-left-right
                -Inorder traversal -> left-root-right
                -Postorder traversal -> left-right-root
            Breadth First Search
                -LevelOrder traversal -> level1-level2 etc.
        Binary Tree with array -> first index empty and left node 2x right node 2x+1 parent i/2



--------------------------------------------------------------

Binary Search Tree

    Binary Search Tree = Left node less than or equal - right node greater
    Why = It performs faster than binary tree when inserting and deleting nodes


--------------------------------------------------------------

Avl Tree

    Avl Tree is a self-balancing Binary Search Tree where the difference between heights of left and right subtrees cannot be more than one for all nodes
    Insertion
        Case 1 = Rotation is not required
        Case 2 = Rotation is required
            LL condition -> Right Rotation(Avl.java 77th line) (Root node becomes right node - left node becomes root - left-left node becomes left)
            LR condition -> Left Rotation(Avl.java 86th line) + Right Rotation(Avl.java 77th line)
            RR condition -> Left Rotation(Avl.java 86th line)
            RL condition -> Right Rotation(Avl.java 77th line) + Left Rotation(Avl.java 86th line)

--------------------------------------------------------------

Binary Heap

    Heap / Priority Queue : Min or max -> pop smallest or largest first

    Binary Heap is a Binary Tree with following properties:
        A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys present in Binary Heap.
        It's a complete tree. All levels are completely filled except possibly the last level and the last level has all keys as left as possible.
        Max heap exactly the opposite of min heap


--------------------------------------------------------------

Trie

    A trie is a tree-based data structure that organizes information in a hierarchy.
        Properties :
            - It is typically used to store or search strings in a space and time efficient way.
            - Any node in trie can store non-repetitive multiple characters.
            - Every node stores link of the next character of the string
            - Every node keeps track of 'end of string'
    Why
        To solve many standard problems in efficient way
            - Spelling checker
            - Auto completion


--------------------------------------------------------------

Hashing

    Hashing is a method of sorting and indexing data. The idea behind hashing is to allow large amounts of data to be indexed using keys commonly created by formulas.
    Why
        It is time efficient in case of SEARCH operations.
            Data Structure |    Time Complexity for Search
            Array          |    O(logN)
            Linked List    |    O(N)
            Tree           |    O(logN)
            Hashing        |    O(1) / O(N)

    Hashing Terminology
        Hash function : It is a function that can be used to map of arbitrary size to data of fixed size.
        Key : Input data by a user
        Hash value : A value that is returned by Hash function
        Hash table (Dictionary or HashMap) : It is a data structure which implements an associative array abstract data type, a structure that can map keys to values
        Collision : A collision occurs when two different keys to a hash function produce the same output.

    Collision Resolution Techniques
        - Direct Chaining : Implements the buckets as linked list. Colliding elements are stored in these lists. If collision occurs then add it into a linked list. Inserting references to hash table.
        - Open Addressing : Create 2x size of current Hash Table and recall hashing for current keys. Colliding elements are stored in other vacant buckets. During storage and lookup these are found through so called probing.
            - Linear Probing : It places new key into the closest following empty cell. If 2 is occupied then move to 3 check if it is occupied or not and then move on to the next empty cell.
            - Quadratic Probing : Adding arbitrary quadratic polynomial to the index until an empty cell is found. Ex / cell 2 is occupied then 2 + 1 square = 3 if 3 is occupied 2 + 2 square 6 ... 3 square etc.
            - Double Hashing : Interval between probes is computed by another hash function. Hash function 2


--------------------------------------------------------------

Sorting Algorithms

    By definition sorting refers to arranging data in a particular format : either ascending or descending.
        Sorting Algorithms
            - Bubble Sort
                Definition : We repeatedly compare each pair of adjacent(near) items and swap them if they are in the wrong order.
            - Selection Sort
                Definition : In case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted.
            - Insertion Sort
                Definition :
                    - Divide the given array into two part
                    - Take first element from unsorted array and find its correct position in sorted array
                    - Repeat until unsorted array is empty
            - Bucket Sort
                Definition :
                    - Create buckets and distribute elements of array into buckets
                    - Sort buckets individually
                    - Merge buckets after sorting
            - Merge Sort
                Definition :
                    - Merge sort is a divide and conquer algorithm
                    - Divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further
                    - Merge halves by sorting them
            - Quick Sort
                Definition :
                    - Quick sort is a divide and conquer algorithm
                    - Find pivot number and make sure smaller numbers located at the left pivot and bigger numbers are located at the right of the pivot
                    - Unlike merge sort extra space is not required
            - Heap Sort
                Definition :
                    - Step 1 : Insert data to Binary heap tree
                    - Step 2 : Extract data from Binary heap
                    - It is best suited with array, it does not work with linked list


--------------------------------------------------------------

Searching Algorithms

    Linear Search : To find the desired element by searching the entire list one by one.
    Binary Search :
        - Binary search is faster than Linear Search.
        - Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one.
        - Binary Search only works for sorted arrays.

--------------------------------------------------------------

Graphs

    Graph consists of a finite set of Vertices(or nodes) and set of Edges which connect a pair of nodes.
    Graph Terminology
        - Vertices(vertex) : Vertices are the nodes of the graph.
        - Edge : The edge is the line that connects pairs of vertices.
        - Unweighted graph : A graph which does not have a weight associated with any edge.
        - Weighted graph :  A graph which has a weight associated with any edge.
        - Undirected graph : In case the edges of the graph do not have a direction associated with them.
        - Directed graph : If the edges in a graph have a direction associated with them.
        - Cyclic graph : A graph which has at least one loop.
        - Acyclic graph : A graph with no loop.
        - Tree : It is special case of directed acyclic graphs.

    If a graph is complete or almost complete we should use Adjacency Matrix
    If the number of edges are few then we should use Adjacency List


--------------------------------------------------------------

BFS-DFS (Breadth First Search ...)

    Breadth First Search :
                - Use queue.
                - BFS is an algorithm for traversing Graph data structure.
                - It starts at some arbitrary node of a graph and explores the neighbor nodes(which are at current level) first, before moving to the next level neighbors.
    Depth First Search :
                - Use stack.
                - DFS is an algorithm for traversing a graph data structure which starts selecting some arbitrary node and explores as far as possible along each edge before backtracking.



--------------------------------------------------------------

Topological Sort

    Topological Sort : Sorts given actions in such a way that if there is a dependency of one action on another, then the dependent action always comes later than its parent action.


--------------------------------------------------------------

Single Source Shortest Path Problem ( SSS_PP )

    Solve with :
        - BFS
        - Dijkstra's Algorithm
        - Bellman Ford

    BFS does not work with weighted Graph. So for weighted problems use dijkstra's algorithm or bellman.
    DFS has the tendency to go "as far as possible" from source, hence it can never find "Shortest path"

--------------------------------------------------------------

Dijkstra's Algorithm

    Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, for example, a road network.

--------------------------------------------------------------

Bellman Ford Algorithm

    Bellman Ford Algorithm is used to find single source shortest path problem. If there is a negative cycle it catches it and report its existance.

--------------------------------------------------------------

Floyd Warshall Algorithm

    Why :
        - The vertex is not reachable
        - Two vertices are directly connected
        - Two vertices are connected via other vertex

--------------------------------------------------------------

Minimum Spanning Tree

    A minimum spanning tree is a subset of the edges of connected, weighted and undirected graph which:
        - Connect all vertices together
        - No cycle
        - Minimum total edge

    Disjoint Set :
        It is a data structure that keeps track of set of elements which are partitioned into a number of disjoint and non overlapping sets and each sets have representative which helps in identifying that sets.
        makeSet(N) , union(x,y) , findSet(x)

--------------------------------------------------------------

Kruskal and Prim 's Algorithms

Kruskal
    It is a greedy algorithm
    It finds a minimum spanning tree for weighted undirected graphs in two steps :
        - Add increasing cost edges at each step
        - Avoid any cycle at each step

Prim
    - Determine an arbitrary vertex as the starting vertex of the MST.
    - Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
    - Find edges connecting any tree vertex with the fringe vertices.
    - Find the minimum among these edges.
    - Add the chosen edge to the MST if it does not form any cycle.
    - Return the MST and exit

--------------------------------------------------------------

Greedy Algorithms

    - Insertion Sort
    - Selection Sort
    - Topological Sort
    - Prim's Algorithm
    - Kruskal Algorithm

    * Activity Selection Problem
        You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
    * Coin Change Problem
        Given an integer array of coins[] of size n representing different types of denominations and an integer sum, the task is to count all combinations of coins to make a given value sum.
    * Fractional Knapsack Problem
        Given the weights and profits of N items, in the form of {profit, weight} put these items in a knapsack of capacity W to get the maximum total profit in the knapsack. In Fractional Knapsack, we can break items for maximizing the total value of the knapsack.

--------------------------------------------------------------

Divide and Conquer Algorithms

    - Merge Sort
    - Quick Sort

    * Number Factor
    * House Robber
    * Convert one string to another
    * Zero one knapsack
    * Longest common subsequence
    * Longest palindromic subsequence
    * Minimum cost to reach last cell
    * Number of paths to reach the last cell with given cost

--------------------------------------------------------------

Dynamic Programming

    - Dynamic programming is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the
    optimal solution to the overall problem depends upon the optimal solution to its subproblems.

    Top Down with Memoization :
        Solve the bigger problem by recursively finding the solution to smaller subproblems. Whenever we solve a sub-problem, " we cache its result " so that
        we don't end up solving it repeatedly if it's called multiple times. This technique of storing the results of already solved subproblems is called * Memoization *.

    Bottom Up with Tabulation :
        Tabulation is the opposite of the top-down approach and avoids recursion. In this approach, we solve the problem "bottom-up" . This is done by filling up a
        table. Based on the results in the table, the solution to the top/original problem is the computed.


--------------------------------------------------------------

Problem Solving Recipe
    - Step 1 : Understand the problem
    - Step 2 : Explore examples
    - Step 3 : Break it down
    - Step 4 : Solve
    - Step 5 : Look back and refactor

--------------------------------------------------------------

Backtracking

    Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end.
    It is commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like Sudoku.
    When a dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted.





"""