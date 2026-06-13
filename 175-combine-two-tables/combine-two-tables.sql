-- Write your PostgreSQL query statement belo
SELECT firstName,lastName, city, state
FROM person 
LEFT JOIN address
ON person.personID = address.personId