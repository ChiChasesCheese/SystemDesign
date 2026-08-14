---
id: analytics-star-schema
node: analytics.olap
type: qa
---
## Q
Describe the star schema, and why warehouses tolerate wide, denormalized dimension tables that would be bad OLTP design.

## A
One huge **fact table** of events (sale, click, shipment) — each row a narrow record of foreign keys plus numeric measures — surrounded by **dimension tables** (who/what/where/when: product, customer, date) that give the keys meaning.

Facts are append-only and billions of rows; dimensions are small (thousands–millions) and change rarely. Denormalizing dimensions (flattening the "snowflake") is fine because update anomalies barely matter for slowly-changing reference data, while fewer joins means simpler, faster queries.

Analysts' queries then follow one shape: filter/group by dimension attributes, aggregate fact measures.
