UPDATE Person SET age=27 WHERE last_name='Snow' AND first_name='Jon';
UPDATE Person SET age=18 WHERE last_name='White' AND first_name='Walter Junior';

/*DELETE FROM Person JOIN EyesColor ON Person.id = EyesColor.person_id WHERE last_name='White' AND first_name='Walter';*/

/*SELECT id INTO temp FROM Person JOIN EyesColor ON Person.id = EyesColor.person_id;*/

DELETE FROM Person WHERE last_name='White' AND first_name='Walter';
DELETE FROM EyesColor WHERE last_name='White' AND first_name='Walter';
