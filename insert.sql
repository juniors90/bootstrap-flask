INSERT INTO blog_user (
	id,
	name,
	email,
	password,
    is_admin
)
VALUES
	(
        5,
		'Dustin Johnson',
		'DustinJohnson@gmail.com',
        'pbkdf2:sha256:260000$M0S2DdZl84QUk8Zb$e94bdb27dd4f1ed96ade0c8f8875c942c7194aff650659c186adf0438cd95b53',
        't'
	);