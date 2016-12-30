### replica set
[replica set](https://docs.mongodb.com/manual/replication/#replication)

#### what is replica set and what is it for
>A replica set in MongoDB is a group of mongod processes that maintain the same data set. Replica sets provide redundancy(冗余，备份) and high availability, and are the basis for all production deployments. 
>
>With multiple copies of data on different database servers, replication provides a level of fault tolerance(容错功能) against the loss of a single database server.
>
>In some cases, replication can provide increased read capacity as clients can send read operations to different servers.

#### how it works
> A replica set contains several data bearing nodes(轴节点) and optionally one arbiter node(仲裁节点),Of the data bearing nodes, one and only one member is deemed(被视为) the primary node, while the other nodes are deemed secondary nodes.
> 
> The primary node receives all write operations. A replica set can have only one primary capable of confirming writes with { w: "majority" } write concern; although in some circumstances(情况), another mongod instance may transiently(暂时的) believe itself to also be primary. [1] The primary records all changes to its data sets in its operation log.

![](https://docs.mongodb.com/manual/_images/replica-set-read-write-operations-primary.png)

>The secondaries replicate the primary’s oplog and apply the operations to their data sets such that the secondaries’ data sets reflect the primary’s data set. If the primary is unavailable, an eligible(合适的) secondary will hold an election(选举) to elect(选择) itself the new primary.

![](https://docs.mongodb.com/manual/_images/replica-set-primary-with-two-secondaries.png)

>You may add an extra mongod instance to a replica set as an arbiter. Arbiters do not maintain a data set. The purpose of an arbiter is to maintain a quorum(仲裁) in a replica set by responding to heartbeat and election requests by other replica set members. 

![](https://docs.mongodb.com/manual/_images/replica-set-primary-with-secondary-and-arbiter.png)

>An arbiter will always be an arbiter whereas a primary may step down and become a secondary and a secondary may become the primary during an election.