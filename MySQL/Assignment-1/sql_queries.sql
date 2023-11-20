-- 1. Count the number of Salesperson whose name begin with ‘a’/’A’.

SELECT COUNT(*)
FROM SalesPeople
WHERE UPPER(SUBSTRING(Sname, 1, 1)) = 'A';


-- 2.  Display all the Salesperson whose all orders worth is more than Rs. 2000.

SELECT S.Snum, S.Sname
FROM SalesPeople S
WHERE NOT EXISTS (
    SELECT O.Snum
    FROM Orders O
    WHERE O.Snum = S.Snum AND O.Amt <= 2000
);


-- 3. Count the number of Salesperson belonging to Newyork

SELECT COUNT(*)
FROM SalesPeople
WHERE City = 'Newyork';


-- 4. Display the number of Salespeople belonging to London and belonging to Paris.

SELECT City, COUNT(*)
FROM SalesPeople
WHERE City IN ('London', 'Paris')
GROUP BY City;


-- 5. Display the number of orders taken by each Salesperson and their date of orders.

SELECT S.Snum, S.Sname, COUNT(O.Onum) AS NumberOfOrders, O.Odate
FROM SalesPeople S
JOIN Orders O ON S.Snum = O.Snum
GROUP BY S.Snum, S.Sname, O.Odate;
