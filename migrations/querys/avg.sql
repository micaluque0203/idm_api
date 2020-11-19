select avg(count)
        from(SELECT users.ip,
        count(*) as count
        FROM users
        WHERE users.iso_code='{iso_code}'
        GROUP BY 1) as counts