  SELECT sum(a.count * b.count)
  FROM frequency a, frequency b
  WHERE a.term = b.term
        AND a.docid = "10080_txt_crude" AND b.docid = "17035_txt_earn";
