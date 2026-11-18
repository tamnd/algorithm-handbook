## History

Stored query results are as old as relational systems, but their maintenance became a research subject in the 1980s. José Blakeley, Per-Åke Larson and Frank Tompa gave delta rules for select-project-join views in 1986, with a test for updates that cannot change a view. In 1993 Ashish Gupta, Inderpal Singh Mumick and V. S. Subrahmanian published the counting algorithm for nonrecursive views and the DRed algorithm for recursive ones, in *Maintaining Views Incrementally*. Timothy Griffin and Leonid Libkin gave delta rules for the whole bag algebra in 1995.

Data warehouses made the subject practical. Views over remote sources had to be maintained without querying the sources, which led to self-maintainable views, studied by Dallan Quass and others in 1996. Latha Colby and her colleagues described deferred maintenance in the same year, including the error of computing a delta against the state after the update. Gupta and Mumick surveyed the field in 1995, and Alon Halevy surveyed the related use of views for answering queries in 2001.

Later work made incremental computation a general method. Christoph Koch showed in 2010 that the delta of a delta is simpler again, and built higher-order maintenance into the DBToaster system. Christoph Berkholz, Jens Keppeler and Nicole Schweikardt characterized in 2017 the conjunctive queries whose results can be maintained with constant time per update. Dataflow systems such as differential dataflow and DBSP apply the same algebra of changes to streams and to recursive programs, and Boris Motik and his colleagues gave alternatives to DRed for Datalog reasoners.

## Further reading

- Ashish Gupta, Inderpal Singh Mumick and V. S. Subrahmanian, *Maintaining Views Incrementally*, SIGMOD 1993. Counting and DRed.
- Ashish Gupta and Inderpal Singh Mumick, *Maintenance of Materialized Views: Problems, Techniques, and Applications*, IEEE Data Engineering Bulletin 18(2), 1995. A short survey of the field.
- Timothy Griffin and Leonid Libkin, *Incremental Maintenance of Views with Duplicates*, SIGMOD 1995. Delta rules for the bag algebra.
- Christoph Koch, *Incremental Query Evaluation in a Ring of Databases*, PODS 2010. Higher-order delta processing.
