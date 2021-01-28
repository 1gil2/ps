--level 3

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B ON B.ANIMAL_ID = A.ANIMAL_ID
WHERE B.DATETIME < A.DATETIME
ORDER BY A.DATETIME