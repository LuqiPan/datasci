SELECT value FROM(
  SELECT sum(a.value * b.value) as value, a.row_num, b.col_num
  FROM a, b
  WHERE a.col_num = b.row_num
  GROUP BY a.row_num, b.col_num
)
WHERE row_num = 2 AND col_num = 3;
