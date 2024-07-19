INSERT INTO whatisfordinner_family (
    family_id,
    family_name,
    creation_date,
    activity_status,
    suggestion_deadline,
    dinner_deadline
  )
VALUES (
    2,
    'Johnsonville',
    '2020-01-03',
    'Active',
    '18:30:00',
    '18:30:00'
  );
INSERT INTO whatisfordinner_family (
    family_id,
    family_name,
    creation_date,
    activity_status,
    suggestion_deadline,
    dinner_deadline
  )
VALUES (
    1,
    'Pants',
    '2020-01-03',
    'Active',
    '18:30:00',
    '18:30:00'
  );
INSERT INTO whatisfordinner_member (
    member_id,
    first_name,
    last_name,
    email,
    family_id
  )
VALUES (
    1,
    'John',
    'Pants',
    'john.pants@sample.com',
    1
  );