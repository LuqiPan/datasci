SELECT MAX(value), docid FROM (
  SELECT SUM(a.count * b.count) value, b.docid docid
  FROM with_query a, with_query b
  WHERE a.term = b.term
        AND a.docid = "q"
        AND b.docid <> "q"
  GROUP BY b.docid
);
