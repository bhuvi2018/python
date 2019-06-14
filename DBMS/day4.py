#ex25
SELECT COUNT(*) as SALE_COUNT FROM SALE WHERE SYSDATE-SLDATE<1800

#COL40
SELECT DISTINCT ITEMTYPE,
CASE WHEN Price BETWEEN 0 AND 499 THEN 'Cheap' 
WHEN Price BETWEEN 500 AND 1999 THEN 'Affordable'
WHEN Price BETWEEN 2000 AND 4999 THEN 'Expensive'
WHEN Price>=5000 THEN 'Very Expensive' 
END AS CLASSIFICATION
FROM ITEM 
ORDER BY ITEMTYPE,CLASSIFICATION ASC

#col41
SELECT
CASE
WHEN EXTRACT(MONTH FROM QDATE)=1 THEN 'January'
WHEN EXTRACT(MONTH FROM QDATE)=2 THEN 'Feburaray'
WHEN EXTRACT(MONTH FROM QDATE)=3 THEN 'March'
WHEN EXTRACT(MONTH FROM QDATE)=4 THEN 'April'
WHEN EXTRACT(MONTH FROM QDATE)=5 THEN 'May'
WHEN EXTRACT(MONTH FROM QDATE)=6 THEN 'June'
WHEN EXTRACT(MONTH FROM QDATE)=7 THEN 'JULY'
WHEN EXTRACT(MONTH FROM QDATE)=8 THEN 'AUGEST'
WHEN EXTRACT(MONTH FROM QDATE)=9 THEN 'SEPTEMBER'
WHEN EXTRACT(MONTH FROM QDATE)=10 THEN 'October'
WHEN EXTRACT(MONTH FROM QDATE)=11 THEN 'November'
WHEN EXTRACT(MONTH FROM QDATE)=12 THEN 'DECEMBER' 
END AS MONTH ,COUNT(*) AS QUOTATIONCOUNT
FROM QUOTATION 
GROUP BY EXTRACT(MONTH FROM QDATE) 
