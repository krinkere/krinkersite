Title: How to move ElasticSearch data directory
Date: 2018-06-08 14:14
Modified: 2018-06-08 14:30
Status: published
Category: How To article
Tags: elasticsearch, devops
Slug: how_to_move_elasticsearch_data_directory
Authors: Al Krinker
Summary: When directory of ES data is full, you need to move it in order to avoid index read-only error

I was currently working on a project where I had to ingest massive amounts of data into ElasticSearch and I defaulted to /var/lib/elasticsearch to store all of my data. 
I admit it was a mistake as I soon was starring at a 403 error from my cluster.

```console
{
  "type": "cluster_block_exception",
  "reason": "blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];"
}
```
After quick google search and verifying that I was truly low on space by issusing df -h command, I had to move my data. Below are the steps that I took<br />
1. Determine current location of data files, if in doubt (curl "localhost:9200/_nodes/settings?pretty=true")<br />
2. Figure out where you have space and create a directory in it, let's say mega_elasticdata_dir<br />
3. Stop ElastiSearch service: systemctl stop elasticsearch.service<br />
4. Navigate to the current data directory determined in step 1 and move or copy files to new location (cp -RP * /mega_elasticdata_dir/)<br />
5. Change ownership on new directory to elasticsearch (sudo chown -R elasticsearch:elasticsearch /mega_elasticdata_dir)<br />
6. Edit data path inside of /etc/elasticsearch/elasticsearch.yml by changing parameter “path.data:”<br />
7. Start ElasticSearch service again (systemctl start elasticsearch.service)<br />
8. Check ElasticSearch log for any errors (tail -500f /var/log/elasticsearch/elasticsearch.log)<br />

At this point, you have moved the data, but if you were to try to index any data, you would still get the same error message even now that you have plenty of space.
This is because ElasticSearch has switched to read-only mode when it could not index more documents (when the hard drive got full). This is done to ensure 
availability for read-only queries. ElasticSearch will not switch back automatically and you have to reset the flag manually by sending following command

```console
curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
```

References:<br />
[ElasticSearch Settings](https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html)<br />
[Disk Allocator](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/disk-allocator.html)