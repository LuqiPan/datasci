CREATE VIEW with_query AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT MAX(value) FROM (
  SELECT SUM(a.count * b.count) value
  FROM with_query a, with_query b
  WHERE a.term = b.term
        AND a.docid = "q"
  GROUP BY b.docid
);
