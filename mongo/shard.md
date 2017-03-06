# sharding
>Sharding is a method for distributing data across multiple machines. MongoDB uses sharding to support deployments with **very large data sets** and **high throughput operations**.

>MongoDB supports horizontal scaling through sharding.

>MongoDB shards data at the **collection level**, distributing the collection data across the shards in the cluster.

## sharded cluster
A MongoDB sharded cluster consists of the following components:

* **shard**: Each shard contains a subset of the sharded **data**. Each shard can be deployed as a replica set.
* **mongos**: The mongos acts as a **query router**, providing an interface between client applications and the sharded cluster.
* **config servers**: Config servers store **metadata and configuration settings** for the cluster. As of MongoDB 3.4, config servers must be deployed as a replica set (CSRS). 

### Production configuration
![](https://docs.mongodb.com/manual/_images/sharded-cluster-production-architecture.png)

### Development configuration
![](https://docs.mongodb.com/manual/_images/sharded-cluster-test-architecture.png)

## Shard keys

## A balance cluster
MongoDB ensures a balanced cluster using two processes: **chunk splitting** and the **balancer**.

### Data Partitioning with Chunks
MongoDB uses the shard key associated to the collection to partition the data into **chunks**. A chunk consists of a subset of sharded data. Each chunk has a inclusive lower and exclusive upper range based on the shard key.

The mongos routes writes to the appropriate chunk based on the shard key value.  MongoDB splits chunks when they grows beyond the configured chunk size  or if the number of documents in the chunk exceeds `Maximum Number of Documents Per Chunk to Migrate`. Both inserts and updates can trigger a chunk split.

The smallest range a chunk can represent is a single unique shard key value. A chunk that only contains documents with a single shard key value cannot be split.

To create splits, MongoDB does **not** migrate any data or affect the shards. Splits may lead to an uneven distribution of the chunks for a collection across the shards. In such cases, the balancer redistributes chunks across shards.

The balancer is a background process that manages chunk migrations. If **the difference** in number of chunks between the largest and smallest shard exceed the migration thresholds, the balancer begins migrating chunks across the cluster to ensure an even distribution of data.

`moveChunk directory`. If some error occurs during a migration, these files may be helpful in recovering documents affected during the migration.

### Sharded Cluster Balancer
The MongoDB balancer is a background process that monitors the number of chunks on each shard. When the number of chunks on a given shard reaches specific migration thresholds, the balancer attempts to automatically migrate chunks **between shards** and reach an equal number of chunks per shard.

The balancing procedure for sharded clusters is entirely transparent to the user and application layer, though there may be some performance impact while the procedure takes place.

Changed in 3.4: The balancer runs on the **primary** of the **config server** replica set.

Chunk migrations carry some overhead in terms of bandwidth and workload, both of which can impact database performance. 
