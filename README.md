# Parallelised Data Backup Using Merkle Trees
With the ever-increasing amount of data generated and processed daily, ensuring data integrity and security has become a critical challenge for many organizations. Merkle trees have emerged as a popular data structure for backup and verification systems due to their ability to detect data tampering and provide efficient integrity checks.

Data backup using hash trees is a technique that involves breaking down large datasets into smaller chunks, creating separate hash trees for each chunk, and comparing the root hash of the tree with a previously stored version to determine if any data has been modified. This method allows for efficient and secure data backups, particularly for large datasets and incremental backups.
 
 ## Table Comparing the Codes

| S. No. | Size of Folder (in MBs) | Number of Files | Serial Implementation (in seconds) | Parallel Implementation (in seconds) | Speedup  |
| ------ | ----------------------- | --------------- | ---------------------------------- | ------------------------------------ | -------- |
| 1      | 2290                    | 5856            | 10.21                              | 11.54                                | 0.884749 |
| 2      | 809                     | 8539            | 13.58                              | 12.88                                | 1.054348 |
| 3      | 386                     | 24335           | 18.9                               | 14.52                                | 1.301653 |
| 4      | 230                     | 75001           | 30.89                              | 15.98                                | 1.933041 |
| 5      | 1430                    | 87900           | 43.75                              | 17.56                                | 2.491458 |


## Graph for the Comparison
![Serial Vs Parallel](https://github.com/dipsikhade/backup-using-merkle-trees/blob/main/graph.png)
