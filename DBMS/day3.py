#ex10
INSERT INTO Salesman VALUES(11, 'Elizabeth', 'London')

#ex11
INSERT INTO Product VALUES(110, 'Bat', 50, 'Sports', NULL)

#ex12
SELECT * FROM Product

#ex13
SELECT DISTINCT PRODID , PRICE , CATEGORY FROM Product

#ex14
SELECT DISTINCT CATEGORY FROM Product

#ex15
SELECT PRODID , PDESC , CATEGORY ,DISCOUNT
FROM Product WHERE CATEGORY='Apparel'

#ex16
SELECT PRODID, PDESC , CATEGORY ,DISCOUNT FROM Product WHERE PDESC IS NULL

#ex17
SELECT PRODID, PDESC , CATEGORY ,DISCOUNT FROM Product WHERE CATEGORY='Apparel' AND DISCOUNT>5

#ex18
UPDATE Product SET DISCOUNT=25 WHERE CATEGORY='Sports'

#ex19
UPDATE Product SET PRICE=50 WHERE CATEGORY='Apparel' AND PDESC='Trouser'

#ex20
UPDATE Salesman SET SNAME='Jenny' ,LOCATION='Bristol' WHERE SID=3

#ex21
DELETE FROM SaleDetail WHERE SALEID=1004

#ex22
DELETE FROM SaleDetail WHERE QUANTITY>5

#col16
INSERT INTO Article VALUES( 'A1001' ,'Mouse',500,0,'C')

#Ass17
INSERT INTO Store VALUES('Loyal World','Infy Campus, Mysore','Rohan Kumar');

#ass18
INSERT INTO Bill VALUES(1001,'Loyal World',101,'A1001',1000,'20-OCT-15',2);

#ass19
INSERT INTO Supplier VALUES('S501','Avaya Ltd',9012345678,'Mysore');

#ass20
SELECT DESCR,PRICE FROM Item WHERE DESCR LIKE '%Hard disk'

#ass21
SELECT QUOTATIONID,SNAME,ITEMCODE,QUOTEDPRICE,	QDATE,QSTATUS FROM Quotation WHERE QSTATUS='Rejected' OR QSTATUS='Closed'

