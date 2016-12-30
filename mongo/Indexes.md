# index in mongo
## performance test
Useing `maxnews.data2news` from `host_ip:port` 

```bash
>db.runCommand({cloneCollection:'maxnews.dota2news', from:'host_ip:port'})
>db.dota2news.count()
5748

# without index
> db.dota2news.find({'title': {$regex: 'dota'}}).explain()
{
	"cursor" : "BasicCursor",
	"isMultiKey" : false,
	"n" : 32,
	"nscannedObjects" : 5748,
	"nscanned" : 5748,
	"nscannedObjectsAllPlans" : 5748,
	"nscannedAllPlans" : 5748,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 12,
	"indexBounds" : {
		
	},
}
> db.dota2news.find({'title': {$regex: 'dota|EHOME|IG|EG|LGD'}}).explain()
{
	"cursor" : "BasicCursor",
	"isMultiKey" : false,
	"n" : 235,
	"nscannedObjects" : 5748,
	"nscanned" : 5748,
	"nscannedObjectsAllPlans" : 5748,
	"nscannedAllPlans" : 5748,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 34,
	"indexBounds" : {
		
	},
}
> db.dota2news.find({'title': {$regex: 'dota|max|EHOME'}, 'content': {$regex: 'EHOME|IG|LGD|EG'}}).explain()
{
	"cursor" : "BasicCursor",
	"isMultiKey" : false,
	"n" : 199,
	"nscannedObjects" : 5748,
	"nscanned" : 5748,
	"nscannedObjectsAllPlans" : 5748,
	"nscannedAllPlans" : 5748,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 63,
	"indexBounds" : {
		
	},
}

# with title index
>db.dota2news.createIndex({title: 1})
>db.dota2news.find({'title': {$regex: 'dota2'}}).explain()
{
	"cursor" : "BtreeCursor title_1 multi",
	"isMultiKey" : false,
	"n" : 32,
	"nscannedObjects" : 32,
	"nscanned" : 5748,
	"nscannedObjectsAllPlans" : 32,
	"nscannedAllPlans" : 5748,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 10,
	"indexBounds" : {
		"title" : [
			[
				"",
				{
					
				}
			],
			[
				/dota/,
				/dota/
			]
		]
	},
}
>db.dota2news.find({title: {$regex: "dota|EHOME|IG|LGD|EG"}}).explain()
{
	"cursor" : "BtreeCursor title_1 multi",
	"isMultiKey" : false,
	"n" : 799,
	"nscannedObjects" : 799,
	"nscanned" : 5748,
	"nscannedObjectsAllPlans" : 799,
	"nscannedAllPlans" : 5748,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 34,
	"indexBounds" : {
		"title" : [
			[
				"",
				{
					
				}
			],
			[
				/dota|EHOME|IG|LGD|EG/,
				/dota|EHOME|IG|LGD|EG/
			]
		]
	},
}
>db.dota2news.find({'title': {$regex: 'dota|max|EHOME'}, 'content': {$regex: 'EHOME|IG|LGD|EG'}}).explain()
{
	"cursor" : "BtreeCursor title_1 multi",
	"isMultiKey" : false,
	"n" : 199,
	"nscannedObjects" : 235,
	"nscanned" : 5748,
	"nscannedObjectsAllPlans" : 2260,
	"nscannedAllPlans" : 7773,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 80,
	"indexBounds" : {
		"title" : [
			[
				"",
				{
					
				}
			],
			[
				/dota|max|EHOME/,
				/dota|max|EHOME/
			]
		]
	},
}

# with text-content combined index
>db.dota2news.createIndex({title:1, content:1})
>db.dota2news.find({'title': {$regex: 'dota2'}}, {'content': {$regex: 'EHOME'}}).explain()
{
	"cursor" : "BtreeCursor title_1_content_1 multi",
	"isMultiKey" : false,
	"n" : 0,
	"nscannedObjects" : 0,
	"nscanned" : 555,
	"nscannedObjectsAllPlans" : 556,
	"nscannedAllPlans" : 1666,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 5,
	"indexBounds" : {
		"title" : [
			[
				"",
				{
					
				}
			],
			[
				/dota/,
				/dota/
			]
		],
		"content" : [
			[
				"",
				{
					
				}
			],
			[
				/EHOME/,
				/EHOME/
			]
		]
	},
}
>db.dota2news.find({'title': {$regex: 'dota|max|EHOME'}, 'content': {$regex: 'EHOME|IG|LGD|EG'}}).explain()
{
	"cursor" : "BtreeCursor title_1_content_1 multi",
	"isMultiKey" : false,
	"n" : 53,
	"nscannedObjects" : 14,
	"nscanned" : 555,
	"nscannedObjectsAllPlans" : 584,
	"nscannedAllPlans" : 1666,
	"scanAndOrder" : false,
	"indexOnly" : false,
	"millis" : 16,
	"indexBounds" : {
		"title" : [
			[
				"",
				{
					
				}
			],
			[
				/dota|max|EHOME/,
				/dota|max|EHOME/
			]
		],
		"content" : [
			[
				"",
				{
					
				}
			],
			[
				/EHOME|IG|LGD|EG/,
				/EHOME|IG|LGD|EG/
			]
		]
	},
}


>db.dota2news.status()
{
	"ns" : "maxnews.dota2news",
	"count" : 5748,
	"size" : 37038032,
	"avgObjSize" : 6443.63813500348,
	"storageSize" : 41570304,
	"numExtents" : 6,
	"nindexes" : 6,
	"lastExtentSize" : 20971520,
	"totalIndexSize" : 2125760,
	"indexSizes" : {
		"_id_" : 196224,
		"newsid_1" : 179872,
		"timestamp_-1_type_1_show_1" : 261632,
		"title_text" : 613200,
		"title_1" : 416976,
		"title_1_content_1" : 457856
	},
	"ok" : 1
}
```