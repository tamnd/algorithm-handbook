## History

Recovery was designed together with the first transaction systems. Raymond Lorie described shadow pages in 1977, as the method of the System R storage layer for keeping a consistent copy of each file. Jim Gray's *Notes on Data Base Operating Systems* of 1978 set out the write-ahead log, the commit rule, two-phase commit and the idea of a transaction as the unit of recovery. In 1981 Gray and his colleagues reported on the recovery manager of System R and found that shadow pages were costly next to the log, which was needed anyway.

Theo Haerder and Andreas Reuter gave the field its vocabulary in 1983, in *Principles of Transaction-Oriented Database Recovery*. They named the ACID properties and classified recovery methods by the steal and force choices of the buffer manager, by how they propagate changes, and by the kind of checkpoint they take. Their taxonomy explained why the fastest buffer policy, steal with no-force, needs both undo and redo.

Group commit appeared in IMS Fast Path in the late 1970s, and was studied by David DeWitt and his colleagues for main memory databases in 1984. In 1992 C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh and Peter Schwarz published ARIES. It combined the write-ahead log, a log sequence number on each page, fuzzy checkpoints, repeating history and compensation log records, and it supported record-level locking and logical undo. ARIES became the reference design, and IBM DB2, Microsoft SQL Server and many other systems use variants of it.

Later work changed the hardware assumptions. Copy-on-write B-trees, as in LMDB, revived shadow paging for embedded stores. Main memory systems log commands or logical records in place of page images, and new storage devices have led to proposals such as write-behind logging and instant restart.

## Further reading

- Theo Haerder and Andreas Reuter, *Principles of Transaction-Oriented Database Recovery*, ACM Computing Surveys 15(4), 1983. The steal and force taxonomy and the ACID properties.
- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh and Peter Schwarz, *ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging*, ACM Transactions on Database Systems 17(1), 1992. The full algorithm, with many design discussions.
- Jim Gray and Andreas Reuter, *Transaction Processing: Concepts and Techniques*, Morgan Kaufmann, 1993. Logging, buffers and recovery as real systems build them.
- Raghu Ramakrishnan and Johannes Gehrke, *Database Management Systems*, 3rd edition, McGraw-Hill, 2003. A textbook account of ARIES with worked logs.
- Philip A. Bernstein, Vassos Hadzilacos and Nathan Goodman, *Concurrency Control and Recovery in Database Systems*, Addison-Wesley, 1987. The recovery chapters give the model of the crash recovery problem.
