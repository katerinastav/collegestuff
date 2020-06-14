https://www.dbta.com/Columns/DBA-Corner/Top-10-Steps-to-Building-Useful-Database-Indexes-100498.aspx

Examples:

* Create Index 
``` create unique index bezoeken_primary_key_idx
on bezoeken (reisnr, volgnr);
```
* View size of db
```SELECT pg_size_pretty(pg_total_relation_size('ruimtereizen.bezoeken')); ``` 
* Delete Index
``` DROP INDEX schema_name.index_name; ```
! Index on primary key almost same size with table.
* Compare execution speed 
``` EXPLAIN ANALYSE querry ```

