UPDATE Person SET age=27 WHERE last_name='Snow' AND first_name='Jon';
UPDATE Person SET age=18 WHERE last_name='White' AND first_name='Walter Junior';

DELETE FROM Person WHERE id=1;
DELETE FROM EyesColor WHERE person_id=1;
